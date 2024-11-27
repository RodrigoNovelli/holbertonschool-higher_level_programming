#!/usr/bin/python3
class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        self.__balance = value
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: ${amount}")
    
    def withdraw(self, amount):
        self.__balance -= amount
        print(f"Withdrew: ${amount}")
    
    def get_balance(self):
        print(self.__balance)

account = BankAccount(100)  # Create an account with an initial balance of $100

# Perform operations
print("Initial Balance:", account.get_balance())
account.deposit(50)
print("Balance after deposit:", account.get_balance())
account.withdraw(30)
print("Balance after withdrawal:", account.get_balance())
account.withdraw(200)  # Attempt to withdraw more than the balance