from django.contrib import admin
from django.urls import path, include
from properties.views import globe_view, properties_geojson

urlpatterns = [
    path('admin/', admin.site.urls),
    path('globe/', globe_view, name='globe'),
    path('api/properties/', properties_geojson, name='properties_json'),
    path('', include('properties.urls')),
]
