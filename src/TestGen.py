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

  # TODO: Turn blocks to C code
  return test_blocks
  
def InitBlockPool(config):
  init = [
    Block(SYSCALL.clock_getres),
    Block(SYSCALL.clock_gettime),
  ]

  for env_var in config["env"]:
    init.append(
      Block(SYSCALL.getenv, env_var)
    )

  for i in range(len(config["files"])):
    path = config["files"][i]["path"]
    perm = config["files"][i]["permission"]
    fn = "test_files/{}".format(path)
    init.append(
      Block(SYSCALL.open, fn, perm, ret = Variable("int", "fd{}".format(i)))
    )

  pool = BlockPool()
  pool.addBlocks(init)
  return pool