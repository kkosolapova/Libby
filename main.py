#!/usr/bin/python
import os, sys
from wallaby import *
import wallaby as w
import constants as c
import actions as a


def main():
  #  a.drive_until_black()
    a.follow_line(15)
""" w.enable_servos()
    a.attack(3000)
    w.msleep(1000)
    a.turn_left(100, 1100)
    a.move(80, 4100)
    a.turn_right(100, 1500)
"""


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();