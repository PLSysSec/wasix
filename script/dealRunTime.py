import argparse
import os
import numpy as np

def get_args():
    parser = argparse.ArgumentParser(description='A differential testing tool for WASI-compatible WASM runtimes')
    parser.add_argument("--size", help="size of each test")
    parser.add_argument("--os", help="os")
    args = parser.parse_args()
    return args
args = get_args()
runtimes = ["iwasm", "lucet", "wasmer", "wavm", "wasmtime"]

traces = os.listdir("../trace")
for rtm in runtimes:
    res_f = open("{}_run_time.res".format(rtm), "a")
    time = []
    for case_dir in traces:
        if(case_dir[0:6]=="report"):
            continue
        with open(os.path.join("../trace/"+case_dir,"{}_{}_{}.trace".format(case_dir, rtm, args.os)),  'r') as f:
            for line in f:
                if line[0] == '$':
                    time.append(float(line.split(":")[1]))
                    #res_f.write("-%s %s\n"%(args.size,(time)))
    res_f.write("%s %s\n"%(args.size,np.mean(time)))
    res_f.close()