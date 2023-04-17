from django.core.management.utils import get_random_secret_key  
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Get a random secret key to put in your .env file'

    def handle(self, *args, **options):
        return get_random_secret_key()