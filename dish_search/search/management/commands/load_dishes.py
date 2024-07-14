import csv
import requests
from django.core.management.base import BaseCommand
from search.models import Dish

class Command(BaseCommand):
    help = 'Load dishes from a CSV file'

    def handle(self, *args, **kwargs):
        url = 'https://python-exercise.s3.ap-south-1.amazonaws.com/restaurants_small.csv'
        response = requests.get(url)
        content = response.content.decode('utf-8')
        reader = csv.reader(content.splitlines())
        next(reader)  # Skip header row

        for row in reader:
            name = row[0]
            Dish.objects.create(name=name)

        self.stdout.write(self.style.SUCCESS('Successfully loaded dishes'))
