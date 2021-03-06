#!/usr/bin/env python
"""
the main part of the program to start
inputs:  "inpux.txt", population size,
        mutation, tournoment, crossover, elitism rates
output:  answer to equation, average fittness of genertions
"""

from random import randint
from Tkinter import *
from tkFileDialog import askopenfilename
import matplotlib.pyplot as plt
import genetics

# latin alphabet for polynomial equation
ab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
      'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
low = -10    # minimum amount of random numbers
high = 10    # maximum amount of random numbers


def answer(indiv):
    '''(list)->str
    returns a comprehensive answer for found answer list
    >>> answer([1,2,4])
    a=1 b=2 c=4
    '''
    i = 0
    result = ''
    for x in indiv:
        result += " %s=%i" % (ab[i], x)
        i += 1
    return result


def get_file():
    '''()->str
    reads the file from graphical interface
    '''
    # Load the file from system
    master = Tk()
    master.withdraw()  # hiding tkinter window
    str_file = askopenfilename(title='Select \"input.txt\" file')
    master.quit()
    return str_file


def start(input_str, popltn, elit_rate=0.05, cros_rate=0.75, mut_rate=0.15,
          tour_rate=0.15, show_hist=True):
    '''(str,int,float,float,float,float)->list of lists
    gets input string to evolve generation with given rates and population size
    calculates the best fittness
    also we choose wheater to show the histogram during evelutoin or not
    returns generation number that answer has been found
    we will use index number to calculate the average index of answers
    returns average fitness of population in each generation
    we will use this to show the progress
    >>> start("input.txt",400)
    [3456,[12.0,11.6,5.0,2.1,1]]
    '''
    if show_hist:
        plt.grid(True)      # turning on grid for our histogram
        plt.title('Multinomial Equation answers using GA ')
        plt.xlabel('# of Generation')                # x lable for histogram
        plt.ylabel('Average fitness of population')  # y lable for histogram
    length = genetics.len_eq(input_str)
    popn1 = genetics.population(popltn, length, low, high)
    history_score = [genetics.score(popn1), ]
    next_gen = genetics.generation(popn1, elit_rate, cros_rate,
                                   mut_rate, tour_rate)
    index = 0
    found = False
    best = [next_gen[0], genetics.fitness(next_gen[0]), 0]
    for i in xrange(10000):
        try:
            index += 1
            if not show_hist:
                print genetics.score(next_gen), genetics.fitness(next_gen[0])
            history_score.append(genetics.score(next_gen))
            # here we check the best answer if answer not found
            if best[1] > genetics.fitness(next_gen[0]):
                best = [next_gen[0], genetics.fitness(next_gen[0]), i]
            next_gen = genetics.generation(next_gen, elit_rate, cros_rate,
                                           mut_rate, tour_rate)
            if show_hist:
                # here we want to show the histogram as the programm going on
                plt.plot(index, genetics.score(next_gen), color='b',
                         marker='o')
                plt.pause(0.0000001)  # we puase to make the histogram dynamic
            if int(genetics.fitness(next_gen[0])) == 0:
                found = True
                break
        except KeyboardInterrupt:
            print "\nStoped!..."
            break
            plt.close()
    if found:
        print " The ansewer is:"
        print "", next_gen[0]
        print answer(next_gen[0])
        print " Fitness \'%i\' found in %i\'s generation" \
              % (genetics.fitness(next_gen[0]), index)
        if show_hist:
            plt.show()
    else:
        print " The answer not found in %i generation" % index
        print "  But the best guessed fitness is \'%i\'" \
              % best[1], " found in ", best[2], "\'s generation"
        print "  Aproximate answer is:\n", answer(best[0])
        if show_hist:
            plt.show()
    return [index, history_score]


def change_popn(p=0):
    '''()->int
    changes current population size to another legal
    population size
    >>> change_popn()
    500
    '''
    legal = False
    while not legal:
        p = raw_input('- population size:')
        if not p.isdigit():
            print " \'%s\' is not a number" % p
        elif int(p) < 20 or int(p) > 5000:
            print " Enter between 20 and 5000"
        else:
            legal = True
    return int(p)


def change_rate(what):
    '''(str)->int
    changes current rate to another legal rate
    >>> change_rate('elitism rate')
    0.75
    '''
    p = 0
    legal = False
    while not legal:
        p = raw_input('- new %s:' % what)
        if not p.isdigit():
            print " \'%s\' is not a number" % p
        elif int(p) < 0 or int(p) > 100:
            print " Enter between 0 and 100"
        else:
            legal = True
    return float(p) / 100.0


def static_hist(history_score):
    '''(list)->histogram
    creats a histogram from fitness history of generations
    '''
    plt.grid(True)
    plt.title('Multinomial Equation answers using GA ')
    plt.xlabel('# of Generation')
    plt.ylabel('Average fitness of population')
    plt.plot(history_score, color='r')
    plt.show()


