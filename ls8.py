#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

cpu.load("/Users/swa_isthecreator/Documents/Lambda-CS-Sprints/Sprint-Challenge--Computer-Architecture/sctest.ls8")
cpu.run()