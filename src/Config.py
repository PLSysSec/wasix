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
      {"path": "small.txt", "permission": "O_RDWR"},
      # {"path": "small.txt", "permission": "O_RDONLY"},
      {"path": "medium.txt", "permission": "O_RDWR"},
      {"path": "large.txt", "permission": "O_RDWR"},
      {"path": "not_exist.txt", "permission": "O_RDWR"},
    ],
    "env": ["ENV_VAR_1", "ENV_VAR_2"]
  }
  return config