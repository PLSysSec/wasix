# this srcipt is designed to test the running/executing time for different number of syscalls
# It will generate five .res files, named <runtime>_run_time.res, in the file each line is a (syscall number, executing time for syscalls of number)
# You are allowed to change value
rm *run_time.res
for i in {10,50,100,200,500,1000};do
    echo syscall num = $i
    cd ..
    rm -r test trace
    make all NUM=10 SIZE=$i OS=mzy
    cd script
    python dealRunTime.py --size=$i --os=mzy
done
