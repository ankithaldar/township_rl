#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Module to control the Game Economy'''


#imports
#   script imports
#imports


# classes
class GameEconomy:
  '''Module to control the Game Economy'''

  def __init__(self):
    super(GameEconomy, self).__init__()

    self.coins = 0
    self.cash = 0

  def update_coins(self, used_coins=0, gained_coins=0):
    '''update coins to the economy as game progresses'''

    self.coins += gained_coins - used_coins


  def update_cash(self, used_cash=0, gained_cash=0):
    '''update cash to the economy as game progresses'''

    self.cash += gained_cash - used_cash

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
