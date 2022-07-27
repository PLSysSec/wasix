import shutil
from pathlib import Path

from AbstractFS import File
from AbstractFS import Dir
from AbstractFS import TestDirectory

def getWaveBase():
  wave_dir_name = "verified-wasm-runtime"
  wasixBase = Path(__file__).parent.parent.resolve()
  outter = wasixBase.parent
  if(outter.stem == wave_dir_name): return str(outter) + "/"
  sibling = wasixBase.parent.joinpath(wave_dir_name)
  if(sibling.is_dir()): return str(sibling) + "/"
  print(f"Cannot find {wave_dir_name}, please edit {__file__}")
  quit(1)

WAVE_BASE = getWaveBase()

def getCmdsForVeriWasm(dir, wasm):
  CC = WAVE_BASE + "rlbox_wasm2c_sandbox/build/_deps/wasiclang-src/build/install/opt/wasi-sdk/bin/clang"
  CFLAGS = ["--sysroot", "{}rlbox_wasm2c_sandbox/build/_deps/wasiclang-src/src/wasi-libc/sysroot/".format(WAVE_BASE)]
  LDFLAGS = ["-Wl,--export-all", "-Wl,--growable-table"]
  RLBOX_ROOT = WAVE_BASE + "rlbox_wasm2c_sandbox/"
  WASM2C_BIN_ROOT = RLBOX_ROOT + "build/_deps/mod_wasm2c-src/bin/"
  WASM2C_SRC_ROOT = RLBOX_ROOT + "build/_deps/mod_wasm2c-src/wasm2c/"
  WASM2C = WASM2C_BIN_ROOT + "wasm2c"
  RUNNER = WASM2C_BIN_ROOT + "wasm2c-runner"

  GCC_I = [
    "-I{}".format(WASM2C_SRC_ROOT),
    WASM2C_SRC_ROOT + "wasm-rt-impl.c",
    WASM2C_SRC_ROOT + "wasm-rt-os-unix.c",
    WASM2C_SRC_ROOT + "wasm-rt-os-win.c",
    WASM2C_SRC_ROOT + "wasm-rt-wasi.c",
    WAVE_BASE + "target/release/libwave.so",
    "-I" + WAVE_BASE + "bindings"
  ]

  f_c = wasm.replace(".wasm", ".c")
  f_veri_wasm = wasm.replace(".wasm", ".veri.wasm")
  f_veri_wasm_c = wasm.replace(".wasm", ".veri.wasm.c")
  f_veri_wasm_c_run = wasm.replace(".wasm", ".veri.wasm.c.run")
  cmds = [
    [CC]+CFLAGS+[f_c, "-o", f_veri_wasm, "-I/home/zijie/wasix/src"]+LDFLAGS,
    [WASM2C, "-o", f_veri_wasm_c, f_veri_wasm],
    ["gcc", "-shared", "-fPIC", "-O3", "-o", f_veri_wasm_c_run, f_veri_wasm_c] + GCC_I,
    [RUNNER,  f_veri_wasm_c_run, "--homedir="+dir]
  ]
  # for cmd in cmds:
  #   print(" ".join(cmd))
  return cmds

