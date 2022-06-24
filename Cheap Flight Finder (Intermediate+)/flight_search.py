import requests
from datetime import datetime, timedelta
import os

FLY_FROM = "LON"  # IATA code of departure city
TIME_DELTA = 6  # in months
MIN_STAY_DUR = 7  # in days
MAX_STAY_DUR = 28  # in days
MAX_STOPOVERS = 2  # 0 means direct


def find_cheapest(search_results):
    cheapest = search_results[0]

    for flight in search_results:
        if cheapest["price"] > flight["price"]:
            cheapest = flight
        else:
            if cheapest["price"] == flight["price"]:
                if cheapest["nightsInDest"] < flight["nightsInDest"]:
                    cheapest = flight

    return cheapest


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.API_ENDPOINT = os.environ.get("TEQUILA_ENDPOINT")
        self.API_KEY = os.environ.get("TEQUILA_API_KEY")
        self.headers = {"apikey": self.API_KEY}

    def get_iata_code(self, city_name):
        locations_endpoint = self.API_ENDPOINT + "/locations/query"

        search_params = {
            "term": city_name,
        }

        response = requests.get(locations_endpoint, params=search_params, headers=self.headers)
        iata_code = response.json()["locations"][0]["code"]
        return iata_code

    def search_flights(self, city):
        search_endpoint = self.API_ENDPOINT + "/v2/search"

        date_tomorrow = datetime.today() + timedelta(days=1)
        date_from = date_tomorrow.strftime("%d/%m/%Y")

        date_delta = date_tomorrow + timedelta(days=30 * TIME_DELTA)
        date_to = date_delta.strftime("%d/%m/%Y")

        search_params = {
            "fly_from": FLY_FROM,
            "fly_to": city["iataCode"],
            "date_from": date_from,
            "date_to": date_to,
            "curr": "GBP",
            "price_to": city["lowestPrice"],
            "nights_in_dst_from": MIN_STAY_DUR,
            "nights_in_dst_to": MAX_STAY_DUR,
            "flight_type": "round",
            "max_stopovers": MAX_STOPOVERS,
        }

        response = requests.get(search_endpoint, params=search_params, headers=self.headers)
        if len(response.json()["data"]) > 0:
            return find_cheapest(response.json()["data"])
        else:
            return "No Results Found"


