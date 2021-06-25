import numpy as np
import random as rd
from random import randint


class Knapsack:
    # function calculates fitness
    def cal_fitness(weight, value, population, threshold):
        fitness = np.empty(population.shape[0])
        for i in range(population.shape[0]):
            S1 = np.sum(population[i] * value)
            S2 = np.sum(population[i] * weight)
            if S2 <= threshold:
                fitness[i] = S1
            else:
                fitness[i] = 0
        return fitness.astype(float)

    def selection(fitness, num_parents, population):
        fitness = list(fitness)
        parents = np.empty((num_parents, population.shape[1]))
        x = rd.random()
        for i in range(num_parents):
            max_fitness_idx = np.where(fitness == np.max(fitness))
            parents[i, :] = population[max_fitness_idx[0][0], :]
            fitness[max_fitness_idx[0][0]] = -999999
        return parents
    
    def RouletteSelection(fitness, num_outstanding_parents,num_parents, population):
        fitness = list(fitness)
        
        parents = np.empty((num_parents, population.shape[1]))
        for i in range(num_outstanding_parents):
            max_fitness_idx = np.where(fitness == np.max(fitness))
            parents[i, :] = population[max_fitness_idx[0][0], :]
            fitness[max_fitness_idx[0][0]] = 0
        maximun = sum([fitness[i] for i in range(num_parents)])
        pick = rd.uniform(0, maximun)
        current = 0
        for i in range(num_parents - num_outstanding_parents ):
            current += fitness[i] 
            if current > pick:
                parents[i + num_outstanding_parents, :] = population[i, :]
                fitness[i] = 0
        return parents


    def crossover(parents, num_offsprings, crossover_rate):
        offsprings = np.empty((num_offsprings, parents.shape[1]))
        crossover_point = int(parents.shape[1]/2)

        i = 0
        while (parents.shape[0] < num_offsprings):
            parent1_index = i % parents.shape[0]
            parent2_index = (i+1) % parents.shape[0]
            x = rd.random()
            if x > crossover_rate:
                continue
            parent1_index = i % parents.shape[0]
            parent2_index = (i+1) % parents.shape[0]
            offsprings[i, 0:crossover_point] = parents[parent1_index,
                                                       0:crossover_point]
            offsprings[i, crossover_point:] = parents[parent2_index,
                                                      crossover_point:]
            i = +1
        return offsprings

    def mutation(offsprings, mutation_rate):
        mutants = np.empty((offsprings.shape))

        for i in range(mutants.shape[0]):
            random_value = rd.random()
            mutants[i, :] = offsprings[i, :]
            if random_value > mutation_rate:
                continue
            int_random_value = randint(0, offsprings.shape[1]-1)
            if mutants[i, int_random_value] == 0:
                mutants[i, int_random_value] = 1
            else:
                mutants[i, int_random_value] = 0
        return mutants
        
