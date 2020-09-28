#!/usr/bin/python3
print("content-type: text/html")
print()

import os
import subprocess as sp
import cgi

form=cgi.FieldStorage()
x=form.getvalue("m")

a="sudo touch "+x
cmd=sp.getoutput(a)

output=sp.getstatusoutput(cmd)

status=output[0]
out=output[1]


if status==0:
  print("{} is created successfully ..".format(x))
else:
  print("{}".format(out))
