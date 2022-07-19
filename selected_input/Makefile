comp:
	./comp.sh

run:
	../src/wasix --run --test_dir ./test --trace_dir ./trace --os macOS
	../src/wasix --check --trace_dir ./trace

clean:
	rm -rf trace/*