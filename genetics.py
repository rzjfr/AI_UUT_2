from random import randint,random
cofnt=[]    # coefficient blank list
powr=[]     # power blank list
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
        cofnt.append(int(ch))   # list that has the coefficient of equation
    p=[]
    p+= f.readline().split()    
    for ch in p:
        powr.append(int(ch))    # list that has the power of equation
    f.close()
    return zip(cofnt,powr)


def make_eq(powr,cofnt,i=0,result=""):
    '''
    (list,list)->str
    dsc: loads data and returns an equation of imported data
    assumption: no negetive power
    example:
    >>>make_eq([1 2 -1 1 -1 ],[+1 +1 2 1 1])
    a + 2b + (-c)^2 + d + (-e) +0= 0
    '''    
    z=load_data("input.txt",cofnt,powr)
    # at this point we want a flexible equation appearance
    for x,y in z:
        if x==1 and y!=1 and y!=0:
            result+= " %s^%s " %(ab[i],y)
        elif y==1 and x>0 and x!=1:
            result+= " %i%s " %(x,ab[i])
        elif y==1 and x<0 and x!=-1:
            result+= " (%i)%s " %(x,ab[i])
        elif y==1 and x==-1:
            result+= " (-%s) " %(ab[i])
        elif y!=1 and x==-1:
            result+= " (-%s)^%i " %(ab[i],y)    
        elif y==1 and x==1:
            result+= " %s " %(ab[i])
        elif y==0 or x==0:
            i-=1
        else:
            result+= " (%i%s)^%s " %(x,ab[i],y)
        i+=1
        if i !=len(z):
            result+="+"
    return result+" = 0"


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
        i+=1
    f.close()
    return i
    


def individual(length, low, high):
    '''
    (int,int,int)->list
    dsc: Create a random list as a member of the population.
    example:
    >>>individual(5,-100,100)
    [-90, 87, -80, 52, 71]
    '''
    return [randint(low,high) for i in xrange(length)]


def summs(powr,cofnt,indiv):
    '''
    (list,list,list)->int
    dsc: summation of equation with real number
    exmple:
    >>>summs([1,1,1,1,1],[-3,1,1,1,1],[1,-1,1,1,1])
    -1
    '''
    i=0
    result=0
    for x in xrange(len(powr)):
        result+=(cofnt[i]*indiv[i])**powr[i]
        i+=1
    return result

  
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

def crossover(parent1,parent2,length):
    '''(list,list,int)->list of list
    dsc:
    with random point as pivot to cross over given parents
    
    example: pivot is 3
    >>> crossover([-54, 64, 56, -37, -56],[43, 93, -57, -94, -57],5)
    [[43, 93, -57, -37, -56], [-54, 64, 56, -94, -57]]
    '''
    pivot = randint(1, length-1)
    #print pivot
    child = parent1[:pivot] + parent2[pivot:]
    parent1 = parent2[:pivot] + parent1[pivot:]
    parent2 = child
    return [parent1,parent2]

def generation(popn,elit_rate=0.05,cros_rate=0.75,mut_rate=0.15,tour_rate=0.15):
    '''
    (list of lists)-> list of lists
    dsc:
    in this function we generate the next population with current population so as 
    input we have population and also elitism,crossover,mutation and tournomrnt rates
    example:
    >>> generation(cur_popn)
    next_popn
    '''
    scored = [ (fitness(x), x) for x in popn]   # a list contains each individual with fitness
    scored = [ x[1] for x in sorted(scored)]    # removing fittness from sorted list


    '''Eletisim'''
    len_elit = int(len(scored)*elit_rate)   # now we use elitism to send best indiv. to next_popn
    next_popn = scored[:len_elit]           # next population 
    cur_popn=scored[len_elit:]              # current population

    

    '''Tournoment'''
    for individual in cur_popn:             # tournoment is Roulette Wheel Selection 
        if tour_rate > random():            # here we choose randomly from scored population
            next_popn.append(individual)    # so the higher fitnessed indiv. have more chance
            cur_popn.remove(individual)
      
    #len_cur =len(next_popn)    # current lenght of next population
    len_rest= len(cur_popn)     # to fill rest of population
    if len_rest%2 !=0:          # we want pairs for crossover  
        next_popn.append(cur_popn.pop(0))
    len_rest= len(cur_popn)
    
   
    '''Crossover'''
    while len(cur_popn)>0:
        i=0 # we will choose i index randomly
        j=0 # we will choose j index randomly
        while i==j:     #
            i = randint(0, len(cur_popn)-1)
            j = randint(0, len(cur_popn)-2)
            
        parent1 = cur_popn[i]       # first parent chosen
        parent2 = cur_popn[j]       # second parent chosen
        # we also need to remove chosen chromosomes from current population
        cur_popn.remove(cur_popn[i]) 
        cur_popn.remove(cur_popn[j])
        # with constant probabality corossover happens
        if cros_rate > random():
            childrens=crossover(parent1,parent2,len(parent1))
            next_popn.extend(childrens)
        # or they will be sent to next population as they are
        else:
            next_popn.extend([parent1,parent2])
        
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



'''=========================TEST==================================='''
low=-100
high=100
popltn=1000
length=len_eq("input.txt")
print "Equation:",make_eq(powr,cofnt),"\n"
popn1=population(popltn,length,low,high)
 
print popn1

print score(popn1)
print generation(popn1)
next_gen = generation(popn1)
for i in xrange(10000):
    print score(next_gen),fitness(next_gen[0])
    next_gen = generation(next_gen)
    if int(fitness(next_gen[0]))==0:
        print "found!"
        break
print "best guess fitness is:",fitness(next_gen[0])
#if fitness(next_gen[0])>0:
#print float(100/13),"%"
print next_gen[0]

'''=========================TEST=ENDS=============================='''