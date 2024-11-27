class Person:
    # Class attribute
    species = "Homo sapiens"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

# Step 1: Create instances of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Step 2: Access and modify the class attribute
print("Initial species:", Person.species)  # Output: Homo sapiens

# Modifying the class attribute
Person.species = "Homo sapiens modified"
print("Modified species:", Person.species)  # Output: Homo sapiens modified

# Accessing the class attribute through instances
print("Species from person1:", person1.species)  # Output: Homo sapiens modified
print("Species from person2:", person2.species)  # Output: Homo sapiens modified

# Step 3: Access and modify instance attributes
print(f"{person1.name} is {person1.age} years old.")  # Output: Alice is 30 years old.

# Modifying instance attributes
person1.age = 31
print(f"After a year, {person1.name} is {person1.age} years old.")  # Output: After a year, Alice is 31 years old.

# Accessing instance attributes
print(f"{person2.name} is {person2.age} years old.")  # Output: Bob is 25 years old.