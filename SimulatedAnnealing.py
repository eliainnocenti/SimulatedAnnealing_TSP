# implementation of the Simulated Annealing algorithm (R&N 2009 §4.1.2 simpler version)

import random
import math

import random
import math


def simulated_annealing(problem, cooling_rate):
    current_state = problem.get_initial_state()  # Set the initial state

    for t in range(1, float('inf')):  # Loop indefinitely (until a condition is met)
        temperature = cooling_rate[t]  # Get the current temperature

        if temperature == 0:  # If temperature reaches 0, return the current state
            return current_state

        next_state = problem.get_random_successor(current_state)  # Get a random successor state
        delta_E = problem.calculate_value(current_state) - problem.calculate_value(
            next_state)  # Calculate energy difference

        if delta_E > 0:  # If the new state is better, accept it
            current_state = next_state
        else:
            # If the new state is worse, accept it with a certain probability based on temperature
            probability = math.exp(-delta_E / temperature)
            if random.random() < probability:
                current_state = next_state
