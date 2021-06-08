# This will output the testcase generation time in gentime.res
#each line is the (syscall number, generation time for generating syscalls of number)
#don't change NUM!!!

resFile=gentime
echo > ${resFile}
echo > ${resFile}.res
for i in {10,50,100,500,1000,10000};do
    echo syscall num = $i
    cd ..
    rm -r test
    make gen NUM=1 SIZE=$i > script/${resFile}
    cd script
    python dealGenTime.py --size=$i --file=${resFile} >> ${resFile}.res
done
