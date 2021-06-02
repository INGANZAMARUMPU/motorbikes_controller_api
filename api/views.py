from rest_framework import viewsets, generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission, AllowAny
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from django_filters import rest_framework as filters

from .serializers import *

class PersonneFilter(filters.FilterSet):
	class Meta:
		model = Personne
		fields = {
			"nom":['contains'],
			"prenom":['contains'],
			"profession":['contains'],
			"province":['contains'],
			"commune":['contains'],
			"lieu_naissance":['contains'],
			"date_naissance":['exact'],
			"cni":['contains'],
			"numero_permis":['exact'],
			"residence":['contains'],
			"autres":['contains'],
		}

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
SAFE_EDIT_METHODS = ['PUT', 'PACTH', 'POST']

class IsAdminOrReadOnly(BasePermission):
	def has_permission(self, request, view):
		if(not request.user):
			return False
		if(request.user.is_superuser):
			return True
		if(request.method in SAFE_METHODS):
			return True

class IsAdminOrCreateUpdateOnly(BasePermission):
    def has_permission(self, request, view):
        if(request.user.is_superuser):
            return True
        elif(request.method in SAFE_METHODS+SAFE_EDIT_METHODS and request.user):
            return True
        return False

class TokenPairView(TokenObtainPairView):
	serializer_class = TokenPairSerializer

class PersonneViewset(viewsets.ModelViewSet):
	authentication_classes = (SessionAuthentication, JWTAuthentication)
	permission_classes = [IsAdminOrReadOnly, ]
	queryset = Personne.objects.all()
	serializer_class = PersonneSerializer
	filter_class = PersonneFilter