# This python script file implements the Blocks World program



def reorder(node):
    ''' the purpose of this function is to reorder the blocks incase the user
        enters in the blocks out of order. In addition this function will take
        care of the situation relative position of a block which is irrevelant'''
    temp = node.split('_')
    temp.sort()
    if len(temp) == 2:
        temp.insert(1, '_')
        start =''.join(temp)
    elif len(temp) == 3:
        temp.insert(1, '_')
        temp.insert(3, '_')
        start = ''.join(temp)
    else:
        start = ''.join(temp)
    return start
        

def dfs_paths(graph, start, goal):
    ''' depth first search function, user will enter start state and goal state
              to get the function to work list(dfs_paths(graph,'a_b_c', 'b_ac')'''
    new_start = reorder(start)
    new_goal  = reorder(goal)
    stack = [(new_start, [new_start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == new_goal:
                yield path + [goal]
            else:
                stack.append((next, path + [next]))
            
    

def bfs_paths(graph, start, goal):
    '''breadth first search code where the user enters the start and goal states
       to get the function to work list(bfs_paths(graph,'a_b_c', 'b_ac'))'''
    new_start = reorder(start)
    new_goal  = reorder(goal)
    queue = [(new_start, [new_start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == new_goal:
                path[0] = start
                yield path + [goal]
            else:
                queue.append((next, path + [next]))


def eval2(graph, goal):
    '''my evaluator function for best first search'''
    visited = [goal]
    f = {goal:0}
    stack = [(goal, [goal])]
    while stack:
        (vertex, path) = stack.pop(0)
        visited.append(vertex)
        for next in graph[vertex]:
            if next not in visited:
                f[next] = f[vertex] + 1
                stack.append((next, path + [next]))
    return f
              

def best_first_search(graph, start, goal):
    new_start = reorder(start)
    new_goal  = reorder(goal)
    path = [new_start]
    f = eval2(graph, new_goal)
    while path[-1] != new_goal:
        neighbors = graph[path[-1]] #neighbors is an address and its a set
        nn = [] #neighbors distance from the goal in list format
        aa = [] #address is the list format
        for each in neighbors:
            nn.append(f[each])
            aa.append(each)
        smallest = nn.index(min(nn)) 
        path.append(aa[smallest])
    return path, len(path)-1




def BlocksWorld():
    '''This is the main BlocksWorld program you run'''
    
    graph = {'a_b_c': set(['a_cb', 'ba_c', 'b_ca', 'ac_b','a_bc','ab_c']),
          'ac_b': set(['bac', 'a_b_c']),
          'a_bc': set(['abc', 'a_b_c']),
          'ba_c': set(['cba', 'a_b_c']),
          'b_ca': set(['bca', 'a_b_c']),
          'ab_c': set(['cab', 'a_b_c']),
          'a_cb': set(['acb', 'a_b_c']),
          'bac' : set(['ac_b']),
          'abc' : set(['a_bc']),
          'cba' : set(['ba_c']),
          'bca' : set(['b_ca']),
          'cab' : set(['ab_c']),
          'acb' : set(['a_cb'])}

    strategy = input("What is your strategy you would like to implement onto Block World? You may enter: dfs, bfs, best.     " )
    start       = input("What is your starting position? ")
    goal        = input("What is your goal position? ")
    
    if strategy == 'dfs':
        print(list(dfs_paths(graph, start, goal)))
    elif strategy == 'bfs':
        print(list(bfs_paths(graph, start, goal)))
    elif strategy == 'best':
        a,b = best_first_search(graph, start, goal)
        print("This is the path {} and here is the length of the path {}.".format(a,b))
        
        
    
    
