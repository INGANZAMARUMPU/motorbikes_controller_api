from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import *

class TokenPairSerializer(TokenObtainPairSerializer):
	def validate(self, attrs):
		data = super(TokenPairSerializer, self).validate(attrs)
		data['is_admin'] = self.user.is_superuser
		data['id'] = self.user.id
		data['fullname'] = self.user.first_name+" "+self.user.last_name
		return data