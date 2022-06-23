class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flight):
        self.price = flight["price"]
        self.d_city_name = flight["cityFrom"]
        self.d_iata_code = flight["flyFrom"]
        self.a_city_name = flight["cityTo"]
        self.a_iata_code = flight["flyTo"]
        self.outbound_date = flight["route"][0]["local_departure"].split("T")[0]
        self.inbound_date = flight["route"][1]["local_arrival"].split("T")[0]
