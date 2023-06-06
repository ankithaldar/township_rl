#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Realtime clock for monitoring'''


#imports
import math
#   script imports
#imports


# classes
class Clock:
  '''Realtime clock for monitoring'''

  def __init__(self):
    self.__time = 0


  def clock_tick(self):
    # adding 1 min in every cycle
    self.__time += 1


  @property
  def time(self):
    return self.__time


  def current_time(self):
    time = self.time

    days = math.floor(time / (60 * 24))
    time -= days * 60 * 24

    hours = math.floor(time / 60)
    time -= hours * 60

    return f'{days} days - {hours} hours - {time} minutes'

# classes
