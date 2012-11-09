from random import randint
from operator import add

def individual(length, low, high):
    '''
    (int,int,int)->list
    dsc: Create a random list as a member of the population.
    example:
    >>>individual(5,0,100)
    [92, 21, 75, 66, 70]
    '''
    return [randint(low,high) for i in xrange(length)]

def population(count, length, low, high):
    '''
    (int,int,int,int)->list
    dsc: Create a number of random individuals as a population
    example:
    >>>population(3,5,0,100)
    [[94, 99, 59, 77, 48], [100, 100, 87, 80, 38], [5, 100, 92, 18, 75]]
    '''
    return [individual(length, low, high) for i in xrange(count)]

def fitness(individual, target):
    '''
    (int,int)->int
    dsc: returns fitnes of each individual 
    '''
    sum = reduce(add, individual, 0)
    return abs(target-sum)
