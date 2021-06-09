from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name="adminview"),
    path('api/', include('restapi.urls')),
    path('', include('ui.urls')),
]
