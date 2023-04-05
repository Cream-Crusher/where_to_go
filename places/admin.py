from django.contrib import admin
from places.models import Place, PlaceEntity 

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass

@admin.register(PlaceEntity)
class PlaceEntityAdmin(admin.ModelAdmin):
    raw_id_fields = ['place', ]
    pass
