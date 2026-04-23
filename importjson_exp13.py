import json
import csv

with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

with open('data1.csv', 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("JSON data successfully converted to CSV.")
