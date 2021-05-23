from Block import *
from Syscall import *

def TestGen(config, test_size):
  pool = InitBlockPool(config)
  test_blocks = []
  for i in range(test_size):
    block = pool.getRandomBlock()
    canFollow = Constraint.getCanFollow(block)
    pool.addBlocks(canFollow)
    removalFunc = Constraint.getRemovalFunc(block)
    pool.popBlocks(removalFunc)
    test_blocks.append(block)

  return test_blocks
  
def InitBlockPool(config):
  init = Constraint.getInitBlocks(config)
  pool = BlockPool()
  pool.addBlocks(init)
  return pool