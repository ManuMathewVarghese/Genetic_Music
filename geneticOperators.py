import random
from music import random_note

# Selection(Tournament Selection)
def tournament_selection(generation,fitness,selection_size) -> list:
    indices = random.sample(range(0,len(generation)-1),selection_size)
    parent = [chr for chr,_ in sorted(zip(generation[indices],fitness[indices]),key= lambda x:x[1],reverse=True)][0]
    return parent


# Crossover(Two point crossover)
def crossover(p1, p2) -> (list,list):
    index1 = random.randint(0,len(p1)-2)
    index2 = random.randint(index1+1,len(p1)-1)
    tmp = p1[index1:index2]
    p1[index1:index2] = p2[index1:index2]
    p2[index1:index2] = tmp
    return p1,p2

# Mutation (random reset and swap mutation)
def mutation(p,mutation_rate) -> list:
    index1 = random.randint(0, len(p) - 1)
    index2 = random.randint(0, len(p) - 1)

    #swap mutation
    if mutation_rate[1] > random.random():
        item = random.randint(0, 3) #choosing one of the four value i.e; channel,pitch,time,duration
        tmp = p[index1,item]
        p[index1,item] = p[index2,item]
        p[index2,item] = tmp

    #random reset
    if mutation_rate[2] > random.random():
        item = random.randint(0, 3)  #choosing one of the four value
        p[index1, item] = random_note()[item]
    return p
