# coffee-shop-challenge

A Python project modeling a coffee shop's order system with customers, coffees, and orders.

## Project Structure

coffee-shop-challenge/
├── coffee.py 
├── customer.py 
├── order.py 
├── debug.py 
├── Pipfile
├── Pipfile.lock
└── README.md


## Classes Overview

### Coffee Class (`coffee.py`)
- Represents a coffee type with a name
- Validates name (must be string ≥3 characters)
- Tracks all orders for this coffee
- Provides:
  - List of customers who ordered this coffee
  - Number of orders
  - Average price of orders

### Customer Class (`customer.py`)
- Represents a customer with a name
- Validates name (must be string 1-15 characters)
- Tracks all orders made by this customer
- Provides:
  - List of unique coffees ordered
  - Ability to create new orders
  - Class method to find biggest spender for a coffee

### Order Class (`order.py`)
- Represents an order linking customer, coffee, and price
- Validates:
  - Customer must be Customer instance
  - Coffee must be Coffee instance
  - Price must be float between 1.0 and 10.0
- Automatically updates customer's and coffee's order lists

## Example Usage

See `debug.py` for demonstration:
 
  from customer import Customer
  from coffee import Coffee

  Create coffees
  
  latte = Coffee("Latte")
  espresso = Coffee("Espresso")

  Create customers
  
  alice = Customer("Alice")
  bob = Customer("Bob")

  Create orders
  
  alice.create_order(latte, 4.5)
  alice.create_order(espresso, 3.0)
  bob.create_order(latte, 5.0)

  Get order statistics
  
  print(f"Latte orders: {latte.num_orders()}, Average price: {latte.average_price()}")
  print(f"Espresso orders: {espresso.num_orders()}, Average price: {espresso.average_price()}")

  Find biggest spender
  
  biggest_spender = Customer.most_aficionado(latte)
  print(f"Most afficionado for Latte: {biggest_spender.name if biggest_spender else 'None'}")

## Requirements
 
  Python3

  Dependencies listed in Pipfile.lock

## Installation

  - Clone this repository

  - Set up a virtual environment (recommended)

Install dependencies from Pipfile.lock

# Running the Project
  Execute the debug script to see example output:
    python debug.py

## Author
  Brian Cheruiyot
  briancheruiyot6@gmail.com
