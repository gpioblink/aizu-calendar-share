import subprocess
for j in range(0,9):
    for i in range(0,300):
        gakuseki = 's12' + format(j,'01d') + '0'+ format(i, '03d')
        print(gakuseki)
        res = subprocess.call("find ./ML -name '*.txt' | xargs grep -l '" + gakuseki + "' > ../public/people/"+ gakuseki +".txt", shell=True)