from customer import Customer
from coffee import Coffee

# Create some coffee instances
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create some customer instances
alice = Customer("Alice")
bob = Customer("Bob")

# Create some orders
alice.create_order(latte, 4.5)
alice.create_order(espresso, 3.0)
bob.create_order(latte, 5.0)

# Output some results
print(f"Alice's orders: {[order.price for order in alice.orders()]}")
print(f"Bob's orders: {[order.price for order in bob.orders()]}")
print(f"Latte orders: {latte.num_orders()}, Average price: {latte.average_price()}")
print(f"Espresso orders: {espresso.num_orders()}, Average price: {espresso.average_price()}")

# Get the most afficionado customer for Latte
most_spent_customer = Customer.most_aficionado(latte)
print(f"Most afficionado for Latte: {most_spent_customer.name if most_spent_customer else 'None'}")
