from django.urls import path, include
from rest_framework import routers
from api_v2.views import *

router = routers.DefaultRouter()
# router.register("user",UserViewset)

urlpatterns = [
    path("", include(router.urls)),
]
