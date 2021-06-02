from django.urls import path, include
from rest_framework import routers
from api.views import *
from rest_framework_simplejwt.views import TokenRefreshView

router = routers.DefaultRouter()
# router.register("user",UserViewset)

urlpatterns = [
    path("", include(router.urls)),
    path('login/', TokenPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]
