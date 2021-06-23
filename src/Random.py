import random

class Random:
  def getInteger(min, max):
    return random.randint(min, max)
  def chooseItem(lst):
    return lst[Random.getInteger(0, len(lst)-1)]