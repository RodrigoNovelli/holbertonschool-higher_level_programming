#!/usr/bin/python3
from abc import ABC, abstractmethod

# Step 2: Create an abstract class Payment
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Step 3: Implement subclasses
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount:.2f}.")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount:.2f}.")

# Step 4: Demonstrate polymorphism
def process_payments(payment_method, amount):
    payment_method.process_payment(amount)

# Create instances of the payment methods
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

# Process payments
process_payments(credit_card_payment, 100.00)
process_payments(paypal_payment, 75.50)