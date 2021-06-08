# This file output the bad_syscall_rate and bug rate in corresponding res file.
# each line in the res file is the (syscall number, bad_syscall_rate/bug_rate %)
# You are allowed to change value
rm bad_syscall_rate.res
rm bug_rate.res
for i in {10,50,100,200,500,1000};do
    echo syscall num = $i
    cd ..
    rm -r test trace
    make all NUM=10 SIZE=$i OS=mzy 
    cd script
    python dealCE.py --os=mzy --size=$i
done