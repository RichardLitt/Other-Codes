"""
Oliphaunt creates an initial population of random agents with and evolves this
population over a number of generations, printing total fitness at each
generation. Fitness is calculated after a certain number of random interactions
among the population and is determined by the proportion of successful 'sends' 
and successful 'receives' each scaled by a weighting factor. Parents are 
selected with a probability proportional to their fitness and there is a chance
of mutation of each weight in the vocabulary. simulation returns
the final population.
"""
#This allows use of the random module, which will be accessed throughout.
import random 

#Calls up a row of signals that are equivalent to one meaning in the Signal-Meaning matrix.
def m_weights(system, signal):
    weights = []
    for m in system:
        weights.append(m[signal])
    return weights

#Calls up a column of mulitple meanings corresponding to one signal in the S-M matrix.
def s_weights(system, meaning):
    return system[meaning]

#Finds the item of the highest weight or value in a list (used for searching s_ and m_weights.)
#Determines which signal/meaning should be called for it's corresponding meaing/signal.
def wta(items):
    maxweight = max(items)
    candidates = []
    for i in range(len(items)):
        if items[i] == maxweight:
            candidates.append(i)
    return random.choice(candidates)

#Added recall of sending/recieving matrix for each agent.
def communicate(system1, system2, meaning):
    system1s = system1[0]
    system2r = system2[1]
    #print(system1s, system2r)
    signal = wta(s_weights(system1s, meaning))
    if wta(m_weights(system2r, signal)) == meaning:
        return 1
    else:
        return 0

#This updates chooses which agents to communicate, and then has them do so.
#It then adds the statistics for each agent, adding the output of communicate().
#This function is responsible for determining an agent's fitness.
def pop_update(population):
    s = random.randrange(len(population))
    h = random.randrange(len(population) - 1) 
    if h >= s: 
        h += 1     
    speaker = population[s]
    hearer = population[h]
    meaning = random.randrange(len(speaker[0]))
    success = communicate(speaker, hearer, meaning)
    #The following segment can be modified to change benefit to speaker or hearer.
    speaker[2][0] += success #Setting this to 0 gives no benefit to speaker.
    speaker[2][1] += 1
    hearer[2][2] += success #Setting this to 0 gives no benefit to hearer.
    hearer[2][3] += 1
    return population

#Importing deepcopy, which actually produces a new version.
from copy import deepcopy

#These are values that can be adjusted to manipulate the game.
#Changing the values of send_- and receive_fitness has the same effect as zeroing out the values
#in pop_update, but here's it is possible to give some differing levels of benefit for speaking or hearing.
mutation_rate = 0.01   # probability of mutation per weight
mutation_max = 1       # maximum value for a weight
send_fitness = 5       # weighting factor for send score  
receive_fitness = 5    # weighting factor for receive score
meanings = 2           # number of meanings
signals = 2            # number of signals
interactions = 5000    # number of interactions per generation
size = 100             # size of population
output_file = 'oliphaunt.csv' # file to output population fitness

#This takes the states from pop_update() and determines a value of fitness,
#by dividing the number of successful iterations with the total number of iterations.
def fitness(agent):
    s = agent[2][0]
    sn = agent[2][1]
    r = agent[2][2]
    rn = agent[2][3]
    if sn == 0: 
        sn = 1
    if rn == 0: 
        rn = 1
    return ((s/sn) * send_fitness + (r/rn) * receive_fitness) + 1 # + 1 ensures that zero is not an output.

#This returns the total fitness of a population, by adding up each fitness.
def sum_fitness(population):
    total = 0
    for agent in population:
        total += fitness(agent)
    return total

#This is the function that creates changes in a matrix.
def mutate(system):
        for m in range(meanings):
            for s in range(signals):
                if random.random() < mutation_rate:
                    system[m][s] = random.randint(0, mutation_max)

#This essentially picks an agent.
def pick_parent(population,sum_f):
    accum = 0
    r = random.uniform(0, sum_f)
    for agent in population:
        accum += fitness(agent)
        if r < accum:
            return agent
        
#This makes a new population, by calling up the old population, deepcopying fit agents,
#mutating their matrices, zeroing their stats, and appending them to a new pop.
def new_population(population,outfile):
    new_p = []
    sum_f = sum_fitness(population)
    print(sum_f - 100) #This -100 counter-acts the necessary +1 in fitness, and caps optimality at 1000.
    outfile.write(str(sum_f - 100) + '\n')
    for i in range(len(population)): 
        agent = deepcopy(pick_parent(population, sum_f)[:2])
        mutate(agent[0])
        mutate(agent[1])
        new_p.append([agent[0], agent[1], [0., 0., 0., 0.]])
    return new_p

#This creates a zero-ed out matrix.
def random_system():
    system = []
    for i in range(meanings):
        meaning = []
        for j in range(signals):
            meaning.append(random.randint(0, mutation_max))
        system.append(meaning)
    return system

#This creates a random population of a set size with zero-ed matrices.
#Note the dual system: [0] is the sending matrix, [1] is the recieving matrix.
def random_population(size):
    population = []
    for i in range(size):
        population.append([random_system(), random_system(), [0., 0., 0., 0.]])
    return population

#This runs the entire game, as well as opening a file and writing the output from new_population.
def simulation(generations):
    output = open(output_file,'a')           
    population = random_population(size)
    for i in range(generations):
        for j in range(interactions):
            pop_update(population)
        population = new_population(population,output)
    output.close()          
