from Syscall import SYSCALL
from Template import *

SEP = "\n\t"
DEFAULT_RET = "syscallRet"

def make_syscall(ret, call_format_str, *args):
  if ret == None: ret = DEFAULT_RET
  call_str = call_format_str.format(*args)
  return ["{} = {};".format(ret, call_str)]

def default_log(name, msg=None):
  if msg == None: msg_str = ""
  else: msg_str = "({}) ".format(msg)
  return [
    "log_trace(\"{}{} returns %d\", syscallRet);".format(msg_str, name),
    "syscallCnt++; if(syscallRet==-1) badSyscallCnt++;",
  ]

def CodeGen(blocks, fileName):
  code = [
    "FILE *fp = fopen(\"{0}.trace\", \"w\");".format(fileName),
    "log_add_fp(fp, LOG_TRACE);"
  ]
  for i in range(len(blocks)):
    code.append(BlockToCode(i, blocks[i]))
  return plain_c_template.format(SEP.join(code))

def BlockToCode(i, block):
  code = []
  if block.syscall == SYSCALL.getenv :
    code = [
      'getenv("{}");'.format(block.args[0]),
      'syscallCnt++;',
    ]
  elif block.syscall == SYSCALL.open:
    # execCode = '{} = open("{}", {});'.format(
    #   block.ret.getDef(), block.args[0], block.args[1]
    # )
    # fdName = block.ret.getDef().split(" ")[1]
    code += make_syscall(block.ret.getDef(), 'open("{}", {})', block.args[0], block.args[1])
    code += ['syscallCnt++; if({}==-1) badSyscallCnt++;'.format(block.ret.getRef())]
  elif block.syscall == SYSCALL.read:
    # execCode = "readRet = read({}, {}, {});".format(
    #   block.args[0].getRef(), block.args[1].getValueStr(), block.args[2].getValueStr()
    # )
    # logCode = "log_trace(\"numOfBytes Read %d\", readRet);"
    # syscallCntCode = "syscallCnt++; if(readRet==-1) badSyscallCnt++;"
    code += make_syscall(None, "read({}, {}, {})",
        block.args[0].getRef(), block.args[1].getValueStr(), block.args[2].getValueStr())
    code += default_log("read", block.args[0].getRef())
  elif block.syscall == SYSCALL.write:
    # execCode = "writeRet = write({}, {}, {});".format(
    #   block.args[0].getRef(), block.args[1].getValueStr(), block.args[2].getValueStr()
    # )
    # logCode = "log_trace(\"numOfBytes Written %d\", writeRet);"
    # syscallCntCode = "syscallCnt++; if(writeRet==-1) badSyscallCnt++;"
    code += make_syscall(None, "write({}, {}, {})",
        block.args[0].getRef(), block.args[1].getValueStr(), block.args[2].getValueStr())
    code += default_log("write", block.args[0].getRef())
  elif block.syscall == SYSCALL.posix_fallocate:
    # execCode = "syscallRet = posix_fallocate({}, {}, {});".format(
    #   block.args[0].getRef(), block.args[1].getValueStr(), block.args[2].getValueStr()
    # )
    # syscallCntCode = 'syscallCnt++;'
    code += make_syscall(None, "posix_fallocate({}, 0, {})",
        block.args[0].getRef(), block.args[1].getValueStr(), block.args[2].getValueStr())
    code += default_log("fallocate", block.args[0].getRef())
  elif block.syscall == SYSCALL.fstat:
    statName = "stat_{}".format(i)
    code = [
      "struct stat {};".format(statName),
      "syscallRet = fstat({}, &{});".format(block.args[0].getRef(), statName),
      "log_trace(\"stat info size %d\", {}.st_size);".format(statName),
      'syscallCnt++; if(syscallRet==-1) badSyscallCnt++;'
    ]
  elif block.syscall == SYSCALL.close:
    # execCode = "syscallRet = close({});".format(block.args[0].getRef())
    # syscallCntCode = 'syscallCnt++; if(syscallRet==-1) badSyscallCnt++;'
    code += make_syscall(None, "close({})", block.args[0].getRef())
    code += default_log("close")
  elif block.syscall == SYSCALL.clock_getres:
    tsName= "ts_{}".format(i)
    code = [
      "struct timespec {};".format(tsName),
      "syscallRet = clock_getres(CLOCK_REALTIME, &{});".format(tsName),
      'syscallCnt++; if(syscallRet==-1) badSyscallCnt++;'
    ]
  elif block.syscall == SYSCALL.clock_gettime:
    tsName= "ts_{}".format(i)
    code = [
      "struct timespec {};".format(tsName),
      "syscallRet = clock_gettime(CLOCK_REALTIME, &{});".format(tsName),
      'syscallCnt++; if(syscallRet==-1) badSyscallCnt++;'
    ]
  elif block.syscall == SYSCALL.lseek:
    code += make_syscall(None, "lseek({}, {}, {})",
        block.args[0].getRef(), block.args[1].getValueStr(), block.args[2])
    code += default_log("lseek", block.args[0].getRef())
  elif block.syscall == SYSCALL.ftruncate:
    code += make_syscall(None, "ftruncate({}, {})",
        block.args[0].getRef(), block.args[1].getValueStr())
    code += default_log("ftruncate", block.args[0].getRef())

  return SEP.join(code)