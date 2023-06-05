#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''WorldBuilder - Define all the components of the world to be optimized'''


#imports
from collections import Counter

#   script imports
from bill_of_materials import BillOfMaterials
from factory import Factory
from barn import Storage
#imports


# classes
class WorldBuilder:
  '''WorldBuilder - Define all the components of the world to be optimized'''

  def __init__(self):
    self.barn = Storage(max_capacity=50)

    # self.fields = Fields(field_count=6)

    # Factories
    self.bakery = Factory(
      name='bakery',
      num_prod_boxes=3,
      goods_list=self.boms_materials_for_bakery()
    )

  def boms_crops_for_fields(self):
    return {
      'wheat':             BillOfMaterials(out_prod_name='wheat', time_req=2, coin_req=0, sell_at_barn=1),
      'corn':              BillOfMaterials(out_prod_name='corn', time_req=5, coin_req=1, sell_at_barn=3),
      # 'carrot':            BillOfMaterials(out_prod_name='carrot', time_req=10, coin_req=2, sell_at_barn=5),
      # 'sugarcane':         BillOfMaterials(out_prod_name='sugarcane', time_req=20, coin_req=3, sell_at_barn=7),
      # 'cotton':            BillOfMaterials(out_prod_name='cotton', time_req=30, coin_req=4, sell_at_barn=9),
      # 'strawberry':        BillOfMaterials(out_prod_name='strawberry', time_req=60, coin_req=5, sell_at_barn=11),
      # 'tomato':            BillOfMaterials(out_prod_name='tomato', time_req=120, coin_req=6, sell_at_barn=13),
      # 'pine_tree':         BillOfMaterials(out_prod_name='pine_tree', time_req=180, coin_req=7, sell_at_barn=15),
      # 'potato':            BillOfMaterials(out_prod_name='potato', time_req=240, coin_req=8, sell_at_barn=17),
      # 'cacao':             BillOfMaterials(out_prod_name='cacao', time_req=480, coin_req=9, sell_at_barn=19),
      # 'rubber_tree':       BillOfMaterials(out_prod_name='rubber_tree', time_req=720, coin_req=15, sell_at_barn=29),
      # 'silk':              BillOfMaterials(out_prod_name='silk', time_req=900, coin_req=20, sell_at_barn=33),
      # 'pepper':            BillOfMaterials(out_prod_name='pepper', time_req=300, coin_req=11, sell_at_barn=20),
      # 'mint':              BillOfMaterials(out_prod_name='mint', time_req=165, coin_req=21, sell_at_barn=30),
      # 'rice':              BillOfMaterials(out_prod_name='rice', time_req=80, coin_req=7, sell_at_barn=14),
      # 'rose':              BillOfMaterials(out_prod_name='rose', time_req=150, coin_req=18, sell_at_barn=28),
      # 'jasmine':           BillOfMaterials(out_prod_name='jasmine', time_req=210, coin_req=25, sell_at_barn=37),
      # 'coffee_plant':      BillOfMaterials(out_prod_name='coffee_plant', time_req=360, coin_req=33, sell_at_barn=48),
      # 'peanut_plant':      BillOfMaterials(out_prod_name='peanut_plant', time_req=420, coin_req=35, sell_at_barn=53),
      # 'apple':             BillOfMaterials(out_prod_name='apple', time_req=450, coin_req=36, sell_at_barn=55),
      # 'tea_plant':         BillOfMaterials(out_prod_name='tea_plant', time_req=540, coin_req=37, sell_at_barn=61),
      # 'soybean':           BillOfMaterials(out_prod_name='soybean', time_req=120, coin_req=8, sell_at_barn=15),
    }


  def boms_materials_for_bakery(self):
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
