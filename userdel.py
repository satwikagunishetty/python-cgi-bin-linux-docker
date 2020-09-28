#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()

username=form.getvalue("de")


cmd="sudo userdel {0} ".format(username)

output=sp.getstatusoutput(cmd)

status=output[0]
out=output[1]

if status==0:
  print("successfully user {} is deleted..".format(username))
else:
  print("User not exists")
