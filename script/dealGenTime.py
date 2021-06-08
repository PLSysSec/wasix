import argparse
def get_args():
    parser = argparse.ArgumentParser(description='A differential testing tool for WASI-compatible WASM runtimes')
    parser.add_argument("--size", help="size of each test")
    parser.add_argument("--file", help="read file")

    args = parser.parse_args()
    return args
args = get_args()
with open(args.file, 'r') as f:
    for line in f:
        if line[0] == '@':
            time = float(line.split(":")[1])
print("%s %.7f\n"%(args.size,time))