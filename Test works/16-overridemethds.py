#!/usr/bin/python3
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: ${self.salary:.2f}")

# Step 1: Create a subclass Manager that overrides get_details
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)  # Call the constructor of the parent class
        self.team_size = team_size

    def get_details(self):
        # Call the parent class method to get the common details
        super().get_details()
        print(f"Team Size: {self.team_size}")

# Step 2: Create instances of Employee and Manager
employee = Employee("Alice", 50000)
manager = Manager("Bob", 80000, 10)

# Step 3: Get details of both employee and manager
print("Employee Details:")
employee.get_details()
print("\nManager Details:")
manager.get_details()
