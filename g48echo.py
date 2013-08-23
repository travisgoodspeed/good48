#!/usr/bin/env python

# (C) 2013 Travis Goodspeed <travis at radiantmachines.com>
# HP48 thin client proxy.

from Good48 import Good48;
import sys;

print Good48

calc=Good48();


calc.write(sys.argv[1]);
