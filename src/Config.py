import shutil
from pathlib import Path

def getConfig():
  config = {
    "lucet": True,
    "stdout": True,
    "stderr": False,
    "single_os": False,
    "runtimes": [
      {
        "name": "wasmtime",
        "getCmds":
          lambda dir, wasm: [["wasmtime", "--dir={}".format(dir), wasm]]
      },
      {
        "name": "wasmer",
        "getCmds":
          lambda dir, wasm: [["wasmer", "--dir={}".format(dir), wasm]]
      },
      {
        "name": "lucet",
        "getCmds":
          lambda dir, wasm: [
            ["lucetc-wasi", "-o", wasm.replace(".wasm", ".so"), wasm],
            ["lucet-wasi", wasm.replace(".wasm", ".so"), "--dir", "{}:{}".format(dir, dir)]
          ]
      },
      {
        "name": "wavm",
        "getCmds": 
          lambda dir, wasm: [["wavm", "run", "--mount-root", dir, wasm]]
      },
      {
        "name": "iwasm",
        "getCmds":
          lambda dir, wasm: [["iwasm", "--dir={}".format(dir), wasm]]
      },
      # {
      #   "name": "wasm3",
      #   "getCmds": 
      #     lambda _, wasm: [["wasm3", wasm]]
      # }
    ],
    "files": [
      {"path": "small.txt", "flags": ["O_RDWR",
                                      "O_RDONLY",
                                      "O_WRONLY",
                                      # "O_RDWR | O_CREAT | O_EXCL",
                                      # "O_RDWR | O_TRUNC",
                                      # "O_RDWR | O_PATH",
                                     ]},
      {"path": "medium.txt", "flags": ["O_RDWR"]},
      {"path": "large.txt", "flags": ["O_RDWR"]},
      {"path": "not_exist.txt", "flags": ["O_RDWR",
                                          "O_RDWR | O_CREAT",
                                          # "O_RDWR | O_CREAT | O_EXCL",
                                         ]},
    ],
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

  print("Prepared {}".format(str(working_dir)))

def collect_info(working_dir):
  info = ""
  tf_dir = Path("{}/test_files".format(working_dir))
  for file in tf_dir.iterdir():
    if file.is_file():
      stat = file.stat()
      info += "{}:\n".format(file.name)
      info += "st_size: {}\n".format(stat.st_size)
    # if config["single_os"]:
    #     f.write("st_mode: {}\n".format(stat.st_mode))
    #     f.write("st_nlink: {}\n".format(stat.st_nlink))
    #     f.write("st_uid: {}\n".format(stat.st_uid))
    #     f.write("st_gid: {}\n".format(stat.st_gid))
  return info