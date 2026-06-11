#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Initialize the cash register with optional discount.
        self._discount = 0
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Ensure discount is an integer between 0 and 100 inclusive.
        try:
            discount_value = int(value)
        except (TypeError, ValueError):
            print("Not valid discount")
            return

        if 0 <= discount_value <= 100:
            self._discount = discount_value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        # Add an item to the register, update total, item list, and transaction history.
        item_total = price * quantity
        self.total += item_total

        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity,
        })

    def apply_discount(self):
        # Apply the register discount to the current total.
        if self.discount == 0 or not self.previous_transactions:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100.0)
        self.total -= discount_amount
        self.total = round(self.total, 2)

        last_transaction = self.previous_transactions.pop()
        for _ in range(last_transaction["quantity"]):
            if last_transaction["item"] in self.items:
                self.items.remove(last_transaction["item"])

        print(f"After the discount, the total comes to ${int(self.total) if self.total.is_integer() else self.total}.")

    def void_last_transaction(self):
        # Remove the most recent transaction from the register.
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()
        item_total = last_transaction["price"] * last_transaction["quantity"]
        self.total -= item_total
        self.total = round(self.total, 2)

        for _ in range(last_transaction["quantity"]):
            if last_transaction["item"] in self.items:
                self.items.remove(last_transaction["item"])
