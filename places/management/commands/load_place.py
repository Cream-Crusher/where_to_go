import requests
import logging

from ...models import Place, Image
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


def get_created_place(raw_place):
    place_coordinates = raw_place['coordinates']
    img_name = raw_place['title']
    description_short = raw_place.get('description_short', '')
    description_long = raw_place.get('description_long', '')
    return Place.objects.get_or_create(
        title=img_name,
        lon=place_coordinates['lng'],
        lat=place_coordinates['lat'],
        defaults={
            'description_short': description_short,
            'description_long': description_long,
        }
    )


def add_img_to_place(place, response):
    img_name = place.title
    img_content = ContentFile(response.content, img_name)
    Image.objects.create(
        post=place,
        img=img_content
    )


class Command(BaseCommand):
    help = 'Load location from json link'

    def add_arguments(self, parser):
        parser.add_argument('link_json_file', nargs='?', type=str)

    def handle(self, *args, **options):
        try:
            response_place = requests.get(options['link_json_file'])
            raw_place = response_place.json()
            place, created = get_created_place(raw_place)

            if not created:
                return

            for image in raw_place['imgs']:
                response = requests.get(image)
                add_img_to_place(place, response)

        except Exception as err:
            logger.warning(err)
