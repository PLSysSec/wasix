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
                                      "O_RDWR | O_CREAT | O_EXCL",
                                      "O_RDWR | O_TRUNC",
                                      # "O_RDWR | O_PATH",
                                     ]},
      # {"path": "medium.txt", "flags": ["O_RDWR"]},
      # {"path": "large.txt", "flags": ["O_RDWR"]},
      {"path": "not_exist.txt", "flags": ["O_RDWR",
                                          "O_RDWR | O_CREAT",
                                          "O_RDWR | O_CREAT | O_EXCL",
                                         ]},
    ],
    "env": ["ENV_VAR_1", "ENV_VAR_2"]
  }
  return config