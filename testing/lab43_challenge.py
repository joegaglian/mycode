#!/usr/bin/env python3

import os.path
import os

os.mknod("filename.txt")
if os.path.isfile('filename.txt'):
    print ("File exist")
else:
    print ("File not exist")
