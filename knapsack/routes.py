from flask import render_template, request, jsonify
from knapsack.app import app
from knapsack.source import InputData as ip
from knapsack.source import initial_population as inp
from knapsack.source import output


@app.route("/", methods=['POST', 'GET'])
def index():

    return render_template("index.html")


@app.route("/input-data", methods=['POST'])
def inputData():
    ip.max_value = request.form.get('max_value', type=int)
    ip.min_value = request.form.get('min_value', type=int)
    ip.max_weight = request.form.get('max_weight', type=int)
    ip.min_weight = request.form.get('min_weight', type=int)
    ip.number_item = request.form.get('number_items', type=int)
    item = ip.create_data()
    item = {i: item[i] for i in range(0, len(item), 1)}
    return item


@app.route("/create-initial-population", methods=['POST'])
def create():
    inp.solutions_per_pop = request.form.get('population_size', 100, type=int)
    ip.knapsack_threshold = request.form.get('threshold', 35, type=int)*2
    population = inp.initialPopulation()
    population = {i: population[i] for i in range(0, len(population), 1)}
    return population


@app.route("/start", methods=['POST'])
def start():
    ip.crossover_rate = request.form.get('crossover', 0.01, type=float)
    ip.mutation_rate = request.form.get('mutation', 0.01, type=float)
    output.num_generations = request.form.get('interaction', 1000, type=int)
    output.method = request.form.get('method', 2, type=int)
    chart, data, last_population = output.output()

    result = {
        "parameter": data,
        "last_population": last_population
    }
    return result
