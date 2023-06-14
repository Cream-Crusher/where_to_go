import requests

from ...models import Place, Image
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Load location from json link'

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='?', type=str)

    def handle(self, *args, **options):
        response_place = requests.get(options['poll_ids'])

        raw_place = response_place.json()
        place_coordinates = raw_place['coordinates']

        place, created = Place.objects.get_or_create(
            title=raw_place['title'],
            description_short=raw_place['description_short'],
            description_long=raw_place['description_long'],
            low=place_coordinates['lng'],
            lat=place_coordinates['lat'],
        )

        if not created:

            for image in raw_place['imgs']:
                image, created = Image.objects.get_or_create(
                    post=place,
                    img=image
                )
                img_link = ContentFile(requests.get(image).content)
                img_name = str(image).split('/')[-1]

                image.img.save(img_name, img_link, save=True)
