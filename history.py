#!/usr/bin/python3
print("content-type: text/html")
print()

import os
import subprocess as sp
import cgi

form=cgi.FieldStorage()
b="sudo history -w h.txt"
a="sudo cat h.txt"
cmd2=sp.getoutput(a)
cmd=sp.getoutput(b)

print(cmd)
print(cmd2)
