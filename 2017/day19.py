#day19
def read_line(line, y):
    global grid, steps
    for x in range(len(line)):
        if line[x] != ' ' and line[x] != '\n':
            p = (x, y)
            grid[p] = line[x]
  

def turn():
    global grid, facing, location
    x = location[0]
    y = location[1]
    if facing == 0 or facing == 2:  #facing up or down - check left/right    
        if (x-1, y) in grid:    #check left
            facing = 3
        else:
            facing = 1
    else:                           #facing left/right -  check up/down
        if (x, y-1) in grid:    #check above
            facing = 0
        else:
            facing = 2

def move_to_intersection():
    global location, facing, result, reached_end, grid, steps
    steps += 1
    
    if facing == 2:     #down - y increasing
        loc = list(location)
        loc[1] += 1
        location = tuple(loc)
        #print(grid[location])
        
        while grid[location] != '+':
            
            if grid[location] == '-' or grid[location] == '|':
                steps += 1
                loc = list(location)
                loc[1] += 1
                location = tuple(loc)
            else:
                steps += 1
                result += grid[location]
                loc = list(location)
                loc[1] += 1
                location = tuple(loc)
            if location not in grid:
                reached_end = True
                break
    elif facing == 0:     #up - y decreasing
        loc = list(location)
        loc[1] -= 1
        location = tuple(loc)
        while grid[location] != '+':
            
            if grid[location] == '-' or grid[location] == '|':
                steps += 1
                loc = list(location)
                loc[1] -= 1
                location = tuple(loc)
            else:
                steps += 1
                result += grid[location]
                loc = list(location)
                loc[1] -= 1
                location = tuple(loc)
            if location not in grid:
                reached_end = True
                break
            
    elif facing == 3:     #left - x decreasing
        loc = list(location)
        loc[0] -= 1
        location = tuple(loc)
        while grid[location] != '+':
        
            if grid[location] == '-' or grid[location] == '|':
                steps += 1
                loc = list(location)
                loc[0] -= 1
                location = tuple(loc)
            else:
                steps += 1
                result += grid[location]
                loc = list(location)
                loc[0] -= 1
                location = tuple(loc)
            if location not in grid:
                reached_end = True
                break
    elif facing == 1:     #right - x increasing
        loc = list(location)
        loc[0] += 1
        location = tuple(loc)
        while grid[location] != '+':
            
            if grid[location] == '-' or grid[location] == '|':
                steps += 1
                loc = list(location)
                loc[0] += 1
                location = tuple(loc)
            else:
                steps += 1
                result += grid[location]
                loc = list(location)
                loc[0] += 1
                location = tuple(loc)
            if location not in grid:
                reached_end = True
                break
                

grid = {}
location =  (113, 0)
facing = 2      #0 = up     1 = right   2 = down    3 = left
result = ''
reached_end = False
steps = 0

f = open('day19_input.txt', 'r')
y = 0
for x in f:
    #print (x)
    read_line(x, y)
    y += 1
    #break

#print(grid)



while True:
    #print(location, result)
    move_to_intersection()
    turn()
    if reached_end:
        break

print(result)
print(steps)
#15900 - 16329
