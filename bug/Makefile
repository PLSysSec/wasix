# You need to do
# export WASI_SDK_PATH=/the/path/to/your/wasi

WC     = $(WASI_SDK_PATH)/bin/clang
WCFLAG = --sysroot=$(WASI_SDK_PATH)/share/wasi-sysroot
CC     = clang

.PRECIOUS: %.wasm

SRCS=$(wildcard *.c)
OBJS=$(SRCS:.c=.wasm)

all: $(OBJS)

%.wat: %.wasm
	wasm2wat $< > $@

%.wasm: %.c
	mkdir -p $(CURDIR)/wasm
	$(WC) $(WCFLAG) $< -o wasm/$@

%.out: %.c
	$(CC) $< -o $@

cp:
	mkdir -p $(CURDIR)/test_files
	cp $(CURDIR)/../src/test_files/* $(CURDIR)/test_files/

clean:
	rm -rf *.wasm
	rm -rf *.wat
	rm -rf *.out
	rm -rf wasm/*.wasm
	rm -rf wasm/*.so

