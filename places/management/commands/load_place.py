from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load location from json file'

    def handle(self, *args, **options):
        if options['exclude_media']:
            print('1')
        else:
            print('2')

    def add_arguments(self, parser):
        parser.add_argument(
            '-e_m',
            '--exclude_media',
            action='store_true',
            default=False,
            help='Убрать медиа файлы'
        )
