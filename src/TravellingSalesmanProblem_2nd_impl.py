# ...

import random
import math


class TSP:

    def __init__(self, starting_city):
        self.graph = {}
        self.initial_state = starting_city

    def add_edge(self, city1, city2, distance, add=True):
        if city1 not in self.graph:
            self.graph[city1] = {}
        if city2 not in self.graph:
            self.graph[city2] = {}

        if add:
            self.graph[city1][city2] = distance
            self.graph[city2][city1] = distance
        elif city2 in self.graph[city1]:
            del self.graph[city1][city2]
            del self.graph[city2][city1]

    @staticmethod
    def euclidean_distance(city1, city2):
        return math.sqrt((city2.x - city1.x) ** 2 + (city2.y - city1.y) ** 2)

    @staticmethod
    def manhattan_distance(city1, city2):
        return abs(city2.x - city1.x) + abs(city2.y - city1.y)

    def calculate_distance(self, city1, city2, distance_type='euclidean'):
        if distance_type == 'euclidean':
            return self.euclidean_distance(city1, city2)
        elif distance_type == 'manhattan':
            return self.manhattan_distance(city1, city2)
        else:
            raise ValueError("Invalid distance type")

    def generate_complete_graph(self, cities):
        for i in range(len(cities)):
            for j in range(i + 1, len(cities)):
                distance = self.calculate_distance(cities[i], cities[j])
                self.add_edge(cities[i], cities[j], distance)

    def add_city_complete_graph(self, new_city, existing_cities):
        for city in existing_cities:
            distance = self.calculate_distance(new_city, city)
            self.add_edge(new_city, city, distance)

    def remove_city(self, city):
        if city in self.graph:
            del self.graph[city]
            for other_city in self.graph:
                if city in self.graph[other_city]:
                    del self.graph[other_city][city]

    def calculate_path_length(self, path):
        if len(path) == 1:
            return float('inf')

        total_distance = 0
        for i in range(len(path) - 1):
            city1 = path[i]
            city2 = path[i + 1]
            if city1 in self.graph and city2 in self.graph[city1]:
                total_distance += self.graph[city1][city2]
            else:
                pass
        return total_distance

    def generate_random_path(self, starting_city):
        cities = list(self.graph.keys())
        cities.remove(starting_city)
        random.shuffle(cities)
        path = [starting_city] + cities + [starting_city]
        return path

    def get_initial_state(self):
        path = list()
        path.append(self.initial_state)
        return path

    def get_random_successor(self, city):
        return self.generate_random_path(self.initial_state)  # FIXME

    def calculate_value(self, path):
        return self.calculate_path_length(path)

    def print_graph(self):
        for node in self.graph:
            city_info = str(node)
            print(city_info)
