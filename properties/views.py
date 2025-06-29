from django.shortcuts import render
from django.http import JsonResponse
from .models import Property

def globe_view(request):
    return render(request, 'globe.html')

def properties_geojson(request):
    data = list(Property.objects.values('title', 'lat', 'lng', 'city', 'price'))
    return JsonResponse(data, safe=False)