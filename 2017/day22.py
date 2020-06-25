#day22
import math

def read_row(r, y):
    global grid
    for x in range(len(r)):
        point = (x, y)
        value = r[x]
        if value == '#' or value == '.':
            grid[point] = value
    
def turn(direction):
    global location, facing
    loc = list(location)
    
    if direction == 'right':
        facing = (facing+1) % 4
    elif direction == 'left':
        facing = (facing-1) % 4
    elif direction == 'reverse':
        facing = (facing+2)%4
    #'straight' does not need to alter direction
        
    if facing == 0:
        loc[1] -= 1
    elif facing == 1:
        loc[0] += 1
    elif facing == 2:
        loc[1] += 1
    elif facing == 3:
        loc[0] -= 1
    location = tuple(loc)

def print_grid():
    global grid
    for y in range(-5, 5):
        for x in range(-5, 5):
            p = (x, y)
            if p == location:
                print('s ', end = '')
            elif p not in grid:
                print('. ', end = '')
            else:
                print(grid[p], end = ' ')
        print()


f = open('day22_input.txt', 'r')
grid = {}

y = 0
for r in f:
    read_row(r, y)
    y += 1

"""
for p in grid:
    print(p, grid[p])
"""    

mid = (int(math.sqrt(len(grid))/2))
location = (mid, mid)
steps = 10**7   #100
facing = 0  #0 = up     1 = right   2 = down    3 = left
infections = 0


for i in range(steps):
    #print_grid()
    #print(facing)
    #print()
    if location not in grid:
        grid[location] = '.'
        
    if grid[location] == '#':
        grid[location] = 'F'
        turn('right')
    elif grid[location] == '.':
        grid[location] = 'W'
        turn('left')
    elif grid[location] == 'F':
        grid[location] = '.'
        turn('reverse')
    elif grid[location] == 'W':
        grid[location] = '#'
        turn('straight')
        infections += 1


print(infections)
