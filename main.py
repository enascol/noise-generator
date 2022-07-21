import automata
import convert_to_image
import noise_generator
import time
import sys


print(sys.argv)
rows, columns, density, iterations = sys.argv[1:]
matrix = noise_generator.generate(int(rows), int(columns), int(density))
automata.run(matrix, int(iterations), True)
