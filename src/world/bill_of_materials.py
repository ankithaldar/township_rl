#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Bill of materials'''

# imports
from dataclasses import dataclass
from collections import Counter
# imports


@dataclass
class BillOfMaterials:
  '''Bill of materials'''

  linked_to_factory: object
  barn_storage: object

  output_product_name: str
  inputs: Counter
  price: int = 0
  output_lot_size: int = 1

  def check_inputs_availability(self):

    for each_input_item in self.inputs.keys():
      # check in barn_storage
      # if barn_storage.storage[each_input_item] >= self.inputs[each_input_item]:
        # return True

      # check in factory
      # if linked_to_factory.name == 'Farm':
        # pass
      pass
