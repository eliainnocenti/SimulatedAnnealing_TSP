# SimulatedAnnealing.py

# implementation of the Simulated Annealing algorithm (R&N 2009 §4.1.2 simpler version)

import random
import math


def simulated_annealing(problem, cooling_rate):

    current_state = problem.get_initial_state() # Set the initial state
    temperature = iter(cooling_rate)

    while True:  # Loop indefinitely (until a condition is met)

        try:
            current_temperature = next(temperature)  # Get the current temperature
        except StopIteration:
            break

        if current_temperature == 0.000001:  # If temperature reaches 0, return the current state
            return current_state

        next_state = problem.get_random_successor()  # Get a random successor state
        delta_E = problem.calculate_value() - problem.calculate_value_trial()  # Calculate energy difference

        if delta_E > 0:  # If the new state is better, accept it
            problem.set_state()
            current_state = next_state

        else:
            # If the new state is worse, accept it with a certain probability based on temperature
            probability = math.exp(delta_E / current_temperature)

            if random.random() < probability:
                problem.set_state()
                current_state = next_state

            else:
                problem.increase_i()