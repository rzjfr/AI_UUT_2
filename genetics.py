#!/usr/bin/env python
"""
Methods for genetic algorithm
Note: i stealed some methods form somewhere that i cannot remember now
"""

from random import randint, random
cofnt = []    # coefficient blank list
powr = []     # power blank list
# latin alphabet for polynomial equation
ab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
      'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def load_data(str_file, cofnt=[], powr=[]):
    '''(str, list, list)->list
    dsc: loads Coefficient and Power into seperate lists
    from .txt file
    example:
    >>> load_data("input.txt",cofnt,powr)
    [('8', '2'), ('3', '3'), ('2', '4'), ('5', '2'), ('1', '5')]
    '''
    f = open(str_file)
    c = []
    c += f.readline().split()
    for ch in c:
        cofnt.append(int(ch))   # list that has the coefficient of equation
    p = []
    p += f.readline().split()
    for ch in p:
        powr.append(int(ch))    # list that has the power of equation
    f.close()
    return zip(cofnt, powr)


def make_eq(powr, cofnt, str_file):
    '''(list, list)->str
    dsc: loads data and returns an equation of imported data
    assumption: no negetive power
    example:
    >>> make_eq([1 2 -1 1 -1 ],[+1 +1 2 1 1])
    a + 2b + (-c)^2 + d + (-e) +0= 0
    '''
    i = 0
    result = ""
    z = load_data(str_file, cofnt, powr)
    # at this point we want a flexible equation appearance
    for x, y in z:
        if x == 1 and y != 1 and y != 0:
            result += " %s^%s " % (ab[i], y)
        elif y == 1 and x > 0 and x != 1:
            result += " %i%s " % (x, ab[i])
        elif y == 1 and x < 0 and x != -1:
            result += " (%i)%s " % (x, ab[i])
        elif y == 1 and x == -1:
            result += " (-%s) " % (ab[i])
        elif y != 1 and x == -1:
            result += " (-%s)^%i " % (ab[i], y)
        elif y == 1 and x == 1:
            result += " %s " % (ab[i])
        elif x == 0:
            i -= 1
        elif y == 0:
            result += " %i " % (x)
        else:
            result += " %i(%s^%s) " % (x, ab[i], y)
        i += 1
        if i != len(z):
            result += "+"
    return result + " = 0"


def len_eq(file1, result="", i=0):
    ''' (file, str)->int
    dsc: to findout length of equation
    >>len_eq("input.txt")
    5
    '''
    f = open(file1)
    y = f.readline().split()
    for ch in y:
        i += 1
    f.close()
    return i


def individual(length, low, high):
    '''(int,int,int)->list
    dsc: Create a random list as a member of the population.
    example:
    >>>individual(5,-100,100)
    [-90, 87, -80, 52, 71]
    '''
    return [randint(low, high) for i in xrange(length)]


def summs(powr, cofnt, indiv):
    '''(list,list,list)->int
    dsc: summation of equation with real number
    exmple:
    >>>summs([1,1,1,1,1],[-3,1,1,1,1],[1,-1,1,1,1])
    -1
    '''
    i = 0
    result = 0
    for x in xrange(len(powr)):
        result += cofnt[i] * (indiv[i] ** powr[i])
        i += 1
    return result


def population(count, length, low, high):
    '''(int,int,int,int)->list
    dsc: Create a number of random individuals as a population
    example:
    >>>population(3,5,-100,100)
    [[94, 99, 59, 77, 48], [100, 100, 87, 80, 38], [5, 100, 92, 18, 75]]
    '''
    return [individual(length, low, high) for i in xrange(count)]


def fitness(indiv, target=0):
    '''(list,int)->int
    dsc: returns fitnes of each individual (lower is better)
    >>>fitness([1, 15, -80, -14, 48])
    6350
    '''
    summ = summs(powr, cofnt, indiv)
    return abs(target-summ)     # goal is reaching 0.0


