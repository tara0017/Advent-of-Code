# day24

def read_file():
    global instructions
    
    f = open('day24.txt','r')
    for x in f:
        x = x.replace('se', ' se ')
        x = x.replace('sw', ' sw ')
        x = x.replace('ne', ' ne ')
        x = x.replace('nw', ' nw ')
        x = x.replace('ee', ' e e ')
        x = x.replace('ww', ' w w ')
        x = x.replace('we', ' w e ')
        x = x.replace('ew', ' e w ')
        x = x.strip()
        x = x.split(' ')
        instructions.append(x)
    

def process_instructions():
    global grid, instructions

    for line in instructions:
        (x,y) = (0,0)
        
        for direction in line:
            if direction   == 'e':
                x += 2
            elif direction == 'w':
                x -= 2
            elif direction == 'sw':
                x -= 1
                y -= 1
            elif direction == 'nw':
                x -= 1
                y += 1
            elif direction == 'se':
                x += 1
                y -= 1
            elif direction == 'ne':
                x += 1
                y += 1

        # check if coordinate is already in grid dictionary
        if (x,y) in grid:
            if grid[(x,y)] == 1:    # currently black
                grid[(x,y)] = 0
            else:                   # currently white
                grid[(x,y)] = 1
                
        else:       # new point
            grid[(x,y)] = 1
            
            
def count_black_tiles():
    global grid
    count = 0
    
    for p in grid:
        if grid[p] == 1:
            count += 1
    return count


def count_neighbors(p):
    global grid

    count = 0
    (x,y) = p
                # e         se          sw          w       nw          ne
    neighbors = [(x+2,y), (x+1,y-1), (x-1,y-1), (x-2,y), (x-1,y+1), (x+1,y+1)]

    for n in neighbors:
        try:
            if grid[n] == 1:
                count += 1
        except:
            continue

    return count

    
def flip_tiles(grid_size):
    global grid

    tiles_to_flip = []
    # grid range x:
    for x in range(-grid_size, grid_size + 1):
        for y in range(-grid_size, grid_size + 1):
            p = (x,y)
            
            # make sure point is in grid
            if p not in grid:
                grid[p] = 0

            n = count_neighbors(p)

            if grid[p] == 1:    # black tile
                if n == 0 or n > 2:
                    tiles_to_flip.append(p)
            else:               # white tile
                if n == 2:
                    tiles_to_flip.append(p)

    # flip tiles in tiles_to_flip
    for p in tiles_to_flip:
        if grid[p] == 0:
            grid[p] = 1
        else:
            grid[p] = 0
    
        


# global variables
instructions = []
grid         = dict()

read_file()
process_instructions()

# part 1
print('Part 1')
print(count_black_tiles())


# part 2
for day in range(1,101):
    flip_tiles(25 + day)

print('Part 2')
print(count_black_tiles())


