#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
1. Defining a cells as a individual space on the map.
2. Defining agent class for RL agent later
'''


#imports
from abc import ABC
#   script imports
#imports


# classes
class Cell(ABC):
  '''Defining a cells as a individual space on the map.'''

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return f'{self.__class__.__name__} ({self.x}, {self.y})'


class Agent(ABC):
  '''Defining agent class for RL agent later'''

  def act(self, control):
    pass
# classes
