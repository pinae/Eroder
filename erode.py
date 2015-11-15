#!/usr/bin/env python
# coding=utf-8
from __future__ import division, print_function, unicode_literals

neighbours = [(-1, -1), (0, -1), (1, -1), (1, 0),
              (1, 1), (0, 1), (-1, 1), (-1, 0)]


def single_drop(x, y, height_map, amount_map, sediment=0.0):
    height = height_map[x, y, 0]
    min_n = (0, 0)
    min_n_h = height
    for n in neighbours:
        if 0 <= x + n[0] < height_map.shape[0] and \
           0 <= y + n[1] < height_map.shape[1]:
            n_h = height_map[x + n[0], y + n[1], 0]
            if n_h < min_n_h:
                min_n_h = n_h
                min_n = n
    if min_n_h < height and \
       0 <= x + min_n[0] < height_map.shape[0] and \
       0 <= y + min_n[1] < height_map.shape[1]:
        amount = max(0.3, amount_map[x, y])
        amount_map[x, y] = amount
        steepness = height - height_map[x + min_n[0], y + min_n[1], 0]
        material = amount * min(0.05, steepness) - sediment
        height_map[x, y, 0] = max(height_map[x, y, 0] - material, 0.0)
        height_map[x, y, 1] = height_map[x, y, 0]
        height_map[x, y, 2] = height_map[x, y, 0]
        if amount_map[x + min_n[0], y + min_n[1]] == 0:
            single_drop(x + min_n[0], y + min_n[1],
                        height_map, amount_map, max(0, material))
    return height_map, amount_map


if __name__ == "__main__":
    print("not finished")
