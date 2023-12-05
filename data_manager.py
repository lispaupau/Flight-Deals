import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_get_endpoint = 'YOUR GET ENDPOINT'
        self.sheet_post_endpoint = 'YOUR POST ENDPOINT'
        self.sheet_put_endpoint = 'YOUR PUT ENDPOINT'
        self.headers = {
            'Authorization': 'YOUR TOKEN'
        }

    def post_data(self):
        body = {
            'price': {
                'city': 'Tokyo',
                'iataCode': 'TYO',
                'lowestPrice': 485,
            }
        }
        response = requests.post(url=self.sheet_post_endpoint, json=body, headers=self.headers)
        print(response.json())

    def put_data(self, sheet_data):
        for i in range(len(sheet_data)):
            body = {
                'price': {
                    'iataCode': sheet_data[i]['iataCode']
                }
            }
            response = requests.put(url=f'{self.sheet_put_endpoint}{sheet_data[i]["id"]}', json=body,
                                    headers=self.headers)
            print(response.text)

    def get_data(self):
        response = requests.get(url=self.sheet_get_endpoint)
        return response.json()['prices']
