from django.shortcuts import render, get_object_or_404
from .models import Place
from django.http import JsonResponse
from django.urls import reverse


def show_page(request):
    places_queries = Place.objects.all().loading_db_queries()
    places = []

    for place_queries in places_queries:
        places.append({
            'coordinates': [place_queries.low, place_queries.lat],
            'title': place_queries.title,
            'placeId': place_queries.title,
            "detailsUrl": reverse('place_detail', args=[place_queries.id, ]),
        })

    data = {'places': (places[0], places[1])}

    return render(request, 'index.html', context=data)


def place_detail(request, tag_title):
    place = get_object_or_404(Place, id=tag_title)
    absolute_url = [url.get_absolute_image_url() for url in place.images.all()]

    return JsonResponse({
        'title': place.title,
        'imgs': absolute_url,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng':  place.low,
            'lat': place.lat
        }
        }, json_dumps_params={'indent': 4, 'ensure_ascii': False})
