# day18
from copy import copy, deepcopy

def read_line(x):
    global light_map
    row = []
    for c in x:
        if c == '#':
            row.append(1)
        else:
            row.append(0)
    light_map.append(row)


def get_light_count(y,x):
    global light_map
    neighbor_light_count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            
            # ignore current point
            if i == 0 and j == 0:
                continue
            
            # ignore neighbors off the grid
            if y+i < 0 or x+j < 0 or y+i == len(light_map) or x+j == len(light_map):
                continue
            
            if light_map[y + i][x + j] == 1:
                neighbor_light_count += 1
                

    return neighbor_light_count

            
def count_lights():
    global light_map
    count = 0
    
    for row in light_map:
        for n in row:
            if n == 1:
                count += 1
    return count


def corner_lights_on():
    global light_map

    light_map[0][0]   = 1
    light_map[0][-1]  = 1
    light_map[-1][0]  = 1
    light_map[-1][-1] = 1
    

light_map = []

# read data and store in global map
f = open('day18.txt', 'r')
for x in f:
    x = x.replace('\n', '')
    read_line(x)


corner_lights_on()

next_map = deepcopy(light_map)

for step in range(100):
    #print(step)
    for y in range(len(light_map)):
        for x in range(len(light_map[0])):
            # get count for surrounding lights that are on
            n = get_light_count(y,x)

            if light_map[y][x] == 1:    #current light is on
                if n == 2 or n == 3:
                    next_map[y][x] = 1
                else:
                    next_map[y][x] = 0
            else:                       # current light is off
                if n == 3:
                    next_map[y][x] = 1
                else:
                    next_map[y][x] = 0

    light_map = deepcopy(next_map)
    corner_lights_on()
    #for row in light_map:
    #    print(row)
    #print()


print(count_lights())



    

