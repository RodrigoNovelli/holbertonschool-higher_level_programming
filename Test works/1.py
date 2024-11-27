#!/usr/bin/python3
class Car:
    def __init__(self, brand= str, model= str, year= int):
        self.brand = brand
        self.model = model
        self.year = year
    
    def diplay_info(self):
        print(self.brand, self.model, self.year)

my_car = Car(brand= "Toyota", model= "XT100", year= "2022")
my_car.diplay_info()
