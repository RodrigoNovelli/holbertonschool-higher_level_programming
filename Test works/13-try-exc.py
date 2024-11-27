#!/usr/bin/python3
import json

# Step 1: Define a valid JSON string and a corrupted one
valid_json = '{"name": "Alice", "age": 30}'
corrupted_json = '{"name": "Alice", "age": 30,'  # Missing closing bracket

# Step 2: Function to deserialize JSON and handle exceptions
def deserialize_json(json_string):
    try:
        data = json.loads(json_string)
        return data
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Step 3: Attempt to deserialize both valid and corrupted JSON
print("Attempting to deserialize valid JSON:")
valid_data = deserialize_json(valid_json)
print(valid_data)  # Output: {'name': 'Alice', 'age': 30}

print("\nAttempting to deserialize corrupted JSON:")
corrupted_data = deserialize_json(corrupted_json)
print(corrupted_data)  # Output: None, as the deserialization failed