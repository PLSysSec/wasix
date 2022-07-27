#!/bin/zsh

mkdir -p test
rm -r test/*
mkdir -p trace

WASMTIME_CLI_TEST=0

BUG_C=1
BUG_WAT=1
BUG_WASM=1

if [ $WASMTIME_CLI_TEST -eq 1 ]; then
    echo "Compiling Wasmtime cli_test"
    for f in wasmtime_cli_test/*.wat; do 
        echo $f
        wat2wasm --enable-all $f -o test/$(basename $f .wat).wasmtime.wasm
    done
fi

if [ $BUG_C -eq 1 ]; then
    echo "Compiling Bug reports in C"
    for f in bug_c/*.c; do 
        echo $f
        $WASI_SDK_PATH/bin/clang --sysroot=$WASI_SDK_PATH/share/wasi-sysroot $f -o test/$(basename $f .wat).bugc.wasm
    done
fi

if [ $BUG_WAT -eq 1 ]; then
    echo "Compiling Bug reports in wat"
    for f in bug_wat/*.wat; do 
        echo $f
        wat2wasm --enable-all $f -o test/$(basename $f .wat).bugwat.wasm
    done
fi

if [ $BUG_WASM -eq 1 ]; then
    echo "Compiling Bug reports in wasm"
    for f in bug_wasm/*.wasm; do 
        echo $f
        cp $f test/$(basename $f .wat).bugwasm.wasm
    done
fi