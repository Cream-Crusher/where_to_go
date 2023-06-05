from django.shortcuts import render, get_object_or_404
from .models import Place
from django.http import JsonResponse
from django.urls import reverse


def show_page(request):
    places = Place.objects.all()
    places_processed = []

    for place in places:
        places_processed.append({
            'coordinates': [place.low, place.lat],
            'title': place.title,
            'placeId': place.id,
            'detailsUrl': reverse('place_detail', args=[place.id, ]),
        })

    dataset = {'places': ([(place) for place in places_processed])}

    return render(request, 'index.html', context=dataset)


def place_detail(request, tag_title):
    place = get_object_or_404(Place, id=tag_title)
    absolute_urls = [url.get_absolute_image_url() for url in place.images.all()]

    return JsonResponse({
        'title': place.title,
        'imgs': absolute_urls,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng':  place.low,
            'lat': place.lat
        }
        }, json_dumps_params={'indent': 4, 'ensure_ascii': False})
