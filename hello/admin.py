from django.contrib import admin

from .models import GeoLocation

@admin.register(GeoLocation)
class AuthorAdmin(admin.ModelAdmin):
    pass