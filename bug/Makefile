# You need to do
# export WASI_SDK_PATH=/the/path/to/your/wasi

WC     = $(WASI_SDK_PATH)/bin/clang
WCFLAG = --sysroot=$(WASI_SDK_PATH)/share/wasi-sysroot
CC     = clang
CFLAG  = -I$(CURDIR)/../src

.PRECIOUS: %.wasm

SRCS=$(wildcard *.c)
OBJS=$(SRCS:.c=.so)

all: $(OBJS)

%.wat: %.wasm
	wasm2wat $< > $@

%.wasm: %.c
	mkdir -p $(CURDIR)/wasm
	$(WC) $(WCFLAG) $(CFLAG) $< -o wasm/$@

%.so: %.wasm
	lucetc-wasi wasm/$< -o wasm/$@

%.out: %.c
	$(CC) $< -o $@

cp:
	mkdir -p $(CURDIR)/test_files
	rm -rf test_files/*
	cp $(CURDIR)/../src/test_files/* $(CURDIR)/test_files/

clean:
	rm -rf *.wasm
	rm -rf *.wat
	rm -rf *.out
	rm -rf wasm/*.wasm
	rm -rf wasm/*.so

