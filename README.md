# Simulated Annealing and TSP

Project for Artificial Intelligence Exam @ Unifi - Simulated Annealing Algorithm implementation and application to the Travelling Salesman Problem.

### What it does

In this repository you'll find the implementation of the Simulated Annealing algorithm (_R&N 2009 §4.1.2 simpler version_) 
and its application to the Travelling Salesman Problem 
(_Thermodynamical Approach to the Traveling Salesman Problem: An Efficient Simulation Algorithm_ _- V. Černý 1985_).
It's a Monte Carlo algorithm that finds approximate solutions of the TSP.
The algorithm proceeds by creating permutations of stations randomly.
These new paths are evaluated according to their total length: if the new path is shorter, it is accepted without hesitation, 
otherwise it is accepted with a probability that follows the Boltzmann-Gibbs distribution. 
The algorithm turns out to work, although it is not demonstrated with theorems and proofs, but is shown through several examples 
(you may also refer to the original paper: http://dx.doi.org/10.1007/BF00940812).

### Files

- **TravellingSalesmanProblem.py:** class that implements the TSP, it contains all the attributes and methods needed to create the stations and paths 
(an incidence matrix D is used whose elements D(i,j) represent the weight of the edge from node i to node j)
- **SimulatedAnnealing.py:** it contains the function that implements the algorithm, which uses: 
a function to get the initial state (the random start path), a function to get the next state (a new path created with a permutation of the current path's stations), 
a function to calculate the value of the state (the length of the path) and a function to get the cooling rate (the temperature)
- **CoolingRate.py:** it gives the temperature values, which goes down as the iterations continue; 
the temperature can have various trends regardless of the most suitable mathematical function
- **matrix1.py:** it contains the matrix used for the test
- **main.py:** ...

### How to run

The program, given a particular TSP (i.e. a matrix), has many parameters for execution: the cooling type, any associated parameters, 
the initial temperature, the maximum number of iterations and the number of trials. 
All these parameters can be changed by accessing the file main.py (commands to set these parameters directly from the terminal are currently being implemented).
The program can be run from an IDE, by simply opening the folder containing all the files and running the main.py file, 
otherwise it can be run from a terminal using the command:
```
python main.py
```
No special libraries are currently required (math, random, time and copy are standard python libraries).

### Example

To test the algorithm we use the matrix which is contained in the input file matrix1.py.
The parameters used for the test runs are: cooling_type = 'exponential', decay_rate_input = 0.7,
initial_temperature = 10000, max_iterations = 100.
Several trials are performed.
