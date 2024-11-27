#!/usr/bin/python3
import csv

# Step 1: Create a CSV file and write data to it
header = ['Name', 'Age', 'City']
data = [{
    'Name': 'Alice',
    'Age': 30,
    'City': 'New York'
    },
    {
    'Name': 'Miram',
    'Age': 30,
    'City': 'Chicago'
    },
    {
    'Name': 'Jorge',
    'Age': 25,
    'City': 'Cansas'
    }]

# Writing data to the CSV file
with open('data.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames = header)
    writer.writeheader()  # Write the header row
    writer.writerows(data)  # Write the data rows

# Step 2: Read the CSV file and print its contents in a formatted table

with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        print(row)