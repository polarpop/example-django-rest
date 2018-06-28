# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from api.models import Profile, Location


class LocationSerializer(serializers.ModelSerializer):
  '''
  This is our serializers for locations. In a more
  complex setup you will go ahead and create different
  files for these serializers, as well create a base
  serializer. Giving you the ability to customize the
  data you want serialized.  See below for further
  reading on serializers.

  https://www.django-rest-framework.org/api-guide/serializers/  

  '''

  class Meta:
    model = Location
    fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
  '''
  This is the user profile serializer. A serializer
  is something that will help you validate / clean
  data requests coming into the API. 

  For example, if someone wants to create a user,
  and the username field already exists. Then it will
  throw an error in a JSON or XML response depending on
  the viewset. 

  https://www.django-rest-framework.org/api-guide/serializers/

  '''
  branch = LocationSerializer()

  class Meta:
    model = Profile
    read_only_fields = ('id', 'groups')
    fields = ( 
      'created_on', 
      'updated_on', 
      'employee_id',
      'branch',
      'first_name',
      'last_name',
      'username',
      'email'
    )