def score(popn, target=0):
    '''(list)->float
    dsc: Find average fitness for a population
    >>>score([[52, -40, 65, 35, 6], [59, 22, -78, -59, 50],
             [86, -90, 14, -47, 22]])
    3469.66666667
    '''
    summ = sum([fitness(x, target) for x in popn])
    return summ / (len(popn) * 1.0)


def tournoment(popn, next_popn=[], tour_rate=0.15):
    '''(list of lsit,list of list,float)->list of list
    our tournoment is Roulette Wheel Selection so the
    individual with higher fitness have more chance
    >>>tournoment(popn)
    [[-19, -58, 71, 84, -62], [92, -92, -8, -99, 27]]
    '''
    popn_clone = [(fitness(x), x) for x in popn]
    best = sorted(popn_clone)[0][0]  # we need best to find the fraction
    if best == 0:
        best = 1       # we don't want to ignore the zero fitness
    for individual in popn_clone:
        if individual[0] == 0:
            individual[0] = 1
    popn_clone = [(best/(x[0]*1.0), x[1]) for x in popn_clone]
    # tournoment is Roulette Wheel Selection, I was lying all the time!
    for individual in popn_clone:
        if individual[0] * tour_rate > random():
            next_popn.append(individual[1])
            popn.remove(individual[1])
    return next_popn


def crossover(parent1, parent2, length):
    '''(list,list,int)->list of list
    dsc:
    with random point as pivot to cross over given parents

    example: pivot is 3
    >>> crossover([-54, 64, 56, -37, -56],[43, 93, -57, -94, -57],5)
    [[43, 93, -57, -37, -56], [-54, 64, 56, -94, -57]]
    '''
    pivot = randint(1, length-1)
    child = parent1[:pivot] + parent2[pivot:]
    parent1 = parent2[:pivot] + parent1[pivot:]
    parent2 = child
    return [parent1, parent2]


def generation(popn, elit_rate=0.05, cros_rate=0.75, mut_rate=0.15,
               tour_rate=0.15):
    '''(list of lists)-> list of lists
    dsc: in this function we generate the next population with current
    population so as input we have population and also elitism,crossover,
    mutation and tournomrnt rates
    example:
    >>>generation(cur_popn)
    next_popn
    '''
    # list contains each individual with its fitness
    scored = [(fitness(x), x) for x in popn]
    # removing fittness from sorted list
    scored = [x[1] for x in sorted(scored)]
    '''Eletisim'''
    len_elit = int(len(scored)*elit_rate)   # send best indiv. to next_popn
    next_popn = scored[:len_elit]           # next population
    cur_popn = scored[len_elit:]            # current population
    '''Tournoment'''
    tournoment(cur_popn, next_popn, tour_rate)
    #len_cur =len(next_popn)    # current lenght of next population
    len_rest = len(cur_popn)     # to fill rest of population
    if len_rest % 2 != 0:          # we want pairs for crossover
        next_popn.append(cur_popn.pop(0))
    len_rest = len(cur_popn)
    '''Crossover'''
    while len(cur_popn) > 0:
        i = 0  # we will choose i index randomly
        j = 0  # we will choose j index randomly
        while i == j:     #
            i = randint(0, len(cur_popn)-1)
            j = randint(0, len(cur_popn)-2)
        parent1 = cur_popn[i]       # first parent chosen
        parent2 = cur_popn[j]       # second parent chosen
        # we also need to remove chosen chromosomes from current population
        cur_popn.remove(cur_popn[i])
        cur_popn.remove(cur_popn[j])
        # with constant probabality corossover happens
        if cros_rate > random():
            childrens = crossover(parent1, parent2, len(parent1))
            next_popn.extend(childrens)
        # or they will be sent to next population as they are
        else:
            next_popn.extend([parent1, parent2])
    '''Mutation'''
    for individual in scored[:len_elit]:
        if mut_rate > random():
            # here we change the random positon with random number
            pos_mut = randint(0, len(individual)-1)
            # betwean the lowest and highest number in indiv.
            individual[pos_mut] = randint(min(individual), max(individual))
            # or between the given range
            #individual[pos_mut] = randint(-100,100)
    return next_popn

make_eq(powr, cofnt, "input.txt")
