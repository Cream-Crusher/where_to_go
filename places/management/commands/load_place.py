import requests
import logging

from ...models import Place, Image
from django.core.management.base import BaseCommand

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


def get_response(url):
    response = requests.get(url)
    response.raise_for_status()
    check_for_redirect(response)
    return response


def check_for_redirect(response):
    history = response.history

    if history:
        raise requests.HTTPError(history)


class Command(BaseCommand):
    help = 'Load location from json link'

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='?', type=str)

    def handle(self, *args, **options):
        try:
            response_place = get_response(options['poll_ids'])
            raw_place = response_place.json()
            place_coordinates = raw_place['coordinates']
            description_short = raw_place['description_short']
            description_long = raw_place['description_long']

            place, created = Place.objects.get_or_create(
                title=raw_place['title'],
                lon=place_coordinates['lng'],
                lat=place_coordinates['lat'],
                defaults={
                    'description_short': f'{description_short}',
                    'description_long': f'{description_long}',
                }
            )

            if not created:
                return

            for image in raw_place['imgs']:
                img_name = str(image).split('/')[-1]
                image = Image.objects.create(
                    post=place,
                    img=f'media/{img_name}'
                )

        except Exception as err:
            logger.warning(err)
