from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data = DataManager()
new_data = FlightSearch()
sheet_data = data.get_data()
flight_data = FlightData()

for i in range(len(sheet_data)):
    if sheet_data[i]['iataCode']:
        continue
    else:
        new_iata = new_data.replace_iata(sheet_data[i]['city'])
        sheet_data[i]['iataCode'] = new_iata
        data.put_data(sheet_data)

flight_data.search_data(sheet_data)
