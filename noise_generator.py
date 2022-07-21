from copy import deepcopy
from PIL import Image
import random

from requests import get

ROWS = 20
COLUMNS = 20
FLOOR = "0"
WALL = "1"

def generate(x, y, density):
    matrix = generate_matrix(x, y)

    return generate_noise(matrix, density)

def generate_matrix(rows, columns):
    return  [[FLOOR for _ in range(columns)] for _ in range(rows)]

def show(matrix):
    for row in matrix:
        print(" ".join(row))

def get_matrix_dimensions(matrix):
    x = len(matrix) - 1
    y = len(matrix[0]) - 1

    return x, y

def generate_noise(matrix, density =50):
    new_matrix = deepcopy(matrix)
    rows, columns = get_matrix_dimensions(new_matrix)

    for x in range(rows + 1):
        for y in range(columns + 1):
            add_noise = random.randint(1, 100) <= density

            if add_noise:
                new_matrix[x][y] = WALL
            else:
                new_matrix[x][y] = FLOOR
  
    return new_matrix

def get_adjacent_positions(x, y):
    """
    DLT TOP DRT
    LFT POS RGT
    DLB BTM DRB
    """

    dlt = x - 1, y - 1
    top = x - 1, y
    drt = x - 1, y + 1
    left = x, y - 1
    right = x, y + 1
    dlb = x + 1, y - 1
    down = x + 1, y
    drb = x + 1, y + 1

    return dlt, top, drt, left, right, dlb, down, drb

def is_within_boundary(matrix, x, y):
    if x < 0 or y < 0:
        return False
    else:
        rows, columns = get_matrix_dimensions(matrix)
        return x <= rows and y <= columns

def get_valid_adjacent_positions(matrix, x, y):
    adjacent_positions = get_adjacent_positions(x, y)
    return [(x, y) for (x, y) in adjacent_positions if is_within_boundary(matrix, x, y)]


