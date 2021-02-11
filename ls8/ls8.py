#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *


cpu = CPU()

if(len(sys.argv)>1):
    from cpu import *
    cpu = CPU()
    cpu.load(sys.argv[1])
    cpu.run()
else:
    print("Dont forget the program file in order to run!")
    exit()

