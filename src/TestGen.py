import secrets
import subprocess
import os

from pathlib import Path

from CCodeGen import CCodeGen
from Block import BlockPool 
from Constraint import Constraint

def TestGen(num, size, test_dir, config):
  Path(test_dir).mkdir(parents=True, exist_ok=True)

  for i in range(num):
    blocks = generate_blocks(config, size)

    n = "test_" + secrets.token_hex(8)
    fn ="{}/{}.c".format(test_dir, n)
    f = open(fn, "w")
    f.write(CCodeGen(blocks, n))
    f.flush()
    print("Test #{} stored into {}".format(i, fn))

    wn = "{}/{}.wasm".format(test_dir, n)
    sdk = os.getenv('WASI_SDK_PATH')
    wasix = os.path.dirname(__file__)
    bin = "{}/bin/clang".format(sdk)
    root = "--sysroot={}/share/wasi-sysroot".format(sdk)
    include = "-I{}".format(wasix)
    p = subprocess.run([bin, root, include, fn, "-o", wn], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if not p.returncode == 0:
      print("Compilation failed for {}".format(fn))
      print(p.stdout)
      print(p.stderr)
    else:
      print("WASM: Compiled to {}".format(wn))

    # if config["lucet"]:
    #   son = "{}/{}.so".format(test_dir, n)
    #   p = subprocess.run(["lucetc-wasi", wn, "-o", son], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #   if not p.returncode == 0:
    #     print("lucetc-wasi failed for {}".format(fn))
    #     print(p.stdout)
    #     print(p.stderr)
    #   else:
    #     print("Lucetc: Compiled to {}".format(son))

def generate_blocks(config, test_size):
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