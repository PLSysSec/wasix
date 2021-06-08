rm -r test trace
make all NUM=1 SIZE=$1
cat trace/[0-9a-f]*/*iwasm_not_specified.trace

