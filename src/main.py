# main.py

import SimulatedAnnealing as sa
import TravellingSalesmanProblem
import TSPCity
from src import CoolingRate as cr

if __name__ == "__main__":

    # Create instances of cities
    city_a = TSPCity.City("City A", 0, 0)
    city_b = TSPCity.City("City B", 1, 2)
    city_c = TSPCity.City("City C", 3, 4)
    city_d = TSPCity.City("City D", 2, 1)
    city_e = TSPCity.City("City E", 5, 5)

    # Create list of cities
    cities = [city_a, city_b, city_c, city_d, city_e]

    # Create an instance of the TSP class
    tsp = TravellingSalesmanProblem.TSP(city_a)

    # Generate a complete graph using city instances
    tsp.generate_complete_graph(cities)

    '''
    # Print the graph (optional)
    tsp.print_graph()

    # Generate a random path starting from a specific city
    starting_city = city_a
    random_path = tsp.generate_random_path(starting_city)
    print("Random path:", [city.name for city in random_path])

    # Calculate the length of the random path
    length_random_path = tsp.calculate_path_length(random_path)
    print("Length of the random path:", length_random_path)

    # Remove a city from the graph
    tsp.remove_city(city_b)

    # Calculate a new random path after removing a city
    updated_random_path = tsp.generate_random_path(starting_city)
    print("New random path after removal:", [city.name for city in updated_random_path])

    # Calculate the length of the new random path
    length_updated_random_path = tsp.calculate_path_length(updated_random_path)
    print("Length of the new random path:", length_updated_random_path)
    '''

    initial_temperature = 100
    max_iterations = 3000

    cooling_rate = cr.get_cooling_rate(initial_temperature, max_iterations)

    result_path = sa.simulated_annealing(tsp, cooling_rate)
    print("Result path:", [city.name for city in result_path])

    length_result_state = tsp.calculate_path_length(result_path)
    print("Length of the result path:", length_result_state)