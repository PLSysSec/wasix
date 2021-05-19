
import random

class Block:
  def __init__(self, syscall, *args):
    self.syscall = syscall 
    self.args = args
    self.fd = args[0] if len(args) > 0 else None

  def getID(self):
    args_str = ""
    for arg in self.args:
      args_str += "::" + str(arg)
    return self.syscall + args_str


class BlockPool:
  def __init__(self):
    self.pool = dict()

  def getRandomBlock(self):
    block = random.choice(list(self.pool.values()))
    return block

  def addBlocks(self, blocks):
    for b in blocks:
      self.pool[b.getID()] = b

  def popBlocks(self, pop_fun):
    pop_fun(self.pool)