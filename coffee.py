from customer import Customer
from order import Order

class Coffee:
  def __init__(self, name):
    if isinstance(name, str) and len(name) >= 3:
      self._name = name
    else:
      raise ValueError("Coffee name must be a string of at least 3 characters")
    self._order = []

    @property
    def name(self):
      return self._name