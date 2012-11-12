from random import randint,random
#from operator import add 
import numpy

cofnt=[]    # coefficient blank list
powr=[]     # power blank list
equla=[]    # random calculated blank list
# latin alphabet for binomial equation 
ab=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w']

def load_data(file1,cofnt=[],powr=[]):
    '''
    dsc: loads Coefficient and Power into seperate lists 
    from .txt file
    example:
    >>>load_data("input.txt",cofnt,powr)
    [('8', '2'), ('3', '3'), ('2', '4'), ('5', '2'), ('1', '5')]
    '''
    f = open(file1)
    c=[]
    c+= f.readline().split()
    for ch in c:
        cofnt.append(int(ch))
    p=[]
    p+= f.readline().split()
    for ch in p:
        powr.append(int(ch))
    f.close()
    return zip(cofnt,powr)


def make_eq(powr,cofnt,i=0,result=""):
    '''
    (list,list)->str
    dsc: loads data and returns an equation of imported data
    example:
    >>>make_eq([1 2 -1 1 -1 ],[+1 +1 2 1 1])
    a + 2b + (-c)^2 + d + (-e) +0= 0
    '''    
    z=load_data("input.txt",cofnt,powr)
    # at this point we want a flexible equation appearance
    for x,y in z:
        if x==1 and y!=1 and y!=0:
            result+= " %s^%s +" %(ab[i],y)
        elif y==1 and x>0 and x!=1:
            result+= " %i%s +" %(x,ab[i])
        elif y==1 and x<0 and x!=-1:
            result+= " (%i)%s +" %(x,ab[i])
        elif y==1 and x==-1:
            result+= " (-%s) +" %(ab[i])
        elif y!=1 and x==-1:
            result+= " (-%s)^%i +" %(ab[i],y)    
        elif y==1 and x==1:
            result+= " %s +" %(ab[i])
        elif y==0 or x==0:
            i-=1
        else:
            result+= " (%i%s)^%s +" %(x,ab[i],y)
        i+=1
    return result+"0= 0"


def len_eq(file1,result="",i=0):
    '''
    (filestr)->int
    dsc: to findout length of equation
    >>len_eq("input.txt")
    5
    '''
    f = open(file1)
    y= f.readline().split()
    for ch in y:
        i+=1#result+=ch
    f.close()
    return i#len(result)/2
    


def individual(length, low, high):
    '''
    (int,int,int)->list
    dsc: Create a random list as a member of the population.
    example:
    >>>individual(5,-100,100)
    [-90, 87, -80, 52, 71]
    '''
    return [randint(low,high) for i in xrange(length)]


def summs(powr,cofnt,indiv,equla=[]):
    '''
    (list,list,list)->int
    dsc: summation of equation with real number
    exmple:
    >>>summs([1,1,1,1,1],[-3,1,1,1,1],[1,-1,1,1,1])
    -1
    '''
    pr = numpy.array(powr)
    cr = numpy.array(cofnt)
    ir = numpy.array(indiv)
    equla+= (cr*(ir**pr)).tolist()
    return sum(cr*(ir**pr))


  
def population(count, length, low, high):
    '''
    (int,int,int,int)->list
    dsc: Create a number of random individuals as a population
    example:
    >>>population(3,5,-100,100)
    [[94, 99, 59, 77, 48], [100, 100, 87, 80, 38], [5, 100, 92, 18, 75]]
    '''
    return [individual(length, low, high) for i in xrange(count)]

def fitness(indiv, target=0):
    '''
    (list,int)->int
    dsc: returns fitnes of each individual (lower is better)
    >>>fitness([1, 15, -80, -14, 48])
    6350
    '''
    # sum = reduce(add, individual, 0)
    summ =summs(powr,cofnt,indiv)
    return abs(target-summ)     # goal is reaching 0.0

def score(popn, target=0):
    '''
    (list)->float
    dsc: Find average fitness for a population
    >>>score([[52, -40, 65, 35, 6], [59, 22, -78, -59, 50], [86, -90, 14, -47, 22]])
    3469.66666667
    '''
    summ= sum([fitness(x, target) for x in popn])
    return summ / (len(popn) * 1.0)

def generation(popn,target=0,elit_rate=0.05,cros_rate=0.75,mut_rate=0.15,tour_rate=0.15):
    scored = [ (fitness(x, target), x) for x in popn]   # a list contains each individual with fitness
    print scored
    scored = [ x[1] for x in sorted(scored)]            # removing fittness from sorted list
    print scored
    '''=======================
    Chosing parents for childs
    ======================='''
    '''Eletisim'''
    len_elit = int(len(scored)*elit_rate)   # we use elite individuals as a parent for next generation
    parents = scored[:len_elit]             # the result is awsome! i get 25 fitness score with only 20 idividuals 
    print parents
    for s in parents:
        print fitness(s)
    
    '''Tournoment'''
    for individual in scored[len_elit:]:    # tournoment is Roulette Wheel Selection 
        if tour_rate > random():            # here we choose randomly from scored population
            parents.append(individual)      # so the higher fitnessed indiv. have more chance
    print parents
    
    
    '''========================
    Next generation individuals
    ========================'''
    '''Mutation'''
    for individual in parents:
        if mut_rate > random():
            pos_mut = randint(0, len(individual)-1)
            # here we change the random positon with random number
            # betwean the lowest and highest number in indiv.
            individual[pos_mut] = randint(min(individual), max(individual))
    print parents
    
    
    '''Crossover'''
    len_parents = len(parents)
    len_rest = len(popn) - len_parents          # we crossover for rest of population
    children = []                               # here we keep the children
    while len(children) < len_rest:
        parent1 = randint(0, len_parents-1)
        parent2 = randint(0, len_parents-1)
        if parent1 != parent2:
            parent1 = parents[parent1]
            parent2 = parents[parent2]
            pivot = len(parent1) / 2            # pivot is half of indiv.
            child = parent1[:pivot] + parent2[pivot:]
            children.append(child)
    parents.extend(children)        # mutaded parents and children creats next generation
    print parents
'''=========================TEST==================================='''
low=-100
high=100
popltn=20
length=len_eq("input.txt")

#load_data("input.txt",cofnt,powr)
print "Equation:",make_eq(powr,cofnt),"\n"

indiv1=individual(length,low,high)
print indiv1
print summs(powr,cofnt,indiv1),"\n"

popn1=population(popltn,length,low,high)
print popn1
print score(popn1),"\n"

generation(popn1)


# cross over test
parent1 = [1,2,3,4,5,6]
parent2 = ['a','b','c','d','e','f']
child = parent1[:3] + parent2[3:]
print "\n",child
'''=========================TEST=ENDS=============================='''