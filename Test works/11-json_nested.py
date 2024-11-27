#!/usr/bin/python3
import json

# Step 1: Serialize the nested Python object into JSON
nested_data = {
    "employees": [
        {"name": "John", "age": 30},
        {"name": "Emma", "age": 25},
    ],
    "department": "HR"
}

# Serialize and write to file
with open("nested_data.json", "w") as json_file:
    json.dump(nested_data, json_file, indent=4)  # Using indent for better readability

# Step 2: Deserialize the JSON back into the original object
with open("nested_data.json", "r") as json_file:
    loaded_data = json.load(json_file)

# Confirm the deserialized object matches the original
print("Original Object:")
print(nested_data)

print("\nDeserialized Object:")
print(loaded_data)

# Check if both objects are identical
print("\nAre the original and deserialized objects identical?", nested_data == loaded_data)