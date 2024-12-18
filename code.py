import math
import random

# GLOBAL DECLARATIONS
population = {"chromosomes": [], "fitness": []}  # Random population

new_population = {"chromosomes": [], "fitness": []}  # Engineered population

best_chromosome = {"generation": [], "chromosome": [], "fitness": []}

# Initialize interval boundaries for x and y
interval_x = [-5, 5]
interval_y = [-5, 5]

# Population size
num_chromosomes = 10
num_genes = 10
num_generations = 10

# Probabilities for genetic operations (crossover and mutation)
prob_crossover = 0.8
prob_mutation = 0.01

# Generate random chromosome
def generate_random_chromosome(num_genes):
    chromosome = []
    for _ in range(num_genes):
        chromosome.append(random.randint(0, 1))
    return chromosome


# Create population to hold chromosomes
def create_population(num_chromosomes, num_genes, population):
    for _ in range(num_chromosomes):
        population["chromosomes"].append(generate_random_chromosome(num_genes))


# Function to evaluate
def function(x, y):
    return (math.cos(x) + math.sin(y)) ** 2 / (x**2 + y**2)


# Decode chromosome using binary decoding
def decode_chromosome(chromosome, interval):
    numerator = 0
    denominator = 0
    for i, gene in enumerate(chromosome):
        numerator += gene * (2 ** -(i + 1))
        denominator += 2 ** -(i + 1)
    return interval[0] + (((interval[1] - interval[0]) / denominator) * numerator)


# Split array into two gametes: x and y
def split_chromosome(chromosome):
    mid = len(chromosome) // 2
    return chromosome[:mid], chromosome[mid:]


# Calculate fitness value
def calculate_fitness(value):
    epsilon = 1e-10
    return 1 / (value + epsilon)


# Calculate fitness for the population
def evaluate_population_fitness(population):
    population["fitness"] = []
    for chromosome in population["chromosomes"]:
        x, y = split_chromosome(chromosome)
        decoded_x = decode_chromosome(x, interval_x)
        decoded_y = decode_chromosome(y, interval_y)
        fitness_value = function(decoded_x, decoded_y)
        population["fitness"].append(calculate_fitness(fitness_value))


# Select parents using roulette wheel selection
def roulette_wheel_selection(population):
    total_fitness = sum(population["fitness"])
    selection_point = random.random()
    cumulative_probability = 0
    for i, fitness in enumerate(population["fitness"]):
        cumulative_probability += fitness / total_fitness
        if selection_point < cumulative_probability:
            return population["chromosomes"][i]


# Perform single-point crossover
def crossover(parent1, parent2, probability):
    if random.random() < probability:
        crossover_point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
    else:
        child1, child2 = parent1, parent2
    return child1, child2


# Perform mutation
def mutate(chromosome, probability):
    for i in range(len(chromosome)):
        if random.random() <= probability:
            chromosome[i] = 1 - chromosome[i]
    return chromosome


# Perform elitism selection
def elitism_selection(population, new_population):
    if not population["fitness"] or not population["chromosomes"]:
        return new_population

    best_indices = sorted(
        range(len(population["fitness"])),
        key=lambda i: population["fitness"][i],
        reverse=True,
    )[:2]
    for idx in best_indices:
        new_population["chromosomes"].append(population["chromosomes"][idx])
        new_population["fitness"].append(population["fitness"][idx])
    return new_population


# MAIN PROGRAM
# Generational Model for Generation Replacement
create_population(num_chromosomes, num_genes, population)
evaluate_population_fitness(population)

generation = 1
while generation <= num_generations:
    new_population = {"chromosomes": [], "fitness": []}

    # Display population table
    print(f">>>> POPULATION GENERATION {generation} <<<<\n")
    print("-" * 120)
    print(
        "No.\t| {:<33}{:<3}{:<22}{:<3}{:<22}{:<3}{:<22}".format(
            "Chromosome", "|", "Phenotype x", "|", "Phenotype y", "|", "Fitness Value"
        )
    )
    print("-" * 120)

    for i, chromosome in enumerate(population["chromosomes"]):
        x, y = split_chromosome(chromosome)
        print(
            f"{i + 1}\t| {chromosome} | {decode_chromosome(x, interval_x):<22} | {decode_chromosome(y, interval_y):<22} | {population['fitness'][i]:<22}"
        )

    print("-" * 120)
    print()

    # Select top 2 chromosomes with highest fitness
    new_population = elitism_selection(population, new_population)

    # Store best chromosome data
    best_chromosome["generation"].append(generation)
    best_chromosome["chromosome"].append(new_population["chromosomes"][0])
    best_chromosome["fitness"].append(new_population["fitness"][0])

    while len(new_population["chromosomes"]) < num_chromosomes:
        parent1 = roulette_wheel_selection(population)
        parent2 = roulette_wheel_selection(population)

        offspring1, offspring2 = crossover(parent1, parent2, prob_crossover)

        offspring1 = mutate(offspring1, prob_mutation)
        offspring2 = mutate(offspring2, prob_mutation)

        new_population["chromosomes"].append(offspring1)
        new_population["chromosomes"].append(offspring2)

    evaluate_population_fitness(new_population)
    population = new_population
    generation += 1

# Display best chromosome per generation
print("BEST CHROMOSOME WITH MINIMUM FUNCTION VALUE IN EACH GENERATION\n")
print("-" * 122)
print(
    "{:<16}{:<3}{:<31}{:<3}{:<22}{:<3}{:<22}{:<3}{:<22}".format(
        "Generation",
        "|",
        "Chromosome",
        "|",
        "Phenotype x",
        "|",
        "Phenotype y",
        "|",
        "Fitness Value",
    )
)
print("-" * 122)

for i in range(len(best_chromosome["generation"])):
    x, y = split_chromosome(best_chromosome["chromosome"][i])
    print(
        f"{best_chromosome['generation'][i]}\t\t| {best_chromosome['chromosome'][i]} | {decode_chromosome(x, interval_x):<22} | {decode_chromosome(y, interval_y):<22} | {best_chromosome['fitness'][i]:<22}"
    )

print("-" * 122)

# Find the generation with the best solution
best_fitness = max(best_chromosome["fitness"])
best_index = best_chromosome["fitness"].index(best_fitness)

# Display the best solution
print(
    f"\nThe best chromosome in the population is {best_chromosome['chromosome'][best_index]}"
)
print(
    f"with a fitness value of {best_fitness}, found in generation {best_chromosome['generation'][best_index]}"
)

best_x, best_y = split_chromosome(best_chromosome["chromosome"][best_index])
decoded_x = decode_chromosome(best_x, interval_x)
decoded_y = decode_chromosome(best_y, interval_y)
print(f"Value of x: {decoded_x}")
print(f"Value of y: {decoded_y}")
print(f"Function result: {function(decoded_x, decoded_y)}")
