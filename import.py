import requests
import csv
import sys

def fetch_and_write_to_csv(endpoint, filename):
    response = requests.get(endpoint)
    data = response.json()

    if "results" in data:
        data = data["results"]

    if isinstance(data, dict):  # For Star Wars planets API
        data = [data]  # Wrap the dictionary in a list for consistent processing

    keys = data[0].keys() if data else []
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    print("Choose an API endpoint:")
    print("1. Universities in Canada")
    print("2. Star Wars Planets")

    choice = input("Enter your choice (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        sys.exit(1)

    if choice == '1':
        api_url = "http://universities.hipolabs.com/search?country=Canada"
        output_filename = "universities.csv"
    else:
        api_url = "https://swapi.dev/api/planets/"
        output_filename = "star_wars_planets.csv"

    fetch_and_write_to_csv(api_url, output_filename)