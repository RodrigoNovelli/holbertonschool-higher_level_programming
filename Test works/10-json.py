#!/usr/bin/python3
import json

# Step 1: Serialize dictionary into JSON and save it to a file
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Serialize and write to file
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Step 2: Read the JSON file and deserialize it back into a dictionary
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)

print("Deserialized Dictionary:", loaded_data)