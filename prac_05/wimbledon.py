"""cp 1404 prac -05
"""
import csv

def read_csv(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip header row
        for row in reader:
            data.append(row)
    return data

# Function to process the CSV data
def process_data(data):
    champions = {}
    countries = set()
    for row in data:
        champion = row[2]
        country = row[1]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
        countries.add(country)
    return champions, sorted(countries)
