from Syscall import SYSCALL
from Template import *

SEP = "\n\t"

def CodeGen(blocks, fileName):
  code = [
    "FILE *fp = fopen(\"{0}.trace\", \"w\");".format(fileName),
    "log_add_fp(fp, LOG_TRACE);"
  ]
  for i in range(len(blocks)):
    code.append(BlockToCode(i, blocks[i]))
  return plain_c_template.format(SEP.join(code))

def BlockToCode(i, block):
  if block.syscall == SYSCALL.getenv :
    return 'getenv("{}");'.format(block.args[0])
  elif block.syscall == SYSCALL.open:
    return '{} = open("{}", {});'.format(
      block.ret.getDef(), block.args[0], block.args[1]
    )
  elif block.syscall == SYSCALL.read:
    # TODO buffer to str is wrong
    execCode = "readRet = read({}, {}, {});".format(
      block.args[0].getRef(), block.args[1].getValueStr(), block.args[2].getValueStr()
    )
    logCode = "log_trace(\"numOfBytes Read %d\", readRet);"
    code = [
      execCode,
      logCode
    ]
    return SEP.join(code)
  elif block.syscall == SYSCALL.write:
    execCode = "writeRet = write({}, {}, {});".format(
      block.args[0].getRef(), block.args[1].getValueStr(), block.args[2].getValueStr()
    )
    logCode = "log_trace(\"numOfBytes Written %d\", writeRet);"
    code = [
      execCode,
      logCode
    ]
    return SEP.join(code)
  elif block.syscall == SYSCALL.posix_fallocate:
    return "posix_fallocate({}, 0, {});".format(
      block.args[0].getRef(), block.args[1].getValueStr(), block.args[2].getValueStr()
    )
  elif block.syscall == SYSCALL.fstat:
    statName = "stat_{}".format(i)
    code = [
      "struct stat {};".format(statName),
      "fstat({}, &{});".format(block.args[0].getRef(), statName),
      "log_trace(\"stat info size %d\", {}.st_size);".format(statName)
    ]
    return SEP.join(code)
  elif block.syscall == SYSCALL.close:
    return "close({});".format(block.args[0].getRef())
  elif block.syscall == SYSCALL.clock_getres:
    tsName= "ts_{}".format(i)
    code = [
      "struct timespec {};".format(tsName),
      "clock_getres(CLOCK_REALTIME, &{});".format(tsName),
    ]
    return SEP.join(code)
  elif block.syscall == SYSCALL.clock_gettime:
    tsName= "ts_{}".format(i)
    code = [
      "struct timespec {};".format(tsName),
      "clock_gettime(CLOCK_REALTIME, &{});".format(tsName),
    ]
    return SEP.join(code)