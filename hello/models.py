from django.db import models

# Create your models here.
class GeoLocation(models.Model):
	when = models.DateTimeField('date created', auto_now_add=True)
	lat = models.DecimalField('Latitude', max_digits=8, decimal_places=6)
	lng = models.DecimalField('Longitude', max_digits=8, decimal_places=6)