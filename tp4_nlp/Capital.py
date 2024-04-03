import requests

class Capital:
    def __init__(self):
        self.capitals = {}
        self.populate_capitals()

    def populate_capitals(self):
        url = "https://countriesnow.space/api/v0.1/countries/capital"
        response = requests.get(url)
        if response.status_code == 200:
            countries_data = response.json().get("data", [])
            for country in countries_data:
                self.capitals[country["name"].lower()] = country["capital"]

    def get_country_capital(self, country_name):
        return self.capitals.get(country_name.lower(), None)
