from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableStackedInline, SortableAdminBase

from places.models import Place, Image


class ImageStackedInline(SortableStackedInline):
    model = Image
    raw_id_fields = ['post', ]
    readonly_fields = ['preview', ]

    def preview(self, image):
        return format_html('<img src="{}" width="{}" height={} />', image.img.url, 200, 200,)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ['title', ]
    inlines = [ImageStackedInline]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ['preview', ]
    list_display = ['post', 'img', ]
    raw_id_fields = ['post', ]
    fields = ['img', 'post', 'preview', ]

    def preview(self, image):
        return format_html('<img src="{}" width="{}" height={} />', image.img.url, 200, 200,)
