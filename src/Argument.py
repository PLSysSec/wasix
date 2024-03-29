from Random import Random
import string

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

class ValueGroup:
  def __init__(self, lst, name = "noname"):
    self.name = name
    self.lst = lst
  def __str__(self):
    return "string_from_{}".format(self.name)
  def getValueStr(self):
    return Random.chooseItem(self.lst)

class RandomString:
  def __init__(self, length):
    self.length = length
  def __str__(self):
    return "rand_str_{}".format(self.length)
  def getValueStr(self):
    letters = list(string.ascii_letters)
    s = ""
    for i in range(self.length):
      s += Random.chooseItem(letters)
    return '"{}"'.format(s)


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
    return str(Random.getInteger(self.min, self.max))

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