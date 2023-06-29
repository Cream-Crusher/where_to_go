from django.shortcuts import render, get_object_or_404
from .models import Place
from django.http import JsonResponse
from django.urls import reverse


def show_page(request):
    places = Place.objects.all()
    processed_places = []

    for place in places:
        processed_places.append({
            'coordinates': [place.lon, place.lat],
            'title': place.title,
            'placeId': place.id,
            'detailsUrl': reverse('get_place_detail', args=[place.id, ]),
        })

    return render(request, 'index.html', context={'places': processed_places})


def get_place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    urls = [url.img.url for url in place.images.all()]

    return JsonResponse(
        {
            'title': place.title,
            'imgs': urls,
            'description_short': place.description_short,
            'description_long': place.description_long,
            'coordinates': {
                'lng':  place.lon,
                'lat': place.lat
            }
        },
        json_dumps_params={
            'indent': 4,
            'ensure_ascii': False
        }
    )
