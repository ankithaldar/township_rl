#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Factory module'''


#imports
from collections import Counter
from dataclasses import dataclass
from typing import Dict

#   script imports
from bill_of_materials import BillOfMaterials

#imports


# classes
@dataclass
class Factory:
  '''Factory module'''

  name: str
  num_prod_boxes: int
  goods_list: Dict[str, BillOfMaterials]

  def __postinit__(self):
    self.max_num_prod_boxes = 7
    self.max_storage_space: int = 6
    self.is_production = False
    self.current_goods_stored: Counter = Counter()


  def check_req_materials(self):
    pass


  def start_production(self):
    pass


  def end_production(self):
    pass



@dataclass
class MultiFactory(Factory):
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
