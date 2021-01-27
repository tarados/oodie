from django.core.management.base import BaseCommand, CommandError
from app.localization import import_locales


class Command(BaseCommand):
    def handle(self, *args, **options):
        import_locales()

        self.stdout.write('Successfully')
