#!/usr/bin/env python
# coding=utf-8
from __future__ import division, print_function, unicode_literals
import numpy as np


def blockmap():
    map_dimensions = (256, 256)
    height_map = np.zeros(map_dimensions+(3,), dtype=np.float32)
    for i in range(10, map_dimensions[0]-10):
        for j in range(10, map_dimensions[1]-10):
            height_map[i, j] = [0.5, 0.5, 0.5]
    for i in range(100, map_dimensions[0]-100):
        for j in range(100, map_dimensions[1]-100):
            height_map[i, j] = [1.0, 1.0, 1.0]
    return height_map
