import requests

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load location from json link'

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=str)

    def handle(self, *args, **options):

        r = requests.get('https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json')
        place = r.json()
