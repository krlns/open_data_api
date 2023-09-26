import requests
from django.db import DatabaseError, connection
from .models import Cinema


url = "https://opendata.mkrf.ru/v2/cinema/86?l=150"
headers = {"X-API-KEY": "bd642ee6d25320d7e24f87bd51e345cfcad7f7532de0197452fcdc19c1351e1d"}


def check_table_exits():
    table_names = connection.introspection.table_names()
    if "api_cinema" in table_names and len(Cinema.objects.values()) == 0:
        parse_and_adding()


def parse_and_adding():
    response = requests.get(url, headers=headers).json()

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
