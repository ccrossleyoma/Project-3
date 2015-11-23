from django.shortcuts import *

# Import models
from django.db import models
from django.contrib.auth.models import *
from myapp.api.models import *

#REST API
from rest_framework import viewsets
from myapp.api.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status