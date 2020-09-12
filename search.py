from random import shuffle

from eight_puzzle_state_2 import *
#from pegs_state import *
#from jealous_state import *

# a general search function that is given a start state, a goal state,
# a strategy ('dfs', 'bfs, 'best', 'manhattan') and a maximum number of states to
# visit.  Returns the number of states visited in order to find the goal
# state, using the given strategy

# best-first search expects the state objects to have a __lt__ method,
# which will determine how a list of states is sorted.
def search(start, goal, strategy, max_states, states_so_far=0):
    to_visit = [ start ]
    already_visited = set()
    while to_visit != []:
        state = to_visit.pop()
        if state == goal:

            return states_so_far
        elif states_so_far >= max_states:
            return states_so_far
        elif state in already_visited:
             pass
        else:
            already_visited.add(state)
            new_states = state.successors()
            shuffle(new_states)
            if strategy == 'dfs':
                to_visit = to_visit + new_states
            elif strategy == 'bfs':
                to_visit = new_states + to_visit
            elif strategy == 'best':
                to_visit = to_visit + new_states
                to_visit = sorted(to_visit)
            elif strategy == 'manhattan': #incorporated my estimator which is manhattan distance 
                to_visit = [manhattan_distance(new_states)]
            states_so_far += 1
    return states_so_far

# this compares search strategies.  It runs each
# strategy on start states 1 through n (some measure
# of difficulty of the problem).  Each is run the given
# number of trials.  A maximum number of states determines
# when the search should terminate (and fail)
def compare(strategies, easiest=1, hardest=10, trials=10, max_states=10000):
    for strat in strategies:
        print(',{}'.format(strat),end='')
    for level in range(easiest, hardest+1):
        print('\n{}'.format(level),end="")
        for strat in strategies:
            total_states = 0
            for trial in range(trials):
                start = start_state(level)
                goal = goal_state(level)
                total_states += search(start, goal, strat, max_states)
            print(',{}'.format(total_states//trials), end='')

def manhattan_distance(n):
    '''This function evaluates the manhattan distances for each successor states then takes the minimum
    manhattan distance and returns the next successor to visit.'''
    
    store = {} # stores all the positions and indexes of the successor states
    States ={} # stores the successor states along with its manhattan distance
    manhattan_distance = 0 #initialize at zero
    goal_dictionary = {'1':[0,0],'2':[0,1],'3':[0,2],'8':[1,0],' ':[1,1],'4':[1,2],'5':[2,2],'6':[2,1],'7':[2,0]}
    
    for suck in n:
        temp = suck
        for i in range(len(temp)):
            x = i//3 #calculating the x position of successor 
            y = i % 3 # calculating the y position of successor
            store.update({temp[i]:[x,y]})
            a = goal_dictionary[temp[i]]
            x2 = a[0]
            y2 = a[1]
            manhattan_distance += (abs(x2 - x) + abs(y2 - y)) # calculates thte manhattan distance 

        States.update({manhattan_distance:temp})
        the_min =min(States) # finds the minimum manhattan distance 
        next_direction = States.get(the_min) #calls the successor with the lowest manhattan distance

    return next_direction
        

