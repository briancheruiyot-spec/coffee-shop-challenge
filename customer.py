class Customer:
  def __init__(self, name):
    self.name = name
    self._order = []

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, value):
    if isinstance(value, str) and 1 <= len(value) <=15:
      self._name = value
    else:
      raise ValueError("Name must be a string 1-15 characters long.")
    
  def orders(self):
    return self._orders
  
  def coffees(self):
    return list(set(order.coffee for order in self._orders))
  
  def create_order(self, coffee, price):
    from order import Order
    new_order = Order(self, coffee, price)
    self._order.append(new_order)
    return new_order