import requests
import os
import sys
import django
from django.db import DatabaseError
from .models import Cinema

proj = os.path.dirname(os.path.abspath(__file__))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'locallibrary.settings'
django.setup()

#from locallibrary.api.models import Cinema


url = "https://opendata.mkrf.ru/v2/cinema/86?l=150"
headers = {"X-API-KEY": "bd642ee6d25320d7e24f87bd51e345cfcad7f7532de0197452fcdc19c1351e1d"}

response = requests.get(url, headers=headers).json()


def parse_and_adding():
    def data_checking() -> bool:
        if 'contacts' in data['data']['general'] \
                and 'email' in data['data']['general']['contacts'] \
                and data['data']['general']['contacts']['email'] != '' \
                and 'phones' in data['data']['general']['contacts'] \
                and data['data']['general']['contacts']['phones']:
            return True
        return False

    for data in response['data']:
        if data_checking():
            name = data['data']['general']['name']
            full_address = data['data']['general']['address']['fullAddress']
            email = data['data']['general']['contacts']['email']
            phone = data['data']['general']['contacts']['phones'][0]['value']
            try:
                Cinema.objects.create(name=name, full_address=full_address, email=email, phone=phone)
            except DatabaseError:
                pass
