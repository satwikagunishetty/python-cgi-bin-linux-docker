#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()

osname=form.getvalue("dr")


cmd="sudo docker rm {0}".format(osname)

output=sp.getstatusoutput(cmd)
print(output)
status=output[0]
out=output[1]

if status==0:
  print("docker container  {} removed ..".format(osname))
else:
  print("some error : {}".format(out))
