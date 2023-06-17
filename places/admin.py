from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableStackedInline, SortableAdminBase

from places.models import Place, Image


def preview(image):
    image_url = image.img.url
    height = 200

    return format_html(f'<img src="{image_url}" height={height} />')


class ImageStackedInline(SortableStackedInline):
    model = Image
    raw_id_fields = ['post', ]
    readonly_fields = [preview, ]


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ['title', ]
    inlines = [ImageStackedInline]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = [preview, ]
    list_display = ['post', 'img', ]
    raw_id_fields = ['post', ]
    fields = ['img', 'post', preview, ]
