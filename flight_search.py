class FlightSearch:
    def __init__(self):
        self.iataCodes = {'Paris': 'CDG', 'Berlin': 'BER', 'Tokyo': 'TYO', 'Sydney': 'SYD', 'Istanbul': 'IST',
                     'Kuala Lumpur': 'KUL', 'New York': 'JFK', 'San Francisco': 'SFO', 'Cape Town': 'CTW'}

    def replace_iata(self, city_name):
        if city_name in self.iataCodes.keys():
            new_iata = self.iataCodes[city_name]
            return new_iata

