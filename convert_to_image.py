from copy import deepcopy
from multiprocessing.sharedctypes import Value
from PIL import Image

import random
import noise_generator
import numpy as np

WALL_BG = (36, 36, 36)
FLOOR_BG = (191, 191, 191)

def get_random_color(base=(None, None, None)):
    r, g, b = base
    
    if not r: r = random.randint(0, 255)
    if not b: b = random.randint(0, 255)
    if not g: g = random.randint(0, 255)

    return r, g, b

def convert(matrix):
    base = deepcopy(matrix)
    rows, columns = noise_generator.get_matrix_dimensions(base)

    for x in range(rows + 1):
        for y in range(columns + 1):
            pixel = base[x][y]

            if pixel == noise_generator.WALL:
                base[x][y] = WALL_BG
            else:
                base[x][y] = FLOOR_BG

    numpy_matrix = np.asarray(base, dtype=np.uint8)
    img = Image.fromarray(numpy_matrix)
    img.save("hiii.png")
