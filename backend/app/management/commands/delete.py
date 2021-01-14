from django.core.management.base import BaseCommand
from app.localization import delete_localization


class Command(BaseCommand):
    def handle(self, *args, **options):
        delete_localization()

        self.stdout.write('Successfully')