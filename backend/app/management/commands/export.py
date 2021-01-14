from django.core.management.base import BaseCommand, CommandError
from app.localization import export_locales


class Command(BaseCommand):
    def handle(self, *args, **options):
        export_locales()

        self.stdout.write('Successfully')
