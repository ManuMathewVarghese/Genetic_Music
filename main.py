#please read readme.md

from music import musicGenerator,random_note,setInstruments
from geneticOperators import tournament_selection,crossover,mutation
from instruments import showList
import numpy as np
import random

np.seterr(all='raise')


# Function to play and rate tracks
def rate_music(instr_array,track) -> int:
    '''
    Function to take user rating as input
    '''
    musicGenerator(instr_array, track)
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
def fitness(instr_array,generation) -> np.ndarray:
    fitness = np.full(len(generation),-1)
    unique = np.unique(generation,return_inverse=True,axis=0)
    unique_indices = unique[1]
    for i,chromosome in enumerate(generation):
        if fitness[i] == -1:
            fit = rate_music(instr_array,chromosome)
            fitness[np.where(unique_indices==unique_indices[i])] = fit
        else:
            print("Music already rated")
    return fitness





# Generating new generation
def next_generation(generation,fitness_array,selection_size,elite_max,crossover_rate,mutation_rate) -> list:
    '''
    Elitism: Best track from one generation are copied to the next generation.
    Selection: Tournament selection
    Incest_check: If all the tracks in a population are similar, randomly selected tracks are forced to mutate.
    Crossover: Recombination of two tracks
    Mutation: 1. Swap mutation: Swaps values of notes in a track. 2. Random reset: Varies values in a note randomly.
    '''
    next_gen = []

    # Elitism
    elite = [chr for chr,_ in sorted(zip(generation,fitness_array),key= lambda x:x[1],reverse=True)][:elite_max]
    for chromosome in elite:
        next_gen.append(chromosome)

    #selection
    while True:
        c1 = tournament_selection(generation, fitness_array,selection_size)
        c2 = tournament_selection(generation, fitness_array,selection_size)

        #Mutation
        if mutation_rate[0] > random.random():
            c1 = mutation(c1, mutation_rate)
        if mutation_rate[0] > random.random():
            c2 = mutation(c2, mutation_rate)

        #Crossover
        if crossover_rate > random.random():
            count = 0

            #incest check
            while True:
                if count == len(generation)-1:
                    mutation(c1,mutation_rate)
                    break
                elif (np.array(c1) == np.array(c2)).all():
                    c2,count = tournament_selection(generation, fitness_array,selection_size),count+1
                else:
                    c1, c2 = crossover(c1, c2)
                    break

        if len(next_gen) < population_size:
            next_gen.append(c1)
        elif len(next_gen) < population_size:
            next_gen.append(c2)
        else:
            break

    return next_gen



# Genetic parameters
population_size = 6
generation_max = 10
selection_size = 2
crossover_rate = 0.8
mutation_rate = [0.6, 0.5, 0.6] #[mutation_rate, swap rate, reset rate]
elite_max = 1

# To take input from users
print("{} Select instrument number of your choice from the above list (max 9 instruments):".format(showList()))
instr_array = []
for i in range(1,10):
    instr_array.append(int(input(f'Enter instrument number {i}, (0 to finish):')))
    if instr_array[-1] == 0: break
#instr_array = list(map(int,instruments.replace(",",""))) #string to int array
print(instr_array)
setInstruments(instr_array)

#Music Paremeters
notesPerTrack = 25



#Population initialization
generation_ = []
for _ in range(population_size):
    chromosome = []
    for __ in range(notesPerTrack):
        chromosome.append(random_note())
    generation_.append(chromosome)


best_value = []
avg_value = []

# Searching for solution till generation max is reached
for i in range(0, generation_max):
    print(f"-------------Generation: {i}-------------")
    generation = np.array(generation_)
    fitness_array = fitness(instr_array,generation)
    generation_ = next_generation(generation,fitness_array,selection_size,elite_max,crossover_rate,mutation_rate)

    # best_value.append(np.max(fitness_array))
    # avg_value.append(np.average(fitness_array))
    # print(best_value,avg_value)
