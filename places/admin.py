from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin, SortableStackedInline

from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image


class ImageStackedInline(SortableStackedInline):  # TODO чТО ТО С ЭТИМ СДЕЛТАЬ
    model = Image
    raw_id_fields = ("post",)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ['image', ]
    list_display = ['post', 'img', ]
    raw_id_fields = ['post', ]
    list_filter = ['post', ]
    fields = ['img', 'post', 'image', ]
    #inlines = [ImageStackedInline, ]

    def image(self, Image):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=Image.img.url,
            width=150,
            height=150,
            ))
