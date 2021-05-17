# You need to do
# export WASI_SDK_PATH=/the/path/to/your/wasi

WC     = $(WASI_SDK_PATH)/bin/clang
WCFLAG = --sysroot=$(WASI_SDK_PATH)/share/wasi-sysroot
CC     = clang

.PRECIOUS: %.wasm

%.wat: %.wasm
	wasm2wat $< > $@

%.wasm: %.c
	$(WC) $(WCFLAG) $< -o $@

%.out: %.c
	$(CC) $< -o $@

clean:
	rm -rf *.wasm
	rm -rf *.wat
	rm -rf *.out

