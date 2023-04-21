from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableStackedInline, SortableAdminBase

from places.models import Place, Image


class ImageStackedInline(SortableStackedInline):
    model = Image
    raw_id_fields = ['post', ]


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageStackedInline]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ['preview', ]
    list_display = ['post', 'img', ]
    raw_id_fields = ['post', ]
    fields = ['img', 'post', 'preview', ]

    def preview(self, Image):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=Image.img.url,
            width=200,
            height=200,
            ))
