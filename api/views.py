from django.shortcuts import *

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

#more detailed, but more control class based view example
class FillupList(APIView):
    """
    List all Fillups, or create a new Fillup.
    """
    def get(self, request, format=None):
        Fillup = Fillup.objects.all() #you could limit this to only the posts for which the user has access
        serializer = FillupSerializer(Fillup, many=True, context={'request': request})
        return Response(serializer.data) #you can customize the response here
    
    def post(self, request, format=None):
        serializer = ForumpostSerializer(data=request.data, context={'request': request})
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
        Fillup = self.get_object(pk)
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

class FillupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows for CRUD operations on Fillup objects.
    """
    queryset = Fillup.objects.all()
    serializer_class = FillupSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows for CRUD operations on Vehicle objects.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer