import numpy as np
import random as rd
from random import randint
import json

number_item = 10
min_weight = 1
max_weight = 15
min_value = 10
max_value = 750
knapsack_threshold = 35  # Can nang cua cai tui
crossover_rate = 0.10
mutation_rate = 0.01
item_number = None
weight = None
value = None


def create_data():
    global item_number, weight, value
    item_number = np.arange(1, number_item + 1)
    weight = np.random.randint(min_weight, max_weight, size=number_item)
    value = np.random.randint(min_value, max_value, size=number_item)
    listItem = []

    for i in range(item_number.shape[0]):
        item = {
            "id": int(item_number[i]),
            "weight": int(weight[i]),
            "value": int(value[i])
        }
        listItem.append(item)
    # listItem.tolist()
    # List= json.dumps(listItem, cls=NumpyEncoder)
    return listItem
