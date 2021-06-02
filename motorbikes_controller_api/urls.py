from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

admin.site.site_header = 'Motorbikes Controller'
admin.site.index_title = 'Features area'
admin.site.site_title = 'Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
