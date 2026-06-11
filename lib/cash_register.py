#!/usr/bin/env python3

class CashRegister:
    """A simple cash register model for adding items, applying discounts, and voiding transactions."""

    def __init__(self, discount=0):
        """Initialize a CashRegister.

        Args:
            discount (int, optional): Percentage discount applied to the total. Defaults to 0.
        """
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
        """Validate and set the discount percentage.

        The discount must be an integer between 0 and 100 inclusive.
        If the value is invalid, print an error message and keep the existing discount.
        """
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
        """Add an item to the register.

        This updates the running total, adds every item name to the items list,
        and stores the transaction details for later operations.
        """
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
        """Apply the current discount to the register total.

        If a discount exists and there is at least one prior transaction, the total
        is reduced and the last transaction is removed from history and items.
        Otherwise, print a message that no discount can be applied.
        """
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
        """Remove the most recent transaction and adjust the total and items."""
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
