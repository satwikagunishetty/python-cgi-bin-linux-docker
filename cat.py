#!/usr/bin/python3
print("content-type: text/html")
print()

import os
import subprocess as sp
import cgi

form=cgi.FieldStorage()
x=form.getvalue("l")

a="cat "+x
cmd=sp.getoutput(a)

print(cmd)
