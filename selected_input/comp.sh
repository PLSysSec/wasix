mkdir -p test
mkdir -p trace

echo "Compiling Wasmtime cli_test"
for f in wasmtime_cli_test/*.wat; do 
    echo $f
    wat2wasm $f -o test/$(basename $f .wat).wasm
done