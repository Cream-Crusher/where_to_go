from django.shortcuts import render
from .models import Place


def show_page(request):  # TODO возможно добавить оптимидзацию
    places = Place.objects.all()

    for place in places:
        requested_place = {
            'title': place.title,
            'description_short': place.description_short,
            'description_long': place.description_long,
            'low': place.low,
            'lat': place.lat,
            'img': [request.build_absolute_uri('/media/{}'.format(image)) for image in place.images.all()],
            }

        print(requested_place['img'])
    return render(request, 'index.html', context={})