def main():
    input_str = "input.txt"
    history_score = None
    ave_answer = []   # to store where anwser found
    popltn = 400      # defualt size of population
    equation = None   # our equation
    elit_rate = 0.05  # elitism rate
    cros_rate = 0.75  # crossover rate
    mut_rate = 0.15   # mutation rate
    tour_rate = 0.15  # tournoment rate
    print '''


                        =============================
                              Genetic Algorithm
                        =============================



    Genetic Algorithm (NOV 15 2012) -- "Reza Jafari Maraush"
    platform: i686-pc-linux-gnu (32-bit)

    Type 'help' for help and commands list
    Type 'q' or 'quit' to quit the Programm








    '''
    commands = ['help', 'q', 'quit', 'start', 'get', 'get file', 'show',
                'rates', 'popn', 'hist', 'log', 'export log', 'export hist']
    help = '''                        =============================
                                User Help
                        =============================


DESCRIPTION
    this is a simple program finds answer of given polynomial equation with GA

COMMANDS
    get          imports the "input.txt" from current directory
    get file     imports the "input.txt" file from any directory
    rates        changes the defualt  rates in genetic algol.
                 defualt rates are{ (mutation:   15%) (elitism:     5%)
                                    (tournoment: 15%) (crossover:  75%) }
    popn         chenges count of indiv. in population defualt is (400)
    start        evolving the generation to find answer (Ctrl+c to stop)
    show         shows equation and all informations
    hist         shows the histogram of the average fitness of generations
    log          shows the history log and some statistics
    export hist  exports histogram as .png file format
    export log   exports log as .txt file
    q,quit       exit the programm
'''
    while(1):
        inputs = raw_input('> ')
        legal = False
        for c in commands:
            if inputs == c:
                legal = True
        while legal is False:
            print "No commadn '%s' found, did you mean:" % inputs
            print ''' Command 'start'
 Command 'get'
 Command 'rates'
 Command 'popn'
 Command 'hist'
 Command 'log'
 Command 'export hist'
 Command 'export log' '''
            print "%s: command not found" % inputs
            inputs = raw_input('> ')
            for c in commands:
                if inputs == c:
                    legal = True
        if inputs == 'get':
            cofnt = []    # coefficient blank list
            powr = []     # power blank list
            equation = genetics.make_eq(powr, cofnt, input_str)
            print "Equation:", equation, "\n"
        if inputs == 'get file':
            input_str = get_file()
            cofnt = []    # coefficient blank list
            powr = []     # power blank list
            equation = genetics.make_eq(powr, cofnt, input_str)
            print "Equation:", equation, "\n"
        if inputs == 'start':
            if equation is None:
                print """ Please import \"input.txt\" first\n
  Note: you can use \'get\' command to load from current directory
        or \'get file\' command to read from another directory"""
            else:
                legal = False
                while not legal:
                    ans = raw_input('> Show the Histogram?[y/n] ')
                    if ans == 'y' or ans == 'n':
                        legal = True
                if ans == 'y':
                    log = start(input_str, popltn, elit_rate, cros_rate,
                                mut_rate, tour_rate)
                else:
                    log = start(input_str, popltn, elit_rate, cros_rate,
                                mut_rate, tour_rate, False)
                ave_answer.append(log[0])
                history_score = log[1]
        if inputs == 'rates':
            mut_rate = change_rate('Mutation rate')
            cros_rate = change_rate('Crossover rate')
            elit_rate = change_rate('Elitism rate')
            tour_rate = change_rate('Tournoment rate')
        if inputs == 'popn':
            popltn = change_popn()
        if inputs == 'show':
            print " Equation: ", equation
            print " Population have %i Individuals" % popltn
            print " Mutation rate= %i" % (mut_rate * 100.0), '%', \
                  "\t Crossover rate= %i" % (cros_rate * 100.0), '%'
            print " Elitism rate= %i" % (elit_rate * 100.0), '%', \
                  "\t Tournoment rate= %i" % (tour_rate * 100.0), '%'
        if inputs == 'hist':
            static_hist(history_score)
        if inputs == 'log':
            print " Average fitness of each generation for last attempt:"
            print "", history_score
            print "\n in %i attempt answers found at:" % len(ave_answer)
            print "", ave_answer
            print " In average answer found at ", \
                  sum(ave_answer)/(len(ave_answer)*1.0)
        if inputs == 'export hist':
            save_name = "histogram_%i.png" % (randint(100, 999))
            print " Histogram Saved in", save_name
            plt.plot(history_score)
            #plt.show()
            plt.savefig(save_name)
        if inputs == 'export log':
            print "not implemented yet!"
        if inputs == 'q' or inputs == 'quit':
            print "Goodbye!\n"
            break
        if inputs == 'help':
            print help
            raw_input(': Press any Key...')

if __name__ == "__main__":
    main()
