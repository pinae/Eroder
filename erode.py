#!/usr/bin/env python
# coding=utf-8
from __future__ import division, print_function, unicode_literals
import numpy as np
from config import map_dimensions

height_map = np.zeros(map_dimensions+(3,), dtype=np.uint8)
