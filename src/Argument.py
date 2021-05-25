import random

class Variable:
  __count = 0

  def __init__(self, type, name = "var"):
    self.count = Variable.__count
    Variable.__count += 1
    self.type = type
    self.ori_name = name
    self.name = "{}{}".format(name, self.count)

  def getDef(self):
    return "{} {}".format(str(self.type), str(self.name))

  def getRef(self):
    return str(self.name)

  def __str__(self):
    return "{}_{}".format(str(self.type), str(self.name))
  
  def clear_count():
    Variable.__count = 0

class Integer:
  def __init__(self, val):
    self.val = val

  def __str__(self):
    return self.getValueStr()

  def getValueStr(self):
    return str(self.val)

class RandomInteger:
  def __init__(self, min, max):
    self.min = min
    self.max = max

  def __str__(self):
    return "rand_int_{}_{}".format(str(self.min), str(self.max))

  def getValueStr(self):
    return str(random.randint(self.min, self.max))

class Buffer:
  GLOBAL_RBUF = None
  GLOBAL_WBUF = None
  def __init__(self, size):
    self.size = size

  def __str__(self):
    if self.size == -1:
      return "global_rbuf"
    elif self.size == -2:
      return "global_wbuf"
    else:
      return "buf_{}".format(self.size)

  def getValueStr(self):
    if self.size == -1:
      return "global_rbuf"
    elif self.size == -2:
      return "global_wbuf"
    else:
      return "WRONG"

Buffer.GLOBAL_RBUF = Buffer(-1)
Buffer.GLOBAL_WBUF = Buffer(-2)