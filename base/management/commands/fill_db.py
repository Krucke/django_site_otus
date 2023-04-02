from django.core.management import BaseCommand

# from faker import Faker

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('test command')