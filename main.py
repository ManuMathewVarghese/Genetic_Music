from music import musicGenerator,random_note,setInstruments,save_track
from geneticOperators import tournament_selection,crossover,mutation
import numpy as np
import random

np.seterr(all='raise')


# Function to play and rate tracks
def rate_music(instr_array,track) -> int:
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
mutation_rate = [0.6, 0.5, 0.6] #[mutation_rate, swap_mutation, random reset]
elite_max = 1

# To take input from users
#instruments = input("{} Select instrument number of your choice from the above list (max 9 instruments):".format(showList()))
#instr_array = list(map(int,instruments.replace(",",""))) #string to int array

#Musical Paremets
instr_array = [2,27]
setInstruments(instr_array)
notePerTrack = 20



#Population initialization
generation_ = []
for _ in range(population_size):
    chromosome = []
    for __ in range(notePerTrack):
        chromosome.append(random_note())
    generation_.append(chromosome)

best_value = []
avg_value = []
ind_array = range(0,population_size-1)
# Searching for solution till generation max is reached
for i in range(0, generation_max):
    print(f"-------------Generation: {i}-------------")
    generation = np.array(generation_)
    fitness_array = fitness(instr_array,generation)
    generation_ = next_generation(generation,fitness_array,selection_size,elite_max,crossover_rate,mutation_rate)
    x = int(input("Enter song number to save, 0 indexing(9 for none)"))
    if x in ind_array:
        save_track(generation[x],instr_array)
        print("came")

    best_value.append(np.min(fitness_array))
    avg_value.append(np.average(fitness_array))
    print(best_value,avg_value)

#CHANGE THESE names each time code runs for 10 generations
print("Just copy the above arrays to a file incase if save didn't work")
np.save("best1",best_value)
np.save("avg1",avg_value)