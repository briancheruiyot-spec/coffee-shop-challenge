from order import Order
from coffee import Coffee

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