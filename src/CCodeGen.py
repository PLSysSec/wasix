from Libc import SYSCALL
from Template import *

SEP = "\n\t"

def CCodeGen(blocks, fileName):
  code = [
    "FILE *fp = fopen(\"{0}.trace\", \"w\");".format(fileName),
    "log_add_fp(fp, LOG_TRACE);"
  ]
  for i in range(len(blocks)):
    code.append(BlockToCode(i, blocks[i]))
  return plain_c_template.format(SEP.join(code))

def BlockToCode(i, block):
  if block.syscall == SYSCALL.getenv :
    execCode = 'getenv("{}");'.format(block.args[0])
    syscallCntCode = 'syscallCnt++;'
    code = [
      execCode,
      syscallCntCode
    ]
    
    return SEP.join(code)
  elif block.syscall == SYSCALL.open:
    execCode = '{} = open("{}", {});'.format(
      block.ret.getDef(), block.args[0], block.args[1]
    )
    fdName = block.ret.getDef().split(" ")[1]
    syscallCntCode = 'syscallCnt++; if({}==-1) badSyscallCnt++;'.format(fdName)
    code = [
      execCode,
      syscallCntCode
    ]
    return SEP.join(code)
  elif block.syscall == SYSCALL.read:
    # TODO buffer to str is wrong
    execCode = "readRet = read({}, {}, {});".format(
      block.args[0].getRef(), block.args[1].getValueStr(), block.args[2].getValueStr()
    )
    logCode = "log_trace(\"numOfBytes Read %d\", readRet);"
    syscallCntCode = "syscallCnt++; if(readRet==-1) badSyscallCnt++;"
    code = [
      execCode,
      logCode,
      syscallCntCode
    ]
    return SEP.join(code)
  elif block.syscall == SYSCALL.write:
    execCode = "writeRet = write({}, {}, {});".format(
      block.args[0].getRef(), block.args[1].getValueStr(), block.args[2].getValueStr()
    )
    logCode = "log_trace(\"numOfBytes Written %d\", writeRet);"
    syscallCntCode = "syscallCnt++; if(writeRet==-1) badSyscallCnt++;"
    code = [
      execCode,
      logCode,
      syscallCntCode
    ]
    return SEP.join(code)
  elif block.syscall == SYSCALL.posix_fallocate:
    execCode = "syscallRet = posix_fallocate({}, 0, {});".format(
      block.args[0].getRef(), block.args[1].getValueStr(), block.args[2].getValueStr()
    )
    syscallCntCode = 'syscallCnt++;'
    code = [
      execCode,
      syscallCntCode
    ]
    return SEP.join(code)
  elif block.syscall == SYSCALL.fstat:
    statName = "stat_{}".format(i)
    code = [
      "struct stat {};".format(statName),
      "syscallRet = fstat({}, &{});".format(block.args[0].getRef(), statName),
      "log_trace(\"stat info size %d\", {}.st_size);".format(statName),
      'syscallCnt++; if(syscallRet==-1) badSyscallCnt++;'
    ]
    return SEP.join(code)
  elif block.syscall == SYSCALL.close:
    execCode = "syscallRet = close({});".format(block.args[0].getRef())
    syscallCntCode = 'syscallCnt++; if(syscallRet==-1) badSyscallCnt++;'
    code = [
      execCode,
      syscallCntCode
    ]
    return SEP.join(code)
  elif block.syscall == SYSCALL.clock_getres:
    tsName= "ts_{}".format(i)
    code = [
      "struct timespec {};".format(tsName),
      "syscallRet = clock_getres(CLOCK_REALTIME, &{});".format(tsName),
      'syscallCnt++; if(syscallRet==-1) badSyscallCnt++;'
    ]
    return SEP.join(code)
  elif block.syscall == SYSCALL.clock_gettime:
    tsName= "ts_{}".format(i)
    code = [
      "struct timespec {};".format(tsName),
      "syscallRet = clock_gettime(CLOCK_REALTIME, &{});".format(tsName),
      'syscallCnt++; if(syscallRet==-1) badSyscallCnt++;'
    ]
    return SEP.join(code)
  elif block.syscall == SYSCALL.lseek:
    code = [
      "lseekRet = lseek({}, {}, {});".format(
        block.args[0].getRef(), block.args[1].getValueStr(), block.args[2].getValueStr()
      ),
      "log_trace(\"lseek returns: %d\", lseekRet);",
      'syscallCnt++; if(lseekRet==-1) badSyscallCnt++;'
    ]
    return SEP.join(code)
  elif block.syscall == SYSCALL.ftruncate:
    code = [
      "syscallRet = ftruncate({}, {});".format(
        block.args[0].getRef(), block.args[1].getValueStr()
      ),
      "log_trace(\"ftruncate returns: %d\", syscallRet);",
      'syscallCnt++; if(lseekRet==-1) badSyscallCnt++;'
    ]
    return SEP.join(code)
  elif block.syscall == SYSCALL.posix_fadvise:
    code = [
      "syscallRet = posix_fadvise({}, {}, {}, {});".format(
        block.args[0].getRef(), block.args[1].getValueStr(),
        block.args[2].getValueStr(), block.args[3].getValueStr()
      ),
      "log_trace(\"ftruncate returns: %d\", syscallRet);",
      'syscallCnt++; if(lseekRet==-1) badSyscallCnt++;'
    ]
    return SEP.join(code)
  elif block.syscall == SYSCALL.fdatasync:
    code = [
      "syscallRet = fdatasync({});".format(block.args[0].getRef()),
      "log_trace(\"ftruncate returns: %d\", syscallRet);",
      'syscallCnt++; if(lseekRet==-1) badSyscallCnt++;'
    ]
    return SEP.join(code)
  elif block.syscall == SYSCALL.fsync:
    code = [
      "syscallRet = fsync({});".format(block.args[0].getRef()),
      "log_trace(\"ftruncate returns: %d\", syscallRet);",
      'syscallCnt++; if(lseekRet==-1) badSyscallCnt++;'
    ]
    return SEP.join(code)