class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item: str, price: int):
        self.items.append((item, price))
        print(f"Added {item} for ${price:.2f}")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item, price in self.items:
                print(f"- {item}: ${price:.2f}")

    def total(self):
        total_price = sum(price for _, price in self.items)
        print(f"Total: ${total_price:.2f}")
        return total_price

# Setting up shopping carts.
mario_cart = ShoppingCart()
bob_cart = ShoppingCart()

print("\nMario:")
mario_cart.add_item("mushroom", 7.40)
mario_cart.add_item("star", 6.40)

print("\nBob:")
bob_cart.add_item("wheel", 3.90)
bob_cart.add_item("frame", 6.20)
bob_cart.add_item("hype", 11.90)

print("\nMario's cart:")
mario_cart.view_cart()
mario_cart.total()

print("\nBob's cart:")
bob_cart.view_cart()
bob_cart.total()
