import requests

class CountryInfo:
    def __init__(self, url):
        self.url = url
        self.data = self.fetch_data()

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data")
            return None

    def display_country_info(self):
        if self.data:
            print("Countries and their currencies:")
            for country_info in self.data:
                country_name = country_info.get('name', {}).get('common', 'N/A')
                currencies = country_info.get('currencies', [])
                if currencies:
                    for currency_code, currency_info in currencies.items():
                        currency_name = currency_info.get('name', 'N/A')
                        currency_symbol = currency_info.get('symbol', 'N/A')
                        print(f"Country: {country_name}, Currency: {currency_name}, Symbol: {currency_symbol}")

    def display_dollar_countries(self):
        if self.data:
            print("Countries with DOLLAR as currency:")
            for country_info in self.data:
                currencies = country_info.get('currencies', {})
                if 'USD' in currencies:
                    print(country_info.get('name', {}).get('common', 'N/A'))

    def display_euro_countries(self):
        if self.data:
            print("Countries with EURO as currency:")
            for country_info in self.data:
                currencies = country_info.get('currencies', {})
                if 'EUR' in currencies:
                    print(country_info.get('name', {}).get('common', 'N/A'))

# Creating an instance of CountryInfo with the provided URL
url = "https://restcountries.com/v3.1/all"
country_info = CountryInfo(url)

# Fetching all JSON data
country_info.fetch_data()

# Displaying countries, currencies, and symbols
country_info.display_country_info()

# Displaying countries with Dollar as currency
country_info.display_dollar_countries()

# Displaying countries with Euro as currency
country_info.display_euro_countries()
