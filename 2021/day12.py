# day12
import copy


    

def part1():
    global paths, queue, queue2

    s = get_cave('start')
    queue.append([s])
    
    while len(queue) > 0:
                          
        #for each path in queue
        for p in queue:
            
            #get last cave added
            current_cave = p[-1]
            for current_n in current_cave.neighbors:
                #if the neighbor is 'end'
                is_new_node = True
                if current_n.name == 'end':
                    
                    #deepcopy path, add end, add this new path to paths
                    new_path = copy.deepcopy(p)
                    new_path.append(current_n)
                    paths.add(tuple(new_path))
                    continue
                
                #if neighbor is lowercase and already visited
                elif (current_n.name == current_n.name.lower()):
                    for node in p:

                        if node.name == current_n.name:
                            is_new_node = False
                            break

                if is_new_node:
                    #create a duplicate path
                    new_path = copy.deepcopy(p)
                    
                    #add new neighbor
                    new_path.append(current_n)
                        
                    #place new path back queue2
                    queue2.append(new_path)
        
        #deep copy queue 2 onto queue, reset queue2
        queue = copy.deepcopy(queue2)
        queue2.clear()

        
    print('Part1:', len(paths))


def part2_old():
    global paths, queue, queue2
    
    while len(queue) > 0:
        if len(queue) > 2500:
            print(len(queue))
            
        #for each path in queue
        for p in queue:
            
            #get last cave added
            current_cave = p[-1]
            
            for current_n in current_cave.neighbors:    
                #if the neighbor is 'end'
                is_new_node = True
                if current_n.name == 'end':
                    
                    #deepcopy path, add end, add this new path to paths
                    new_path = copy.deepcopy(p)
                    new_path.append(current_n)
                    paths.add(tuple(new_path))
                    continue

                # cannot go back to start
                if current_n.name == 'start':
                    continue
                
                #if neighbor is lowercase and already visited
                elif (current_n.name == current_n.name.lower()):
                    for node in p:

                        if node.name == current_n.name:
                            if duplicate_already_exists(p):
                                is_new_node = False
                            break

                if is_new_node:
                    #create a duplicate path
                    new_path = copy.deepcopy(p)
                    
                    #add new neighbor
                    new_path.append(current_n)
                        
                    #place new path back queue2
                    queue2.append(new_path)
        
        #deep copy queue 2 onto queue, reset queue2
        queue = copy.deepcopy(queue2)
        queue2.clear()

        
    print('Part 2:', len(paths))




def part2_faster_w_sets():
    global paths, queue, queue2

    s = get_cave('start')
    p = path()
    p.add_cave(s)
    queue.append(p)

    while len(queue) > 0:
        if len(queue) > 2500:
            print(len(queue))
            
        #for each path in queue
        for p in queue:
            
            #get last cave added
            current_cave = p.order[-1]
            
            for current_n in current_cave.neighbors:    
                #if the neighbor is 'end'
                is_new_node = True
                if current_n.name == 'end':
                    
                    #deepcopy path, add end, add this new path to paths
                    new_path = copy.deepcopy(p)
                    new_path.add_cave(current_n)
                    paths.add(new_path)
                    continue

                # cannot go back to start
                if current_n.name == 'start':
                    continue
                
                #if neighbor is lowercase and already visited
                elif (current_n.name == current_n.name.lower()):
                    if current_n.name in p.visited_cave_names:
                        if p.duplicate_lowercase == True:
                            is_new_node = False

                if is_new_node:
                    #create a duplicate path
                    new_path = copy.deepcopy(p)
                    
                    #add new neighbor
                    new_path.add_cave(current_n)
                        
                    #place new path back queue2
                    queue2.append(new_path)
        
        #deep copy queue 2 onto queue, reset queue2
        queue = copy.deepcopy(queue2)
        queue2.clear()

        
    print('Part2:', len(paths))


class cave:
    def __init__(self, name, neighbors = set()):
        self.name = name
        self.neighbors = set()

    def add_neighbor(self, cave):
        self.neighbors.add(cave)

    def get_neighbors_names(self):
        nbrs = []
        for n in self.neighbors:
            nbrs.append(n.name)
        return nbrs
       


def get_cave(name):
    global caves

    for c in caves:
        if c.name == name:
            return c
    print('no such cave')


        
        
class path:
    def __init__(self, order = [], visited_cave_names = set(), duplicate_lowercase = False):
        self.order               = []
        self.visited_cave_names  = visited_cave_names
        self.duplicate_lowercase = duplicate_lowercase

    def add_cave(self, c):
        self.order.append(c)
        if (c.name in self.visited_cave_names) and (c.name == c.name.lower()):
            self.duplicate_lowercase = True
        self.visited_cave_names.add(c.name)
        


   

caves       = set()
cave_names  = set()
connections = set()

# ------------- Process data--------------
f = open('day12.txt', 'r')
for x in f:
    x = x.strip()
    x = x.split('-')
    connections.add(tuple(x))
    
    for item in x:
        if item not in cave_names:
            cave_names.add(item)
            c = cave(item)
            caves.add(c)

# ------------- Create cave system (graph) -------------
for item in connections:
    c1 = get_cave(item[0])
    c2 = get_cave(item[1])

    c1.add_neighbor(c2)
    c2.add_neighbor(c1)
           
for c in caves:    
    print(c.name, '\t', c.get_neighbors_names())
print('------------------------')



def print_names_in_path(path):
    for p in path:
        print(p.name, end = ' ')
    print()


def duplicate_already_exists(path):
    for i in range(1, len(path)):
        if path[i].name == path[i].name.lower(): #this only applies to lower case caves
            for j in range(i+1, len(path)):
                if path[i].name == path[j].name:
                    return True
    return False




        


    



#--------------- global variables ------------
paths  = set()
queue  = []
queue2 = []





#part1()
#part2()

def dfs(p):
    global paths

    
    last_cave = p.order[-1]
    
    for n in last_cave.neighbors:
        new_p = copy.deepcopy(p)
        
        if n.name == 'end':
            new_p.add_cave(n)
            paths.add(new_p)
        
        elif n.name == 'start':
            continue
        
        elif n.name == n.name.lower():      # lowercase cave
            # if it is a duplicate
            if n.name in new_p.visited_cave_names:
                
                # if a duplicate already exists
                if new_p.duplicate_lowercase == True:
                    continue
                else:
                    new_p = copy.deepcopy(p)
                    new_p.add_cave(n)
                    dfs(new_p)
                
                # 1st case of a duplicate
            else:
                new_p = copy.deepcopy(p)
                new_p.add_cave(n)
                dfs(new_p)
            

        else:                               # uppercase cave
            #print('here')
            new_p.add_cave(n)
            dfs(new_p)
                    
                



    
def part2_dfs():
    global paths
    
    #s = get_cave('start')
    #s = get_cave('po') # length of paths = 51277
    #s = get_cave('lo') # length of paths = 43209
    #s = get_cave('nu') # length of paths = 54734
    
    p = path()
    p.add_cave(s)
    dfs(p)
    
    print('length of paths =', len(paths))



#part2_dfs()
print('Part 2:',51277+43209+54734)























    
