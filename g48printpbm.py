#!/usr/bin/env python

# (C) 2013 Travis Goodspeed <travis at radiantmachines.com>
# HP48 printer emulator for Bluetooth.

from Good48 import *;
import sys;

sys.stderr.write(

"""Be sure to pipe the output into a file, then convert that to a
better format.
"""

);

calc=Good48();
printer=Good48Printer(Good48PrintBufferPBM());

try:
    while 1:
        bs=calc.read(1);
        printer.handle(bs);
except KeyboardInterrupt:
    print printer.buf.getPBM();
