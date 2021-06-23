from Block import Block
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
  lseek           = "lseek"
  ftruncate       = "ftruncate"
  posix_fadvise   = "posix_fadvise"
  fdatasync       = "fdatasync"
  fsync           = "fsync"
  pread           = "pread"
  pwrite          = "pwrite"