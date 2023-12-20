import csv
import requests

def read_csv_and_update_data(csv_file, api_endpoint):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        csv_columns = reader.fieldnames
        for row in reader:
            identifier = row[csv_columns[0]]
            data_to_update = {key: row[key] for key in csv_columns[1:]}

            response = requests.get(f"{api_endpoint}/{identifier}")

            if response.status_code == 200:
                update_response = requests.patch(f"{api_endpoint}/{identifier}", json=data_to_update)
                print(f"Updated record with identifier {identifier}")
            elif response.status_code == 404:
                add_response = requests.post(api_endpoint, json={**{'ID': identifier}, **data_to_update})
                print(f"Added record with identifier {identifier}")
            else:
                print(f"Failed to process record with identifier {identifier}")

print("Choose an API endpoint:")
print("1. Universities in Canada")
print("2. Star Wars Planets")

choice = input("Enter your choice (1 or 2): ")

if choice not in ['1', '2']:
    print("Invalid choice. Please enter 1 or 2.")
else:
    if choice == '1':
        api_url = "http://universities.hipolabs.com/search?country=Canada"
        csv_file_path = "universities.csv"
    else:
        api_url = "https://swapi.dev/api/planets/"
        csv_file_path = "star_wars_planets.csv"

    read_csv_and_update_data(csv_file_path, api_url)