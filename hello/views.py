from django.shortcuts import render
from django.http import HttpResponse
import json

from .models import GeoLocation

# Create your views here.
def index(request):
	locations = GeoLocation.objects.all()

	encoded_locations = json.dumps([
		{ 'lat': float(location.lat), 
			'lng': float(location.lng), 
			'when': location.when.isoformat()
		}
		for location in locations
	])

	return render(request, 'db.html', {'locations': locations, 'encoded_locations': encoded_locations })

def upload(request):
	geolocation = GeoLocation()
	geolocation.lat = request.GET['lat']
	geolocation.lng = request.GET['lng']
	geolocation.save()

	return HttpResponse('Got from you lat={}, lng={}, time={}'.format(
		geolocation.lat,
		geolocation.lng,
		geolocation.when
		)
	)