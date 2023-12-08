#day 3

def get_num(x, y):
    global grid

    x_end = x
    while grid[y][x_end].isnumeric():
        x_end += 1
        if x_end >= len(grid[y]):
            break

    return grid[y][x:x_end]

    
def get_nums_symb():
    global numbers, symbols, grid

    for y in range(len(grid)):
        x = 0
        while x < len(grid[0]):
            p = grid[y][x]
            
            if p == '.':
                x += 1
                continue
            
            elif p.isnumeric():
                n = get_num(x, y)

                #add n to numbers
                coordinates = set()
                for i in range(len(n)):
                    coordinates.add((x + i, y))
                numbers[int(n), (x,y)] = coordinates                

                #adjust x to end of number location
                x += len(n)
                
            else:
                ###### part 2 ######
                if p == '*':
                    gears[(x,y)] = set()
                ####################
                
                symbols.add((x, y))
                x+= 1
                
def is_adjacent(n):
    global numbers, symbols, grid

    for coord in numbers[n]:
        (x,y) = coord
        #check row above
        if y > 0:
            if x > 0:                   #left
                if (x-1, y-1) in symbols:
                    return True
            if x < len(grid[0]) - 1:    #right
                if (x+1, y-1) in symbols:
                    return True
            if (x, y-1) in symbols:     #center
                return True
            
        #check row below
        if y < len(grid) - 1:
            if x > 0:                   #left
                if (x-1, y+1) in symbols:
                    return True
            if x < len(grid[0]) - 1:    #right
                if (x+1, y+1) in symbols:
                    return True
            if (x, y+1) in symbols:     #center
                return True

        #check left/right
        if x > 0 and (x-1, y) in symbols:                #left
            return True
        if x < len(grid[0]) - 1 and (x+1, y) in symbols: #right
            return True

    return False
            

#global variables
numbers = {}
symbols = set()
gears   = {}
grid = []

f = open('day3.txt','r')
for s in f:
    s = s.strip()
    grid.append(s)


get_nums_symb()


sum_of_parts = 0
for k in numbers:
    if is_adjacent(k):
        #print(k)
        sum_of_parts += k[0]

print('Part 1: ', sum_of_parts)


############## part 2 ###############

def populate_gear_neighbors():
    global numbers, gears, grid

    for n in numbers:
        for coord in numbers[n]:
            (x,y) = coord
            #check row above
            if y > 0:
                if x > 0:                   #left
                    if (x-1, y-1) in gears:
                        gears[(x-1, y-1)].add(n[0])
                        break
                if x < len(grid[0]) - 1:    #right
                    if (x+1, y-1) in gears:
                        gears[(x+1, y-1)].add(n[0])
                        break
                if (x, y-1) in gears:       #center
                    gears[(x, y-1)].add(n[0])
                    break
                
            #check row below
            if y < len(grid) - 1:
                if x > 0:                   #left
                    if (x-1, y+1) in gears:
                        gears[(x-1, y+1)].add(n[0])
                        break
                if x < len(grid[0]) - 1:    #right
                    if (x+1, y+1) in gears:
                        gears[(x+1, y+1)].add(n[0])
                        break
                if (x, y+1) in gears:       #center
                    gears[(x, y+1)].add(n[0])
                    break

            #check left/right
            if x > 0 and (x-1, y) in gears:                #left
                gears[(x-1, y)].add(n[0])
                break
            if x < len(grid[0]) - 1 and (x+1, y) in gears: #right
                gears[(x+1, y)].add(n[0])
                break

 


populate_gear_neighbors()

sum_of_gear_ratios = 0
for k,v in gears.items():
    if len(v) == 2:
        
        gear_ratio = 1
        for g in v:
            gear_ratio *= g    
        sum_of_gear_ratios += gear_ratio
        
print('Part 2: ', sum_of_gear_ratios)

    
