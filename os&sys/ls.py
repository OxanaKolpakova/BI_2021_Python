#!/usr/bin/python3

import sys
import argparse
import os
if len(sys.argv)==1:
    print(*os.listdir("."), sep="\n")
else:
    dirs = sys.argv[1:]
    for dir in dirs:
        print(dir, end = "" )
        print(":")
        print(*os.listdir(dir), sep="\n")
