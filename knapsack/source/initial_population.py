import knapsack.source.InputData as ipd 
import numpy as np

num_generations = 1000
solutions_per_pop = 100
initial_population = None
pop_size = None

def initialPopulation():
    global pop_size, solutions_per_pop, initial_population
    pop_size = (solutions_per_pop, ipd.item_number.shape[0])
    initial_population = np.random.randint(2, size = pop_size)
    initial_population = initial_population.astype(int)
    population = initial_population.tolist()
    
    return population