from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class GeoLocation(models.Model):
	when = models.DateTimeField('date created')
	lat = models.DecimalField('Latitude', max_digits=8, decimal_places=3)
	lng = models.DecimalField('Longitude', max_digits=8, decimal_places=3)