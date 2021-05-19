from Block import Block
from Block import BlockPool
from Argument import *

class SYSCALL:
  getenv          = "getenv"
  open            = "open"
  read            = "read"
  write           = "write"
  posix_fallocate = "posix_fallocate"
  fstat           = "fstat"
  close           = "close"
  clock_getres    = "clock_getres"
  clock_gettime   = "clock_gettime"


class Constraint:
  def getCanFollow(prev : Block):
    canFollow = []
    if prev.syscall == SYSCALL.getenv: pass
    elif prev.syscall == SYSCALL.open:
      fd = prev.ret
      canFollow = [
        Block(SYSCALL.read, fd, Buffer.GLOBAL_RBUF, 0),
        Block(SYSCALL.read, fd, Buffer.GLOBAL_RBUF, 1),
        Block(SYSCALL.read, fd, Buffer.GLOBAL_RBUF, 4096),
        Block(SYSCALL.read, fd, Buffer.GLOBAL_RBUF, RandomInteger(0, 4096)),

        Block(SYSCALL.write, fd, Buffer.GLOBAL_WBUF, 0),
        Block(SYSCALL.write, fd, Buffer.GLOBAL_WBUF, 1),
        Block(SYSCALL.write, fd, Buffer.GLOBAL_WBUF, 4096),
        Block(SYSCALL.write, fd, Buffer.GLOBAL_WBUF, RandomInteger(0, 4096)),

        Block(SYSCALL.posix_fallocate, fd, 0, 0),
        Block(SYSCALL.posix_fallocate, fd, 0, 1),
        Block(SYSCALL.posix_fallocate, fd, 0, 4096),
        Block(SYSCALL.posix_fallocate, fd, 0, RandomInteger(0, 4096)),

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
    elif prev.syscall == SYSCALL.open: pass
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
    return Constraint.__noRemove
  def __noRemove(_): return
    
