from django.shortcuts import *
from django.utils.html import escape

# Import models
from django.db import models
from django.contrib.auth.models import *
from fuelup.api.models import *

#REST API
from rest_framework import viewsets
from fuelup.api.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import *
from rest_framework import filters

class Session(APIView):
    permission_classes = (AllowAny,)
    def form_response(self, isauthenticated, userid, username, error=""):
        data = {
            'isauthenticated': isauthenticated,
            'userid': userid,
            'username': username
        }
        if error:
            data['message'] = error

        return Response(data)

    def get(self, request, *args, **kwargs):
        # Get the current user
        if request.user.is_authenticated():
            return self.form_response(True, request.user.id, request.user.username)
        return self.form_response(False, None, None)

    def post(self, request, *args, **kwargs):
        # Login
        username = escape(request.POST.get('username'))
        password = escape(request.POST.get('password'))
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return self.form_response(True, user.id, user.username)
            return self.form_response(False, None, None, "Account is suspended")
        return self.form_response(False, None, None, "Invalid credentials")

    def delete(self, request, *args, **kwargs):
        # Logout
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

def home(request):
  """
  Send requests to / to the ember.js clientside app
  """
  return render_to_response('index.html', {}, RequestContext(request))

class UserList(APIView):
    """
    Create a new user
    """
    permission_classes = (AllowAny,)
    def form_response(self, username, password, error=""):
        data = {
            'username': username,
            'password': password
        }
        if error:
            data['message'] = error

        return Response(data)

    def get(self, request, format=None):
        user = User.objects.all() #you could limit this to only the posts for which the user has access
        serializer = UserSerializer(user, many=True, context={'request': request})
        return Response(serializer.data) #you can customize the response here
    
    def post(self, request, *args, **kwargs):
    # def post(self, request, format=None):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.exists():
            return self.form_response("Username has been taken. Please choose another.")
        user = User.create_user(username=username, password=password)
        user.save()

        # serializer = UserSerializer(data=request.data, context={'request': request})
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED) #you could customize the response here
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #you could customize the error message here

class UserDetail(APIView):
    """
    Retrieve, update or delete a single user.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        User = self.get_object(pk)
        serializer = UserSerializer(User, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        User = self.get_object(pk)
        serializer = UserSerializer(User, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        User = self.get_object(pk)
        User.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VehicleList(APIView):
    """
    List all vehicles, or create a new vehicle.
    """
    def get(self, request, format=None):
        # Get vehicles only belonging to the user
        vehicle = Vehicle.objects.filter(user__username=request.user.username)
        serializer = VehicleSerializer(vehicle, many=True, context={'request': request})
        return Response(serializer.data) #you can customize the response here
    
    def post(self, request, format=None, *args, **kwargs):
        modelYear = escape(request.POST.get('year'))
        brand = escape(request.POST.get('make'))
        serializer = VehicleSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            if checkYear(modelYear):
                if checkModels(brand):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED) #you could customize the response here
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #{"errors": {"make": ["Invalid vehicle make!"],}})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #{"errors": { "year": ["Vehicle year must be 1900-2016!"],}})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #you could customize the error message here

class VehicleDetail(APIView):
    """
    Retrieve, update or delete a single vehicle.
    """
    def get_object(self, pk):
        try:
            return Vehicle.objects.filter(id=2)
            # return Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Vehicle = Vehicle.objects.filter(id=2)
        # Vehicle = self.get_object(pk)
        serializer = VehicleSerializer(Vehicle, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Vehicle = self.get_object(pk)
        serializer = VehicleSerializer(Vehicle, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Vehicle = self.get_object(pk)
        Vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#more detailed, but more control class based view example
class FillupList(APIView):
    """
    List all Fillups, or create a new Fillup.
    """
    def get(self, request, format=None):
        # Get Fillups belonging only to the user
        fillup = Fillup.objects.filter(vehicle__user__username=request.user.username)
        serializer = FillupSerializer(fillup, many=True, context={'request': request})
        return Response(serializer.data) #you can customize the response here
    
    def post(self, request, format=None):
        serializer = FillupSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) #you could customize the response here
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #you could customize the error message here

class FillupDetail(APIView):
    """
    Retrieve, update or delete a single Fillup.
    """
    def get_object(self, pk):
        try:
            return Fillup.objects.get(pk=pk)
        except Fillup.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Fillup = Fillup.objects.filter(id="2")
        # Fillup = self.get_object(pk)
        serializer = FillupSerializer(Fillup, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Fillup = self.get_object(pk)
        serializer = FillupSerializer(Fillup, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Fillup = self.get_object(pk)
        Fillup.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sessions to be viewed.
    """
    def get(self, request, *args, **kwargs):
        # # Get the current user
        # request.user.is_authenticated():
            return request.user.all()