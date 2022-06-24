class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flight):
        self.price = flight["price"]
        self.hyper_link = flight["deep_link"]
        self.d_city_name = flight["cityFrom"]
        self.d_iata_code = flight["flyFrom"]
        self.a_city_name = flight["cityTo"]
        self.a_iata_code = flight["flyTo"]
        self.outbound_date = flight["route"][0]["local_departure"].split("T")[0]
        self.inbound_date = flight["route"][-1]["local_arrival"].split("T")[0]  # changed 1 to -1
        self.stop_overs = int(len(flight["route"]) / 2 - 1)
        self.via_cities = []
        if self.stop_overs >= 1:
            for i in range(self.stop_overs):
                self.via_cities.append(flight["route"][i]["cityTo"])
