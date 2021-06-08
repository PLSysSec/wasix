import argparse
import os
import numpy as np

def get_args():
    parser = argparse.ArgumentParser(description='A differential testing tool for WASI-compatible WASM runtimes')
    parser.add_argument("--os", help="os")
    parser.add_argument("--size", help="size of each test")
    args = parser.parse_args()
    return args
args = get_args()
runtimes = ["iwasm", "lucet", "wasmer", "wavm", "wasmtime"]

testcase_cnt = 0
bug_case_cnt = 0
syscall_cnt = 0
bad_syscall_cnt = 0

traces = os.listdir("../trace")
for case_dir in traces:
    if(case_dir[0:6]=="report"):
        continue
    for rtm in runtimes:
        testcase_cnt += 1
        case_files = os.listdir(os.path.join("../trace", case_dir))
        if(len(case_files)>=7):
            bug_case_cnt += 1 # if no bug, there will be 6 files(one for test_files dirs, five for runtime)
    
        with open(os.path.join("../trace/"+case_dir,"{}_{}_{}.trace".format(case_dir, rtm, args.os)),  'r') as f:
            for line in f:
                if line[0] == '@':
                    if(line[1] == 'T'):
                        syscall_cnt += int(line.split(":")[1])  
                    elif line[1] == 'B':
                        bad_syscall_cnt += int(line.split(":")[1])

res_f = open("bug_rate.res", "a+")               
res_f.write("%d %.6f\n"%(int(args.size), 100.0*bug_case_cnt/testcase_cnt))
res_f.close()

res_f = open("bad_syscall_rate.res", "a+")               
res_f.write("%d %.6f\n"%(int(args.size) ,100.0*bad_syscall_cnt/syscall_cnt))
res_f.close()