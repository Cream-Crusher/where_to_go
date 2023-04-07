from django.shortcuts import render, get_object_or_404
from .models import Place


def show_page(request):
    places_queries = Place.objects.all().loading_db_queries()
    places = []

    for place_queries in places_queries:
        # place = {
        #     'title': place_queries.title,
        #     'imgs': [request.build_absolute_uri('/media/{}'.format(image)) for image in place_queries.images.all()],
        #     'description_short': place_queries.description_short,
        #     'description_long': place_queries.description_long,
        #     'coordinates': {
        #         "lng":  place_queries.low,
        #         "lat": place_queries.lat
        #     }
        #     }

        places.append({
            "coordinates": [place_queries.low, place_queries.lat],
            "title": place_queries.title,
            "placeId": place_queries.title,
        })

    data = {"places": (places[0], places[1])}

    return render(request, 'index.html', context=data)


def json_detail(request, tag_title):
    place = get_object_or_404(Place, id=tag_title)
    print(place)
    return render(request, 'json_place.html', context={'title': place})
