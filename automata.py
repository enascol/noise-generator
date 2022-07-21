import noise_generator as ng
from copy import deepcopy

import convert_to_image as cti

import time

THRESHOLD = 4


def run(matrix, iterations =1, show_evolution =False):
    for x in range(iterations):
        automata(matrix)
        
        if show_evolution:
            cti.convert(matrix)
    return matrix

def automata(matrix):
    temp_grid = deepcopy(matrix)
    rows, columns = ng.get_matrix_dimensions(temp_grid)
    for x in range(rows + 1):
        for y in range(columns + 1):
            t = transform_tile(temp_grid, x, y)
            matrix[x][y] = t
    
    return matrix

def get_adjacent_values(matrix, x, y):
    valid_positions = ng.get_valid_adjacent_positions(matrix, x, y)
    floors, walls = 0, 0

    for x, y in valid_positions:
        if matrix[x][y] == ng.FLOOR:
            floors += 1
        elif matrix[x][y] == ng.WALL:
            walls += 1
        else:
            raise ValueError(f"Invalid tile {matrix[x][y]} at position ({x}, {y})")
    
    if (floors + walls) < 8:
        walls = walls + (8 - len(valid_positions))
    
    return floors, walls
    
def transform_tile(base, x, y):
    _, adjacent_walls_value = get_adjacent_values(base, x, y)

    if adjacent_walls_value > THRESHOLD:
        return ng.WALL
    else:
        return ng.FLOOR