import os
import subprocess

batcmd = "dir"

# Below line will get the out put of the command in result variable
result = subprocess.check_output(batcmd, shell=True).decode("utf-8")

# below lines are just for "dir" command it will not be same for all the commands.
result = result.split("\n")
for each in result[8:-3]:
    filname = each.split()[-1]
    print(filname)

f = open("sample.csv", "a+")
f.write(str(result))
f.close()
