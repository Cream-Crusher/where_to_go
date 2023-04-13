from django.contrib import admin
from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['post', 'img']
    raw_id_fields = ['post', ]
    list_filter = ['post', ]
    pass
