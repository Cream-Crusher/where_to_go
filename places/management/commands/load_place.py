import requests
import logging

from ...models import Place, Image
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


class Command(BaseCommand):
    help = 'Load location from json link'

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='?', type=str)

    def handle(self, *args, **options):
        try:
            response_place = requests.get(options['poll_ids'])
            response_status = response_place.raise_for_status
            raw_place = response_place.json()
            place_coordinates = raw_place['coordinates']

            place, created = Place.objects.get_or_create(  # TODO заменить none, на пустой списко []
                title=raw_place['title'],
                lon=place_coordinates['lng'],
                lat=place_coordinates['lat'],
                defaults={
                    'description_short': raw_place['description_short'],
                    'description_long': raw_place['description_long'],
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

        except requests.exceptions.MissingSchema:
            logger.info('load_place не получил обязательный параметр.', response_status)

        except requests.exceptions.JSONDecodeError:
            logger.info('Данной ссылки не существует:', response_status)

        except Exception as err:
            logger.warning(err, response_status)
