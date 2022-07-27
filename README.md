# Usage

## Use make
Using `make` is the simplest way to interact with wasix.

`make gen [NUM=X] [SIZE=Y]`: generates X tests, where each test has Y syscalls, in `test/`

`make run [OS=OS_NAME]`: run all test in test/ and generate traces in `traces/`. Trace files have `OS_NAME` as part of their names.

`make check`: checks trace files in traces/ and generates a HTML report there.

`make all [NUM=X] [SIZE=Y] [OS=OS_NAME]`: equivalent to run all commands above

If not specified, defaults are `X=10, Y=30, OS=not_specified`

`run.sh` and `test.sh` each contains an example make commands.

## Use wasix
You can also use the `wasix` script directly to specify where you want to put tests and traces.
```
usage: wasix [-h] (--gen | --run | --check | --all) [--num NUM] [--size SIZE] [--test_dir TEST_DIR] [--trace_dir TRACE_DIR] [--os OS]

A differential testing tool for WASI-compatible WASM runtimes

optional arguments:
  -h, --help            show this help message and exit
  --gen                 generate tests
  --run                 run tests and generate trace files
  --check               compare trace files
  --all                 gen, run, and check; needs all other flags defined
  --num NUM             number of tests
  --size SIZE           size of each test
  --test_dir TEST_DIR   where wasm tests are/should be located
  --trace_dir TRACE_DIR
                        where traces file are/should be located
  --os OS               the name of current os
```

## Check bugs
We manually wrote several tests that reproduce the bugs found by wasix.
These tests are located under `bug/`
To run them and see the result, use

`make bug-comp`: compiles all the tests under bug/

`make bug-run`: run all test and generate trace in bug-trace/

`make bug-check`: check traces in bug-trace/ and generate a HTML report

`make bug-all`: equivalent to run all commands above

# About Wasix
As a cross testing tool for WASM runtimes, focusing on WASI implementations, Wasix can automatically

- generate random WASI-rich tests
- compile and run tests with different WASM runtimes
- check trace files generated by tests
- generate a report showing differences among runtimes in HTML

We have manually written several C files that can reproduce bugs we found using Wasix. To run them, see the [Check bugs](#check-bugs)

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ul>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#use-make">Use make</a></li>
        <li><a href="#use-wasix">Use wasix</a></li>
        <li><a href="#check-bugs">Check bugs</a></li>
      </ul>
    </li>
    <li>
      <a href="#dependencies">Installing Dependencies</a>
      <ul>
        <li><a href="#install-wasi-sdk">WASI SDK</a></li>
        <li><a href="#wasmtime">Wasmtime</a></li>
        <li><a href="#wasmer">Wasmer</a></li>
        <li><a href="#lucet">Lucet</a></li>
        <li><a href="#wavm">WAVM</a></li>
        <li><a href="#wamr">WAMR</a></li>
        <li><a href="#wasm3">Wasm3 (Not recommended)</a></li>
      </ul>
    </li>
  </ul>
</details>

# Dependencies

## Install WASI SDK
We use [WASI SDK](https://github.com/WebAssembly/wasi-sdk) to compile C tests to WASM.
To install WASI SDK, go to WASI SDK's [download page](https://github.com/WebAssembly/wasi-sdk/releases), choose the version for your OS.
Then run:
```
wget https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-12/wasi-sdk-12.0-[YOUR VERSION]}.tar.gz
tar xvf wasi-sdk-12.0-[YOUR VERSION].tar.gz
```

**You need to export your WASI SDK path to `WASI_SDK_PATH`, which should be `current_dir/wasi-sdk-12.0`**


## Install runtimes
Run commands below to see if you already have the runtimes installed.
```
wasmtime --version
wasmer --version
lucet-wasi --version
wasm3 --version
iwasm
wavm version
```

### Wasmtime
To install [Wasmtime](https://github.com/bytecodealliance/wasmtime), run
```
curl https://wasmtime.dev/install.sh -sSf | bash
```

To use wasmtime, run
```
wasmtime *.wasm --dir <access file dir> 
```

### Wasmer
To install [wasmer](https://github.com/wasmerio/wasmer), run
```
curl https://get.wasmer.io -sSfL | sh
```

To use wasmer, run
```
wasmer *.wasm --dir <access file dir> 
```

### Lucet
To install [Lucet](https://github.com/bytecodealliance/lucet), see [instructions for Linux](https://bytecodealliance.github.io/lucet/Compiling-on-Linux.html) or [instructions for macOS](https://bytecodealliance.github.io/lucet/Compiling-on-macOS.html).

We installed Lucet on Ubuntu by doing:
```
# Install dependency
sudo apt install curl ca-certificates cmake
# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
# Install lucet
git clone https://github.com/bytecodealliance/lucet.git
cd lucet
git submodule update --init --recursive
# This is something ignored in the doc.
sudo apt install libclang-dev
export LLVM_CONFIG_PATH="WASI_SDK_PATH/bin"
export PATH="WASI_SDK_PATH/bin:$PATH"
make install
```

To use lucet, run 
```
source /opt/lucet/bin/setenv.sh
lucetc-wasi -o *.so *.wasm
lucet-wasi  *.so --dir  <wasm path>:<host path>
#　e.g.  lucet-wasi  *.so --dir .:.
```


### WAVM
To install [WAVM](https://github.com/WAVM/WAVM), follow [the instruction](https://github.com/WAVM/WAVM/blob/master/Doc/GettingStarted.md) for your OS. 
For Linux, run
```
wget https://github.com/WAVM/WAVM/releases/download/nightly%2F2021-05-10/wavm-0.0.0-prerelease-linux.deb
sudo apt install ./wavm-0.0.0-prerelease-linux.deb
```

To use WAVM, run
```
wavm run --mount-root <access file dir> *.wasm
```

### WAMR
We only need the iwasm VM core from [WAMR](https://github.com/bytecodealliance/wasm-micro-runtime).
To install iwasm, follow [the instruction](https://github.com/bytecodealliance/wasm-micro-runtime/blob/main/doc/build_wamr.md), or run
```
sudo apt install build-essential cmake g++-multilib libgcc-8-dev lib32gcc-8-dev
or
brew install cmake

git clone https://github.com/bytecodealliance/wasm-micro-runtime.git
cd product-mini/platforms/<FIND YOU OS>/
mkdir build
cd build
cmake .. -DWAMR_BUILD_AOT=1 -DWAMR_BUILD_LIBC_WASI=1
make
```
You also need to export your build directory(where the `iwasm` binary locates) to `PATH`.

### Wasm3
To install [Wasm3](https://github.com/wasm3/wasm3):
for MacOS
```
brew install wasm3
```

for linux, download the binary `wasm3-cosmopolitan.com` from [the release page](https://github.com/wasm3/wasm3/releases/tag/v0.4.9). It's supposed to run on Linux.

Run ```wasm3 <file>``` for executing.

Note: seems at this time wasm3 doesn't support fstat.
