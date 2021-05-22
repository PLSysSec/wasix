# You need to do
# export WASI_SDK_PATH=/the/path/to/your/wasi

TEST_DIR  = $(CURDIR)/test
TRACE_DIR = $(CURDIR)/trace

OS   ?= not_specified
NUM  ?= 10
SIZE ?= 30

all:
	./src/wasix --all \
		--num $(NUM) \
		--size $(SIZE) \
		--test_dir $(TEST_DIR) \
		--trace_dir $(TRACE_DIR) \
		--os $(OS)

gen:
	./src/wasix --gen \
		--num $(NUM) \
		--size $(SIZE) \
		--test_dir $(TEST_DIR)

run:
	./src/wasix --run \
		--test_dir $(TEST_DIR) \
		--trace_dir $(TRACE_DIR) \
		--os $(OS)

check:
	./src/wasix --check \
		--trace_dir $(TRACE_DIR)

bug-run:
	./src/wasix --run \
		--test_dir $(CURDIR)/bug/wasm \
		--trace_dir $(CURDIR)/bug_trace \
		--os $(OS)

bug-check:
	./src/wasix --check \
		--trace_dir $(CURDIR)/bug_trace \

deep-clean:
	rm -rf test/
	rm -rf trace/
	rm -rf bug_trace