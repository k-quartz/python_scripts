import subprocess
import os

batcmd="dir"

result=subprocess.check_output(batcmd,shell=True).decode("utf-8")

result=result.split("\n")


for each in result[8:-3]:
    filname=each.split()[-1]
    print(filname)

f=open("sample.csv","a+")
f.write(str(result))
f.close()

