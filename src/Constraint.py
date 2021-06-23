from Block import Block
from Libc import SYSCALL 
from Argument import *

class Constraint:
  def getInitBlocks(config):
    Variable.clear_count()
    init = [
      Block(SYSCALL.clock_getres),
      Block(SYSCALL.clock_gettime),
    ]

    for env_var in config["env"]:
      init.append(
        Block(SYSCALL.getenv, env_var)
      )

    for i in range(len(config["files"])):
      file = config["files"][i]
      path = file["path"]
      for flag in file["flags"]:
        fn = "test_files/{}".format(path)
        init.append(
          Block(SYSCALL.open, fn, flag, ret = Variable("int", name = "fd"))
        )
    return init

  def getCanFollow(prev : Block):
    canFollow = []
    if prev.syscall == SYSCALL.getenv: pass
    elif prev.syscall == SYSCALL.open:
      fd = prev.ret
      canFollow = [
        Block(SYSCALL.read, fd, Buffer.GLOBAL_RBUF, Integer(0)),
        Block(SYSCALL.read, fd, Buffer.GLOBAL_RBUF, Integer(1)),
        Block(SYSCALL.read, fd, Buffer.GLOBAL_RBUF, Integer(4096)),
        Block(SYSCALL.read, fd, Buffer.GLOBAL_RBUF, RandomInteger(0, 4096)),

        Block(SYSCALL.write, fd, Buffer.GLOBAL_WBUF, Integer(0)),
        Block(SYSCALL.write, fd, Buffer.GLOBAL_WBUF, Integer(1)),
        Block(SYSCALL.write, fd, Buffer.GLOBAL_WBUF, Integer(4096)),
        Block(SYSCALL.write, fd, Buffer.GLOBAL_WBUF, RandomInteger(0, 4096)),

        Block(SYSCALL.posix_fallocate, fd, Integer(0), Integer(0)),
        Block(SYSCALL.posix_fallocate, fd, Integer(0), Integer(1)),
        Block(SYSCALL.posix_fallocate, fd, Integer(0), Integer(4096)),
        Block(SYSCALL.posix_fallocate, fd, Integer(0), RandomInteger(0, 4096)),

        Block(SYSCALL.lseek, fd, Integer(0), "SEEK_SET"),
        Block(SYSCALL.lseek, fd, RandomInteger(0, 512), "SEEK_SET"),
        Block(SYSCALL.lseek, fd, Integer(0), "SEEK_CUR"),
        Block(SYSCALL.lseek, fd, RandomInteger(0, 512), "SEEK_CUR"),
        Block(SYSCALL.lseek, fd, Integer(0), "SEEK_END"),
        Block(SYSCALL.lseek, fd, RandomInteger(0, 512), "SEEK_END"),

        Block(SYSCALL.ftruncate, fd, Integer(0)),
        Block(SYSCALL.ftruncate, fd, RandomInteger(0, 8192)),

        Block(SYSCALL.fstat, fd),
        Block(SYSCALL.close, fd)
      ]
    elif prev.syscall == SYSCALL.read: pass
    elif prev.syscall == SYSCALL.write: pass
    elif prev.syscall == SYSCALL.posix_fallocate: pass
    elif prev.syscall == SYSCALL.fstat: pass
    elif prev.syscall == SYSCALL.close: pass
    elif prev.syscall == SYSCALL.clock_getres: pass
    elif prev.syscall == SYSCALL.clock_gettime: pass

    return canFollow


  def getRemovalFunc(prev : Block):
    if prev.syscall == SYSCALL.getenv: pass
    elif prev.syscall == SYSCALL.open:
      def handleOpen(pool):
        pool.pop(prev.getID(), None)
        new_open = Block.copy(prev, ret = Variable("int", prev.ret.ori_name))
        pool[new_open.getID()] = new_open
      return handleOpen
    elif prev.syscall == SYSCALL.read: pass
    elif prev.syscall == SYSCALL.write: pass
    elif prev.syscall == SYSCALL.posix_fallocate: pass
    elif prev.syscall == SYSCALL.fstat: pass
    elif prev.syscall == SYSCALL.close:
      def handleClose(pool):
        for id, block in list(pool.items()):
          if(block.fd == prev.fd):
            pool.pop(id)
      return handleClose

    elif prev.syscall == SYSCALL.clock_getres: pass
    elif prev.syscall == SYSCALL.clock_gettime: pass
    elif prev.syscall == SYSCALL.lseek: pass
    elif prev.syscall == SYSCALL.ftruncate: pass
    return Constraint.__noRemove
  def __noRemove(_): return