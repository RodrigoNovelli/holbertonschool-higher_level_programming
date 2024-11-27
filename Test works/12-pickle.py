#!/usr/bin/python3
import pickle

# Step 1: Create a custom Python class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

# Instantiate an object of the class
person = Person("Alice", 30)

# Step 2: Serialize the object using pickle and save it to a file
with open('person.pkl', 'wb') as file:
    pickle.dump(person, file)

# Step 3: Deserialize the object from the file and verify its properties
with open('person.pkl', 'rb') as file:
    loaded_person = pickle.load(file)

# Verify the properties of the deserialized object
print(loaded_person)  # Output: Person(name=Alice, age=30)
print(loaded_person.name)  # Output: Alice
print(loaded_person.age)   # Output: 30
