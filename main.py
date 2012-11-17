#!/usr/bin/env python

    #################################################################
    #     Author:  Reza Jafari Maraush (rzjfr@yahoo.com)
    #      Class:  AI , Fall 2012, UUT
    #
    #    Program:  Finding answers simple multinomial equation using 
    #              Genetic Algorithm
    #
    #   Language:  Python 2.7
    #     To Run:  python>=v2.7 matplotlib>=v1.0 genetics.py
    #      input:  "inpux.txt", population size, mutation,tournoment,
    #              crossover,elitism rates
    #     output:  answer to equation, average fittness of genertions
    # Descripton:  all four methods for evolving a generation to find
    #              answer in genetic algorithm has been implemented.
    #
    ##################################################################
import genetics

# latin alphabet for binomial equation 
ab=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w']
low=-100    # minimum amount of random numbers
high=100    # maximum amount of random numbers


def start():
    print "null"
def change_popn(p=0):
    '''()->int
    changes current population size to another legal
    population size
    >>> change_popn()
    500
    '''
    legal=False
    while not legal:
        p = raw_input('- population size:')
        if not p.isdigit():
            print " \'%s\' is not a number" %p
        elif int(p)<20 or int(p)>5000:
            print " Enter between 20 and 5000"
        else:
            legal=True
    return int(p)
def change_rate(what,p=0):
    '''(str)->int
    changes current rate to another legal rate
    >>> change_rate('elitism rate')
    0.75
    '''
    legal=False
    while not legal:
        p = raw_input('- new %s:'%what)
        if not p.isdigit():
            print " \'%s\' is not a number" %p
        elif int(p)<0 or int(p)>100:
            print " Enter between 0 and 100"
        else:
            legal=True
    return float(p)/100.0
    
def main():
    popltn=1000     # defualt size of population
    equation=None   # our equation
    elit_rate=0.05  # elitism rate
    cros_rate=0.75  # crossover rate
    mut_rate=0.15   # mutation rate
    tour_rate=0.15  # tournoment rate
    print '''
    
    
                        =============================
                              Genetic Algorithm
                        =============================
                    
                    
                    
    Genetic Algorithm (NOV 15 2012) -- "Reza Jafari Maraush"
    platform: i686-pc-linux-gnu (32-bit)
    
    Type 'help' for help and commands list
    Type 'q' or 'quit' to quit the Programm
    
    
    
    
    
    
    
    
    '''    
    commands=['help','q','quit','start','get','show','rates','popn','hist','log','export log','export hist']
    help='''                        =============================
                                User Help
                        =============================


DESCRIPTION
    this is a simple program finds answer of given equation using GA.

COMMANDS
    get          imports the "input.txt" to make the equation
    rates        changes the defualt  rates in genetic algol.
                 defualt rates are{ (mutation:   15%)
                                    (elitism:     5%)
                                    (tournoment: 15%)
                                    (crossover:  75%) }
    popn         chenges count of population in each generation
                 defualt is (1000)
    start        starts evolving the generation to find answer
    show         shows equation and all informations
    hist         shows the histogram of the average fitness of generations
    log          shows the log of all geneartions including average and best
                 fitness of each generation
    export hist  exports histogram as .png file format
    export log   exports log as .txt file
    q,quit       exit the programm
    
AUTHOR
    written by rzjfr. Maraush
    
COPYRIGHT
    License GPLv3+:GNU GPL version 3 or later<http://gnu.org/licenses/gpl.html>
    '''
    while(1):
        inputs = raw_input('> ')
        legal=False
        for c in commands:
            if inputs==c:
                legal=True
            

        while(legal==False):
            print "No commadn '%s' found, did you mean:" %inputs
            print ''' Command 'start'
 Command 'get'
 Command 'rates'
 Command 'popn'
 Command 'hist'
 Command 'log'
 Command 'export hist'
 Command 'export log' '''
            print "%s: command not found"%inputs
            inputs = raw_input('> ')
            for c in commands:
                if inputs==c:
                    legal=True    
        
        if(inputs=='get'):
            cofnt=[]    # coefficient blank list
            powr=[]     # power blank list
            equation=genetics.make_eq(powr,cofnt)
            print "Equation:",equation,"\n"
        if(inputs=='start'):
            start()
        if(inputs=='rates'):
            mut_rate=change_rate('Mutation rate')
            cros_rate=change_rate('Crossover rate')
            elit_rate=change_rate('Elitism rate')
            tour_rate=change_rate('Tournoment rate')
        if(inputs=='popn'):
            popltn=change_popn()
        if(inputs=='show'):
            print "Population have %i Individuals" %popltn
            print "Equation: ",equation
            print "Mutation rate= %i" %(mut_rate*100.0),'%'
            print "Crossover rate= %i" %(cros_rate*100.0),'%'
            print "Elitism rate= %i" %(elit_rate*100.0),'%'
            print "Tournoment rate= %i" %(tour_rate*100.0),'%'
        if(inputs=='hist'):
            print 'not implemented'  
        if(inputs=='log'):
            print 'not implemented'
        if(inputs=='export hist'):
            print 'not implemented'
        if(inputs=='export log'):
            print 'not implemented'
        if(inputs=='q' or inputs=='quit'):
            print "Goodbye!\n"
            break 
        if(inputs=='help'):
            print help
            raw_input(':')
if __name__ == "__main__": main()
