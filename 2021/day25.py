# day 25
def get_east_moving():
    global grid
    e_movable = set()
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '>':
                # edge case
                if x == len(grid[0]) - 1:
                    if grid[y][0] == '.':
                        e_movable.add((y,x))
                # is next spot open
                elif grid[y][x+1] == '.':
                    e_movable.add((y,x))
                    
    return e_movable


def get_south_moving():
    global grid
    s_movable = set()
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'v':
                # edge case
                if y == len(grid) - 1:
                    if grid[0][x] == '.':
                        s_movable.add((y,x))
                # is next spot open
                elif grid[y+1][x] == '.':
                    s_movable.add((y,x))
                    
    return s_movable


def move_east(s):
    global grid

    for p in s:
        (y,x) = p
        
        grid[y][x] = '.'

        if x == len(grid[0]) - 1:   # edge case
            grid[y][0] = '>'
        else:
            grid[y][x+1] = '>'


def move_south(s):
    global grid

    for p in s:
        (y,x) = p
        
        grid[y][x] = '.'

        if y == len(grid) - 1:   # edge case
            grid[0][x] = 'v'
        else:
            grid[y+1][x] = 'v'
            

grid = []

f = open('day25.txt','r')
for x in f:
    row = []
    x = x.strip()
    for c in x:
        row.append(c)
    grid.append(row)


step = 0
while True:
    step += 1
    
    east_set = get_east_moving()
    #print(east_set)
    move_east(east_set)

    south_set = get_south_moving()
    #print(south_set)
    move_south(south_set)

    if len(east_set) == 0 and len(south_set) == 0:
        print('Number of steps:', step)
        break





