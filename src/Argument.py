import random

class RandomInteger:
  def __init__(self, min, max):
    self.min = min
    self.max = max

  def __str__(self):
    return "rand_int_{}_{}".format(str(self.min), str(self.max))

  def getValue(self):
    return random.randint(self.min, self.max)

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

Buffer.GLOBAL_RBUF = Buffer(-1)
Buffer.GLOBAL_WBUF = Buffer(-2)