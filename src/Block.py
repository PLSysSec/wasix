
import random

class Block:
  def __init__(self, syscall, *args, ret = None):
    self.syscall = syscall 
    self.args = args
    self.ret = ret
    self.fd = args[0] if len(args) > 0 else None

  def copy(old, args = [], ret = None):
    new = Block(old.syscall)
    new.args = old.args if len(args) == 0 else args
    new.ret = old.ret if ret == None else ret
    new.fd = new.args[0] if len(new.args) > 0 else None
    return new

  def getID(self):
    separator = ", "
    args_str = separator.join([str(i) for i in self.args])
    func_str = "{}({}) -> {}"
    return func_str.format(self.syscall, args_str, str(self.ret))


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