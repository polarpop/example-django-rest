# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.serializers import ProfileSerializer, LocationSerializer
from api.models import Profile, Location

class UserViewset(viewsets.ModelViewSet):
  serializer_class = ProfileSerializer
  queryset = Profile.objects.all()
  permission_classes = [IsAuthenticated]


class LocationViewset(viewsets.ModelViewSet):
  serializer_class = LocationSerializer
  queryset = Location.objects.all()
  permission_classes = [IsAuthenticated]

