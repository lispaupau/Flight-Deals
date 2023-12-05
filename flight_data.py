import requests
import datetime


class FlightData:
    def __init__(self):
        self.api_key = 'YOUR API KEY'
        self.fly_from = 'KIV'
        self.search_endpoint = 'https://api.tequila.kiwi.com/v2/search'
        self.general_date_from = datetime.datetime.now()
        self.general_date_to = datetime.datetime.now() + datetime.timedelta(days=180)
        self.date_from = f'{self.general_date_from.day}/{self.general_date_from.month}/{self.general_date_from.year}'
        self.date_to = f'{self.general_date_to.day}/{self.general_date_to.month}/{self.general_date_to.year}'

    def search_data(self, sheet_data):
        headers = {'apikey': self.api_key}
        for i in range(len(sheet_data)):
            query = {
                'fly_from': self.fly_from,
                'fly_to': sheet_data[i]['iataCode'],
                'date_from': self.date_from,
                'date_to': self.date_to,
                'return_from': self.date_from,
                'return_to': self.date_to,
                'curr': 'GBP',
                'adults': 2,
                'price_to': sheet_data[i]['lowestPrice']
            }
            response = requests.get(url=self.search_endpoint, params=query, headers=headers)
            print(response.json())
