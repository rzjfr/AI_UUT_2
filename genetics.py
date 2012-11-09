from random import randint
cofnt=[]
powr=[]
ab=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w']

def load_data(file,cofnt=[],powr=[]):
    '''
    dsc: loads Coefficient and Power into seperate lists 
    from .txt file
    example:
    >>>load_data("input.txt",cofnt,powr)
    [('8', '2'), ('3', '3'), ('2', '4'), ('5', '2'), ('1', '5')]
    '''
    f = open(file)
    cofnt+= f.readline().split()
    powr+= f.readline().split()
    f.close()
    return zip(cofnt,powr)
load_data("input.txt",cofnt,powr)

def make_eq(powr,cofnt,i=0,result=""):
    '''
    (list,list)->str
    dsc: returns an equation of imported data
    example:
    >>>make_eq(powr,cofnt)
    (1a^2)+(-1b^2)+(1c^2)+(1d^2)+(1e^2)+0= 0
    '''
    for x in powr:
        for y in cofnt:
            result+= "(%i%s^%s)+" %(int(y),ab[i],int(x))
            i+=1
        break
    return result+"0= 0"


def len_eq(file,result="",i=0):
    '''
    (filestr)->int
    dsc: to findout length of equation
    >>len_eq("input.txt")
    5
    '''
    f = open(file)
    y= f.readline().split()
    for ch in y:
        i+=1                        #result+=ch
    f.close()
    return i                        #len(result)/2
    


def individual(length, low, high):
    '''
    (int,int,int)->list
    dsc: Create a random list as a member of the chromosome.
    example:
    >>>individual(5,-100,100)
    [-90, 87, -80, 52, 71]
    '''
    return [randint(low,high) for i in xrange(length)]
indiv=individual(5,-100,100)
import numpy
def summs(powr,cofnt,indiv):
    '''
    (list,list,list)->int
    dsc: summation of equation with real number
    exmple:
    
    '''
    
    pr = numpy.array(powr)
    cr = numpy.array(cofnt)
    ir = numpy.array(indiv)
    print cr*(ir**pr)
    return sum(cr*(ir**pr))

print summs([1,1,1,1,1],[-3,1,1,1,1],[1,-1,1,1,1])

from operator import add   
def chromosome(count, length, low, high):
    '''
    (int,int,int,int)->list
    dsc: Create a number of random individuals as a chromosome
    example:
    >>>chromosome(3,5,0,100)
    [[94, 99, 59, 77, 48], [100, 100, 87, 80, 38], [5, 100, 92, 18, 75]]
    '''
    return [individual(length, low, high) for i in xrange(count)]
def fitness(individual, target):
    '''
    (list,int)->int
    dsc: returns fitnes of each individual (lower is better)
    '''
    sum = reduce(add, individual, 0)
    return abs(target-sum)

