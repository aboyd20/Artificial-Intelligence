#Alicia Boyd's modified eight puzzle state
# CSC 380/480 Winter 2018
# Eight-puzzle using various forms of search
# Built on a generalized state finder

from random import shuffle    # to randomize the order in which successors are visited

class eight_puzzle_state:
    'this is the constructor which makes a copy of the list of tiles. We have '
    'copy because the list is mutable object, hence we have to save a new copy to self.tiles.'

    estimator = 0
    def __init__(self, tiles):
        self.tiles = tiles.copy()
        self.index = [0]

    def __str__(self):
        answer = ''
        for i in range(9):
            answer += '{} '.format(self.tiles[i])
            if (i+1)%3 == 0:
                answer += '\n'
        return answer

    def index(self, value):
        ans = []
        for i in range(len(self)):
            if self.tiles[i] == value:
                ans = i
                return ans

    def __len__(self):
        return len(self.tiles)

    def __getitem__(self, item):
        return self.tiles[item]

    def __iter__(self):
        return self

    def __repr__(self):
        return 'eight_puzzle_state({})'.format(self.tiles)

    def __eq__(self, other):
        return self.tiles == other.tiles
            
    def __hash__(self):
        return hash(self.tiles[0])
    
    def successors(self):
        successor_states = [ ]
        neighbors = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4,6],4:[1,3,5,7],5:[2,4,8],6:[3,7],7:[4,6,8],8:[5,7]}
        zero_loc = self.tiles.index(' ')
        for loc in neighbors[zero_loc]:
            state = eight_puzzle_state(self.tiles)
            state.tiles[zero_loc] = state.tiles[loc]
            state.tiles[loc] = ' '
            successor_states.append(state)
        return successor_states

    def evaluation(self):
        correct = 9
        for i in range(9):
            if self.tiles[i] != ['1', '2', '3', '8', ' ', '4', '7', '6', '5'][i]:
                correct -= 1
        return " The number correct is {} out of 9.".format(correct)
    

    def __lt__(self, other):
        'this is the less than method evalutes evaluation method'
        return self.evaluation() < other.evaluation() 
    

# 8-puzzle always has the same goal state, so "dummy" is there
# only because goal_state takes 1 parameter
def goal_state(dummy=0):
    return eight_puzzle_state(['1', '2', '3', '8', ' ', '4', '7', '6', '5'])

# from random import shuffle   random puzzle is too many moves from goal state
from random import randint

# make a start state which is n moves from goal state
def start_state(distance=1):
    already_visited = [ goal_state() ]
    state = goal_state()
    # max number of moves from start state to goal state
    for i in range(distance):
        successors = state.successors()
        for s in successors:
            if s in already_visited:
                successors.remove(s)
        shuffle(successors)
        state = successors[0]
        already_visited.append(state)
    return state

def random_eight_puzzle_state():
    tiles = ['1', '2', '3', '4', '5', '6', '7', '8', ' ']
    shuffle(tiles)
    return eight_puzzle_state(tiles)
