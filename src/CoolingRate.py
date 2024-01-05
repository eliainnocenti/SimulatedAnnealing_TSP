# ...

import math


def linear_cooling(initial_temperature, iteration, max_iterations):
    return initial_temperature * (1 - iteration / float(max_iterations))


def exponential_cooling(initial_temperature, iteration, decay_rate):
    return initial_temperature * (decay_rate ** iteration)


def logarithmic_cooling(initial_temperature, iteration, factor):
    return initial_temperature / math.log(iteration + factor)


def geometric_cooling(initial_temperature, iteration, alpha):
    return initial_temperature * alpha / (1 + alpha * (iteration - 1))


def boltzmann_cooling(initial_temperature, iteration):
    return initial_temperature / math.log(1 + iteration)


def get_cooling_rate(initial_temperature, max_iterations, cooling_type='linear', **kwargs):
    if cooling_type == 'linear':
        return [linear_cooling(initial_temperature, t, max_iterations) for t in range(1, max_iterations + 1)]
    elif cooling_type == 'exponential':
        decay_rate = kwargs.get('decay_rate', 0.9)
        return [exponential_cooling(initial_temperature, t, decay_rate) for t in range(1, max_iterations + 1)]
    elif cooling_type == 'logarithmic':
        factor = kwargs.get('factor', 1)
        return [logarithmic_cooling(initial_temperature, t, factor) for t in range(1, max_iterations + 1)]
    elif cooling_type == 'geometric':
        alpha = kwargs.get('alpha', 0.9)
        return [geometric_cooling(initial_temperature, t, alpha) for t in range(1, max_iterations + 1)]
    elif cooling_type == 'boltzmann':
        return [boltzmann_cooling(initial_temperature, t) for t in range(1, max_iterations + 1)]
    else:
        raise ValueError("Invalid cooling type")