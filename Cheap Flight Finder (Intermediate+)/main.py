from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_sheet_data()

# Find IATA codes from City names if they do not exist
for city in sheet_data:
    if city["iataCode"] == "":
        city["iataCode"] = flight_search.get_iata_code(city["city"])
        data_manager.update_sheet_data(city["id"], city)

result_list = []
print("Finding Deals...")
for city in sheet_data:
    current_city_cheapest = flight_search.search_flights(city)
    if current_city_cheapest == "No Results Found":
        result_list.append("No Results Found")
    else:
        flight_data = FlightData(current_city_cheapest)
        result_list.append(flight_data)

email_list = data_manager.get_emails()
notification_manager = NotificationManager(result_list, email_list)
alert_sent = notification_manager.construct_and_send()
