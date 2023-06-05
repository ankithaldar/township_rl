#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Bill of materials'''


#imports
from collections import Counter
from dataclasses import dataclass

#   script imports
#imports


# classes
@dataclass
class BillOfMaterials:
  '''Bill of materials'''

  out_prod_name: str
  time_req: int
  coin_req: int
  sell_at_barn: int
  input: Counter = Counter() # (product_name -> quantity per lot)
  out_lot_size: int = 1
# classes
