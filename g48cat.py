#!/usr/bin/env python

# (C) 2013 Travis Goodspeed <travis at radiantmachines.com>
# HP48 thin client proxy.

from Good48 import Good48;
import sys;

calc=Good48();

while 1:
    bs=calc.read(1);
    sys.stdout.write(bs);


