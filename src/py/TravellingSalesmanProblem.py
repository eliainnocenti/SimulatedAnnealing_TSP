# TravellingSalesmanProblem.py

import random
import copy


class TSP:

    def __init__(self, N):
        self.D = [[0 for _ in range(N)] for _ in range(N)]
        self.N = N
        self.d = 0
        self.d_trial = 0
        self.i = 1
        self.s = [0 for _ in range(N)]
        self.c = [0 for _ in range(N)]
        self.t = [0 for _ in range(N)]

    def set_matrix(self, matrix):
        self.D = copy.deepcopy(matrix)

    def get_initial_state(self):
        self.s = list(range(0, self.N))
        random.shuffle(self.s)
        self.c = self.s.copy()
        return self.c

    def get_random_successor(self):
        j = self.i
        while j == self.i:
            j = random.randint(1, self.N)
        i_tilde = min(self.i, j)
        j_tilde = max(self.i, j)
        for k in range(1, self.i-1+1):
            self.t[k-1] = self.c[k-1]
        for l in range(0, j_tilde-i_tilde+1):
            self.t[i_tilde+l-1] = self.c[j_tilde-l-1]
        for w in range(j_tilde+1, self.N+1):
            self.t[w-1] = self.c[w-1]
        return self.t

    def calculate_value(self):
        self.d = self.D[self.c[self.N-1]][self.c[0]]
        for k in range(0, self.N-2):
            self.d += self.D[self.c[k]][self.c[k+1]]
        return self.d

    def calculate_value_trial(self):
        self.d_trial = self.D[self.t[self.N-1]][self.t[0]]
        for k in range(0, self.N-2):
            self.d_trial += self.D[self.t[k]][self.t[k + 1]]
        return self.d_trial

    def set_state(self):
        self.c = self.t.copy()
        self.d = self.d_trial

    def increase_i(self):
        self.i += 1
        if self.i > self.N:
            self.i = 1

    def print_path(self):
        print('Path: ')
        for element in self.c:
            print(element, end=' ')
        print('distance: ' + str(self.d) + '\n')

    def has_duplicates(self):
        seen = set()
        for el in self.t:
            if el in seen:
                return True
            seen.add(el)
        return False

    def get_distance(self):
        return self.d

    def get_path(self):
        return self.c

    def calculate_value_path(self, path):
        n = len(path)
        length = self.D[path[n-1]][path[0]]
        for k in range(0, n-2):
            length += self.D[path[k]][path[k+1]]
        return length