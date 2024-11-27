#!/usr/bin/python3
class Animal:
    def __init__(self, name= str, specie= str):
        self.name = name
        self.specie = specie
    def make_sound(self):
        print('Generic sound')

class Dog(Animal):
    def __init__(self, name=str, specie=str):
        super().__init__(name, specie)
    
    def make_sound(self):
        print("woof")

generic_animal = Animal(name="Generic Animal", specie="Unknown")
dog = Dog(name="Buddy")

# Call make_sound() for each
print("Animal Sound:")
generic_animal.make_sound()

print("\nDog Sound:")
dog.make_sound()
