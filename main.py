from instruments import showList
from music import setInstruments,musicEngine,musicGenerator
import numpy as np
import random


def rate_music(instr_array,chromosome):
    print(instr_array,chromosome)
    musicGenerator(instr_array, chromosome)
    while True:
        try:
            rate = int(input("Rate the music (0-10): "))
        except ValueError:
            print("That\'s not a number")
        else:
            if 0 <= rate < 11:
                break
            else:
                print("Enter a number between 1 to 10")

    return rate


# Calculating the fitness of a chromosome
def c_fitness(instr_array,generation):

    fitness = []
    fitness.append([rate_music(instr_array,chromosome) for chromosome in generation])
    return fitness


# Selection
def select_parent(generation, fitness_array, selection_size):
    # Implementing weighted random selection (Individuals with higher fitness has more chance)
    print(generation.shape, fitness_array.shape)
    selection = []
    inverse_fitness = max(fitness_array) - fitness_array
    probability_distribution = np.array(inverse_fitness / sum(inverse_fitness))
    selection.append(
        np.random.choice(
            generation.shape[0], selection_size, p=probability_distribution
        )
    )
    best_index = np.argmin(fitness_array[tuple(selection)])
    parent = generation[best_index, :]
    return parent


# Crossover(Single point)
def crossover(p1, p2):

    point = random.randint(1,len(p1)-1)
    print(np.vstack((p1,p2)))
    return np.vstack((p1[:point],p2[point:])), np.vstack((p2[:point],p2[point:]))

# Mutation (Either changes notes or duration)
def mutate(p):
    print("mute")
    index1 = random.randint(0, len(p) - 1)
    index2 = random.randint(0, len(p) - 1)
    item = np.random.randint(0, 2) #choosing between note and duration
    tmp = p[index1,item]
    p[index1,item] = p[index2,item]
    p[index2,item] = tmp
    return p


# # Random Extinction
# def extinction(generation, fitness_array):
#     selection = []
#     probability_distribution = np.array(fitness_array / sum(fitness_array))
#     selection.append(
#         np.random.choice(
#             generation.shape[0], random.randint(1, 10), p=probability_distribution
#         )
#     )
#     print(selection)
#     # Removing selected candidates from both generation and fitness arrays
#     n_generation = np.delete(generation, selection, axis=0)
#     n_fitness_array = np.delete(fitness_array, selection)
#     print(generation.shape, fitness_array.shape)
#     return n_generation, n_fitness_array


# Creating offspring
def children(c1, c2, crossover_rate, mutation_rate):
    if crossover_rate > random.random():
        c1, c2 = crossover(c1, c2)
    if mutation_rate > random.random():
        c1 = mutate(c1)
    if mutation_rate > random.random():
        c2 = mutate(c2)
    return c1, c2


# Generating new generation
def next_generation(
    generation,
    instr_array,
    fitness_array,
    selection_size,
    crossover_rate,
    mutation_rate,
    elite_max,
    incest_control,
    extinction_rate,
):
    next_gen = []

    # # Random extinction
    # if extinction_rate > random.random():
    #     generation, fitness_array = extinction(generation, fitness_array)

    # Elitism
    elite = generation[np.argsort(fitness_array)[:elite_max]]
    for chromosome in elite:
        next_gen.append(chromosome)

    while True:
        p1 = select_parent(generation, fitness_array, selection_size)
        p2 = select_parent(generation, fitness_array, selection_size)

        # Incest check
        if incest_control > random.random():
            while (np.array(p1) != np.array(p2)).all():
                p2 = select_parent(generation, fitness_array, selection_size)
        c1, c2 = children(p1, p2, crossover_rate, mutation_rate)
        if len(next_gen) < population_size:
            next_gen.append(c1)
        elif len(next_gen) < population_size:
            next_gen.append(c2)
        else:
            break
        # print(len(next_gen))
    return next_gen



# Defining parameters
population_size = 4
generation_max = 10
selection_size = 4
crossover_rate = 0.8
mutation_rate = 0.2
elite_max = 1
incest_control = 0.5
extinction_rate = 0.08

#instruments = input("{} Select instrument number of your choice from the above list (max 9 instruments):".format(showList()))
#instr_array = list(map(int,instruments.replace(",",""))) #string to int array
instr_array = [1,27,41]
#channel, pitch, time, duration,
pop_size = 5
tim = 4
generation_ = []
#Population initialization
for _ in range(pop_size):
    chromosome = []
    for __ in range(tim):
        channel = np.random.randint(0,len(instr_array)-1)
        pitch = np.random.randint(36,96)
        time = np.random.uniform(0.0,15.0)
        duration = np.random.uniform(0.2,3.0)
        chromosome.append([channel,pitch,time,duration])
    generation_.append(chromosome)
# First generation
best_value = []
avg_value = []
# Searching for solution till generation max is reached
for i in range(0, generation_max):
    generation = generation_
    fitness_array = np.array(c_fitness(instr_array,generation)).reshape(
        len(generation) * 1
    )
    generation_ = next_generation(
        generation,
        instr_array,
        fitness_array,
        selection_size,
        crossover_rate,
        mutation_rate,
        elite_max,
        incest_control,
        extinction_rate,
    )
    print(generation.shape,"--------------------")
    if i % 10 == 0:
        best_value.append(np.min(fitness_array))
        avg_value.append(np.average(fitness_array))
