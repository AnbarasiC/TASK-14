import requests

# Function to fetch data from the API
def fetch_breweries():
    url = "https://api.openbrewerydb.org/breweries"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return None

# 1: List the names of all breweries present in the states of Alaska, Maine, and New York
def breweries_in_states(breweries_data, states):
    for state in states:
        print(f"\nBreweries in {state}:")
        for brewery in breweries_data:
            if brewery['state'] == state:
                print(brewery['name'])

# 2: Count of breweries in each of the states mentioned above
def count_breweries_in_states(breweries_data, states):
    for state in states:
        count = sum(1 for brewery in breweries_data if brewery['state'] == state)
        print(f"\nNumber of breweries in {state}: {count}")

# 3: Count types of breweries in individual cities of the mentioned states
def count_types_in_cities(breweries_data, states):
    for state in states:
        print(f"\nBrewery types in {state}:")
        state_breweries = [brewery for brewery in breweries_data if brewery['state'] == state]
        cities = set(brewery['city'] for brewery in state_breweries)
        for city in cities:
            brewery_types = set(brewery['brewery_type'] for brewery in state_breweries if brewery['city'] == city)
            print(f"{city}: {len(brewery_types)} types")

# 4: Count and list how many breweries have websites in the states of Alaska, Maine, and New York
def count_breweries_with_websites(breweries_data, states):
    for state in states:
        count = sum(1 for brewery in breweries_data if brewery['state'] == state and brewery['website_url'])
        print(f"\nNumber of breweries with websites in {state}: {count}")

# Fetching data from the API
breweries_data = fetch_breweries()

if breweries_data:
    states_of_interest = ['Alaska', 'Maine', 'New York']

    # 1
    breweries_in_states(breweries_data, states_of_interest)

    # 2
    count_breweries_in_states(breweries_data, states_of_interest)

    # 3
    count_types_in_cities(breweries_data, states_of_interest)

    # 4
    count_breweries_with_websites(breweries_data, states_of_interest)
