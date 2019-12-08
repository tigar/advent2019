from aoc import file_reader
import sys
import collections
import numpy as np

data = file_reader('day8')
data = data[0]

def solve(width, height):
    num_pixels = width*height
    num_layers = len(data) // num_pixels

    min_zero = sys.maxsize
    ans = 0
    picture = data
    # brute force
    while picture:
        cur_layer = picture[:width*height]
        picture = picture[width*height:]

        num_zero = cur_layer.count('0')
        if num_zero < min_zero:
            min_zero = num_zero
            ans = cur_layer.count('1')*cur_layer.count('2')
    print("Part 1 :", ans)


solve(25, 6)