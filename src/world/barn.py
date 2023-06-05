#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''BarnStorage'''


#imports
from collections import Counter
from dataclasses import dataclass
#   script imports
#imports


# classes
@dataclass
class Storage:
  '''BarnStorage'''

  max_capacity: int

  def __postinit__(self):
    self.stock_levels = Counter()


  def used_capacity(self):
    return sum(self.stock_levels.values())


  def available_capacity(self):
    return self.max_capacity - self.used_capacity()


  def possible_to_add_stock_units(self):
    pass


# classes


# functions
def function_name():
  pass
# functions


# main
def main():
  pass


# if main script
if __name__ == '__main__':
  main()
