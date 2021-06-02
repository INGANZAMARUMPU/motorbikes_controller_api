from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # path('login/', TokenPairView.as_view()),
    # path('refresh/', TokenRefreshView.as_view()),
]
