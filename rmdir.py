#!/usr/bin/python3
print("content-type: text/html")
print()

import os
import subprocess as sp
import cgi

form=cgi.FieldStorage()
y=form.getvalue("n")
b="sudo rmdir "+y 
cmd1=sp.getoutput(b)


print(cmd1)
output=sp.getstatusoutput(cmd1)

status=output[0]
out=output[1]


if status==0:
  print("{} is deleted successfully ..".format(y))
else:
  print("{}".format(out))
