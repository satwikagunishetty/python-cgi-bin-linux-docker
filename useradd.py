#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()

username=form.getvalue("u")
passwd=form.getvalue("p")


cmd="sudo useradd {0} -p {1}".format(username,passwd)

output=sp.getstatusoutput(cmd)

status=output[0]
out=output[1]

if status==0:
  print("successfully user {} is created..".format(username))
else:
  print("User Already exists")
