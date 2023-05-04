import requests

from ...models import Place, Image
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Load location from json link'

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=str)

    def handle(self, *args, **options):
        requests_place = requests.get(options['poll_ids'][0])
        place = requests_place.json()
        place_coordinates = place['coordinates']

        place_mame, created = Place.objects.get_or_create(
            title=place['title'],
            description_short=place['description_short'],
            description_long=place['description_long'],
            low=place_coordinates['lng'],
            lat=place_coordinates['lat'],
        )

        image, created = Image.objects.get_or_create(
            post=place_mame
        )
        img = place['imgs'][0]
        img_link = ContentFile(img)
        img_name = img.split('/')[-1]

        image.img.save(img_name, img_link, save=True)
