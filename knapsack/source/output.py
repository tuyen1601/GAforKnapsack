import numpy as np
import pandas as pd
from random import randint
from knapsack.source.knapsack import Knapsack
from knapsack.source import initial_population as ipo
from knapsack.source import InputData as ip

method = 1

def optimize(weight, value, population, pop_size, num_generations, threshold, mutation_rate, crossover_rate, methods):
    parameters, fitness_history = [], []
    num_parents = int(pop_size[0]/2)
    num_offsprings = pop_size[0] - num_parents
    for i in range(num_generations):
        fitness = Knapsack.cal_fitness(weight, value, population, threshold)
        # fitness_history.append(fitness)
        if(methods == 1):
            parents = Knapsack.selection(fitness, num_parents, population)
        else:
            parents = Knapsack.RouletteSelection(fitness, 2, num_parents, population)

        offsprings = Knapsack.crossover(
            parents, num_offsprings, crossover_rate)
        mutants = Knapsack.mutation(offsprings, mutation_rate)
        population[0:parents.shape[0], :] = parents
        population[parents.shape[0]:, :] = mutants
    fitness_last_gen = Knapsack.cal_fitness(
        weight, value, population, threshold)
    max_fitness = np.where(
        fitness_last_gen == np.max(fitness_last_gen))
    parameters.append(population[max_fitness[0][0], :])
    return parameters, fitness_history, population, fitness_last_gen


def output():

    parameters, fitness_history, last_population, fitness_last_get = optimize(ip.weight, ip.value, ipo.initial_population, ipo.pop_size,
            ipo.num_generations, ip.knapsack_threshold, ip.mutation_rate, ip.crossover_rate, method)
    # print('Ket qua toi uu: \n{}'.format(parameters))
    selected_items = ip.item_number * parameters
    weight_items = np.sum(ip.weight * parameters)
    value_items = np.sum(ip.value * parameters)
    # print('\nCac vat pham se lua chon:')
    select = ''
    for i in range(selected_items.shape[1]):
        if selected_items[0][i] != 0:
            if(select != ''):
                select += ', ' + str(selected_items[0][i])
            else:
                select = str(selected_items[0][i])
    listPopulation = {}
    for i in range(last_population.shape[0]):
        item = {
            "gen": str(last_population[i]),
            "fitness": int(fitness_last_get[i]),
            "weight": int(np.sum(ip.weight * parameters))
        }
        listPopulation[i] = item
    data = {
        "selected_items": select,
        "weight": int(weight_items),
        "value": int(value_items)
    }

    # fitness_history_mean = [np.mean(fitness) for fitness in fitness_history]
    # fitness_history_max = [np.max(fitness) for fitness in fitness_history]
    # plt.plot(list(range(num_generations)), fitness_history_mean, label = 'Mean Fitness')
    # plt.plot(list(range(num_generations)), fitness_history_max, label = 'Max Fitness')
    # plt.legend()
    # plt.title('Fitness through the generations')
    # plt.xlabel('Generations')
    # plt.ylabel('Fitness')
    # plt.show()
    # print(np.asarray(fitness_history).shape)
    return fitness_history, data, listPopulation
