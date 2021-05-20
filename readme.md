# 0. Dependency
## 0.0 Install LLVM

## 0.1 Install WASI
```
wget https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-12/wasi-sdk-12.0-linux.tar.gz
tar xvf wasi-sdk-12.0-linux.tar.gz
```

Then the `WASI_SDK_PATH` is `current_path/wasi-sdk-12.0`



## 0.2 Install runtime
### 0.2.1 wasmtime
```
Install:
curl https://wasmtime.dev/install.sh -sSf | bash
```
See more info at `https://github.com/bytecodealliance/wasmtime`
After running install command, Open a new terminal to start using Wasmtime.

Run with wasmtime: `wasmtime *.wasm `--dir= \<your path\> 


### 0.2.2 wasmer 
```
Install:
curl https://get.wasmer.io -sSfL | sh
```
See more info at `https://github.com/wasmerio/wasmer` 

Run with `wasmer run *.wasm --dir=\<your path\>`