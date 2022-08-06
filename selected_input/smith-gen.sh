mkdir -p smith
for i in {1..30}
do
    head -c 100 /dev/urandom | wasm-tools smith --allow-start true --ensure-termination -o smith/smith-$i.wasm
done