def getConfig():
  td = TestDirectory([
    File("small.txt"),
    File("medium.txt"),
    File("large.txt"),
  ])
  config = {
    "lucet": False,
    "stdout": True,
    "stderr": False,
    "single_os": False,
    "test_directory": td,
    "runtimes": [
      {
        "name": "wasmtime",
        "getCmds":
          lambda dir, wasm: [["wasmtime", "--dir={}".format(dir), "--enable-all", wasm]]
      },
      {
        "name": "wasmer",
        "getCmds":
          lambda dir, wasm: [["wasmer", "--dir={}".format(dir), "--enable-all", wasm]]
      },
      # {
      #   "name": "veriwasm",
      #   "getCmds": getCmdsForVeriWasm
      # },
      # {
      #   "name": "lucet",
      #   "getCmds":
      #     lambda dir, wasm: [
      #       ["lucetc-wasi", "-o", wasm.replace(".wasm", ".so"), wasm],
      #       ["lucet-wasi", wasm.replace(".wasm", ".so"), "--dir", "{}:{}".format(dir, dir)]
      #     ]
      # },
      {
        "name": "wavm",
        "getCmds": 
          lambda dir, wasm: [["wavm", "run", "--function=_start", "--enable", "all", "--mount-root", dir, wasm]]
      },
      {
        "name": "iwasm",
        "getCmds":
          lambda dir, wasm: [["iwasm", "--dir={}".format(dir), "--function", "_start", wasm]]
      },
      {
        "name": "spec",
        "getCmds":
          lambda dir, wasm: [["/Users/zijie/Programs/wasix/selected_input/wasm", wasm]]
      },
      # {
      #   "name": "wasm3",
      #   "getCmds": 
      #     lambda _, wasm: [["wasm3", wasm]]
      # }
    ],
    # "files": [
    #   {"path": "small.txt", "flags": ["O_RDWR",
    #                                   "O_RDONLY",
    #                                   "O_WRONLY",
    #                                   # "O_RDWR | O_CREAT | O_EXCL",
    #                                   # "O_RDWR | O_TRUNC",
    #                                   # "O_RDWR | O_PATH",
    #                                  ]},
    #   {"path": "test_files/medium.txt", "flags": ["O_RDWR"]},
    #   {"path": "test_files/large.txt", "flags": ["O_RDWR"]},
    #   {"path": "test_files/not_exist.txt", "flags": ["O_RDWR",
    #                                       "O_RDWR | O_CREAT",
    #                                       # "O_RDWR | O_CREAT | O_EXCL",
    #                                      ]},
    # ],
    # "dirs": [
    #   ".",
    #   "./test_files",
    #   "empty_dir",
    #   "normal_dir",
    #   "link_dir"
    # ],
    "env": ["ENV_VAR_1", "ENV_VAR_2"]
  }
  return config

def prep_env(working_dir):
  test_file_dir = Path("{}/test_files".format(Path(__file__).parent))
  working_test_file_dir = Path("{}/test_files".format(working_dir))
  working_test_file_dir.mkdir(parents=True, exist_ok=True)
  for tfile in test_file_dir.iterdir():
    if tfile.suffix == ".txt":
      shutil.copy2(str(tfile), working_test_file_dir)
  
  # empty_dir = Path("{}/empty_dir".format(working_dir))
  # empty_dir.mkdir()

  # normal_dir = Path("{}/normal_dir".format(working_dir))
  # normal_dir.mkdir()
  # for tfile in test_file_dir.iterdir():
  #   if tfile.suffix == ".txt":
  #     shutil.copy2(str(tfile), normal_dir)

  # link_dir = Path("{}/normal_dir".format(working_dir))
  # link_dir.mkdir()
  # for tfile in test_file_dir.iterdir():
  #   if tfile.suffix == ".txt":
  #     shutil.copy2(str(tfile), link_dir)

  print("Prepared {}".format(str(working_dir)))

def filter_output_before_checking(lines):
  def remove_black_list(line):
    black_list = ["fdmap ="]
    for word in black_list:
      if word in line: return False
    return True
  filtered = list(filter(remove_black_list, lines))
  return filtered

def collect_info(working_dir):
  info = ""
  tf_dir = Path("{}/test_files".format(working_dir))
  for file in tf_dir.iterdir():
    if file.is_file():
      stat = file.stat()
      info += "{}:\n".format(file.name)
      info += "st_size: {}\n".format(stat.st_size)
      info += "st_mode: {}\n".format(stat.st_mode)
    # if config["single_os"]:
    #     f.write("st_mode: {}\n".format(stat.st_mode))
    #     f.write("st_nlink: {}\n".format(stat.st_nlink))
    #     f.write("st_uid: {}\n".format(stat.st_uid))
    #     f.write("st_gid: {}\n".format(stat.st_gid))
  return info