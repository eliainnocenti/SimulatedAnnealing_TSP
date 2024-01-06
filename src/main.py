# main.py

# files.py
import SimulatedAnnealing as sa
import TravellingSalesmanProblem
import CoolingRate as cr
from matrix1 import matrix1

# modules
#import numpy as np # FIXME
import time
#import sys


# TODO - implement
def read_matrix_from_file(file_path):
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            matrix = np.array([list(map(int, line.split()))] for line in lines])
            return matrix
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    """
    return None


if __name__ == "__main__":

    # TODO - implement
    '''
    if len(sys.argv) > 1:
        first_argument = sys.argv[1]
        if first_argument == 'matrix1':
            settings = 'default'
        elif first_argument == 'random' and len(sys.argv) == 3:
            N = int(sys.argv[2])
            #matrix = np.random.random((N,N)) # FIXME
            #np.fill_diagonal(matrix,0) # FIXME
        elif first_argument.endswith('.py'):
            matrix = read_matrix_from_file(first_argument) # FIXME
            if matrix.shape[0] != matrix.shape[1]:
                print('') # ...
                sys.exit()

        else:
            print('') # ...
    else:
        #print('')
        # momentaneamente:
        settings = 'default'
    '''

    settings = 'default'

    if settings == 'default':
        N = 10
        matrix = matrix1
        cooling_type = 'exponential'
        decay_rate_input = 0.7
        initial_temperature = 10000
        max_iterations = 100
        n_trials = 1000

    tsp = TravellingSalesmanProblem.TSP(N)

    tsp.set_matrix(matrix1)

    cooling_rate = cr.get_cooling_rate(initial_temperature, max_iterations, cooling_type, decay_rate = decay_rate_input)

    paths = []
    lengths = []

    for i in range(n_trials):
        print(str(i), end='\r', flush=True)
        time.sleep(0.001)
        result_path = sa.simulated_annealing(tsp, cooling_rate)
        paths.append(tsp.get_path())
        #tsp.print_path()
        lengths.append(tsp.get_distance())

    dict = {}

    for length, path in zip(lengths, paths):
        if length in dict:
            dict[length].append(path)
        else:
            dict[length] = [path]

    '''
    l = list(set(lengths))
    l.sort()
    for j in range(len(l)):
        print('n path with length = ' + str(l[j]) + ': ' + str(len(dict[l[j]])))
    '''

    min_length = min(lengths)
    set_min_length = []
    for path in dict[min_length]:
        if path not in set_min_length:
            set_min_length.append(path)
    print('Minimun length: ', min_length)
    print('Paths: ')
    print(set_min_length)
    print('')