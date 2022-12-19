#day18
import math, copy

def num_hidden_sides(c):
    global cubes

    n = 0
    #cube above
    if (c[0], c[1] + 1, c[2]) in cubes:
        n += 1
    #cube below
    if (c[0], c[1] - 1, c[2]) in cubes:
        n += 1
    #cube left
    if (c[0] - 1, c[1], c[2]) in cubes:
        n += 1
    #cube right
    if (c[0] + 1, c[1], c[2]) in cubes:
        n += 1
    #cube closer
    if (c[0], c[1], c[2] - 1) in cubes:
        n += 1
    #cube farther
    if (c[0], c[1], c[2] + 1) in cubes:
        n += 1

    return n


def get_neighbors(s):
    global x_range, y_range, z_range

    ngbrs = set()
    #above
    if s[1] + 0 <= y_range[1]:
        ngbrs.add((s[0], s[1] + 1, s[2]))
    #below
    if s[1] - 0 >= y_range[0]:
        ngbrs.add((s[0], s[1] - 1, s[2]))
        
    #right
    if s[0] + 0 <= x_range[1]:
        ngbrs.add((s[0] + 1, s[1], s[2]))
    #left
    if s[0] - 0 >= x_range[0]:
        ngbrs.add((s[0] - 1, s[1], s[2]))

    #closer
    if s[2] + 0 <= z_range[1]:
        ngbrs.add((s[0], s[1], s[2] + 1))
    #farther
    if s[2] - 0 >= z_range[0]:
        ngbrs.add((s[0], s[1], s[2] - 1))

    return ngbrs


def surfaces_facing_ext(c):
    global reachable_spaces

    n = 0
    #surface above
    if (c[0], c[1] + 1, c[2]) in reachable_spaces:
        n += 1
    #surface below
    if (c[0], c[1] - 1, c[2]) in reachable_spaces:
        n += 1
    #surface left
    if (c[0] - 1, c[1], c[2]) in reachable_spaces:
        n += 1
    #surface right
    if (c[0] + 1, c[1], c[2]) in reachable_spaces:
        n += 1
    #surface closer
    if (c[0], c[1], c[2] - 1) in reachable_spaces:
        n += 1
    #surface farther
    if (c[0], c[1], c[2] + 1) in reachable_spaces:
        n += 1

    return n



#global variables 
x_range = [math.inf, 0]
y_range = [math.inf, 0]
z_range = [math.inf, 0]
cubes = set()
hidden_sides = 0


#read data
f = open('day18.txt','r')
for x in f:
    x = eval(x)
    cubes.add(x)
    x_range[0] = min(x_range[0], x[0])
    x_range[1] = max(x_range[1], x[0])

    y_range[0] = min(y_range[0], x[1])
    y_range[1] = max(y_range[1], x[1])

    z_range[0] = min(z_range[0], x[2])
    z_range[1] = max(z_range[1], x[2])


#count the number of hidden sides
for c in cubes:
    hidden_sides += num_hidden_sides(c)

print('Part 1:', len(cubes) * 6 - hidden_sides)



#part 2
#create an empty set of reachable spaces
reachable_spaces = set()

#create an empty set of new reachable spaces
new_reachable_spaces = set()

#expand range by 1 in every direction so there is an empty outer space around perimeter
#pick a starting point on the outside  
start = (x_range[0] - 1, y_range[0] - 1, z_range[0] - 1)

#add it to reachable spaces and new reachabe spaces
reachable_spaces.add(start)
new_reachable_spaces.add(start)


#create a set of spaces that are reachable
while len(new_reachable_spaces) > 0:
    temp = set()
    
    for s in new_reachable_spaces:
        #get its 6 neighbors (if on edge may have less)
        ngbrs = get_neighbors(s)
        
        for n in ngbrs:
            #if ngbr not in cubes AND ngbr not visited already
            if (n not in cubes) and (n not in reachable_spaces) and (n not in new_reachable_spaces):
                temp.add(n)
    
    #copy temp set spaces into new reachable spaces and into reachable spaces
    new_reachable_spaces = copy.deepcopy(temp)
    reachable_spaces = reachable_spaces.union(temp)
    

#count the number of exterior surfaces for each cube
num_ext_surfaces = 0
for c in cubes:
    num_ext_surfaces += surfaces_facing_ext(c)

print('Part 2:', num_ext_surfaces)


