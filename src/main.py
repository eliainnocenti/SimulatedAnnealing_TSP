# main.py

import SimulatedAnnealing as sa
import TravellingSalesmanProblem
import CoolingRate as cr
import numpy as np

if __name__ == "__main__":

    N = 10

    #matrix = np.random.randint(1, 11, size=(10, 10))

    matrix1 = [[ 0,  9,  9,  6,  7,  2,  9,  4,  1, 10],
               [ 7,  0,  2,  5,  4, 10,  3,  7,  9,  3],
               [ 4, 10,  0,  5,  6,  6,  4,  1,  3,  8],
               [ 7,  4,  2,  0, 10,  8,  4,  5,  8,  8],
               [10,  7,  9,  7,  0,  7,  8,  8,  2,  7],
               [ 8,  4,  4,  3, 10,  0,  2,  5,  8,  1],
               [ 2,  2,  2,  5,  3,  2,  0,  5, 10,  1],
               [ 3, 10,  2,  4,  9,  8,  7,  0, 10,  9],
               [ 3,  9,  8,  7,  9,  5,  3,  6,  0,  2],
               [ 9,  5, 10,  9,  2, 10,  6,  4, 10,  0]]

    tsp = TravellingSalesmanProblem.TSP(N)

    tsp.set_matrix(matrix1)

    initial_temperature = 10000000
    max_iterations = 1000

    cooling_rate = cr.get_cooling_rate(initial_temperature, max_iterations, 'exponential', decay_rate = 0.6)

    paths = []
    lengths = []

    for i in range(10000):
        result_path = sa.simulated_annealing(tsp, cooling_rate)
        paths.append(tsp.get_path())
        tsp.print_path()
        lengths.append(tsp.get_distance())

    dict = {}

    for length, path in zip(lengths, paths):
        if length in dict:
            dict[length].append(path)
        else:
            dict[length] = [path]

    min_length = min(lengths)

    #print(paths)
    #print(lengths)

    print('Minimun length: ', min_length)
    print(dict[min_length])