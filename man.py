#!/usr/bin/python3
print("content-type: text/html")
print()

import os
import subprocess as sp
import cgi

form=cgi.FieldStorage()
z=form.getvalue("k")
c="man "+z
cmd3=sp.getoutput(c)


print(cmd3)
output=sp.getstatusoutput(cmd3)
status=output[0]
out=output[1]


if status==0:
  print("{} ..".format(y))
else:
  print("{}".format(out))
