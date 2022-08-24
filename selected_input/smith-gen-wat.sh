mkdir -p smith_wat
for i in {1..30}
do
    head -c 100 /dev/urandom | wasm-tools smith --allow-start true --ensure-termination -t > smith_wat/smith-wat-$i.wat
done
