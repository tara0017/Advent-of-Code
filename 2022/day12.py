#day12
class path:
    def __init__(self, location, num_steps): #[y,x], 0)
        self.location = location
        self.num_steps = num_steps


#returns a list of ngbrs 1 away from current location and within height 
def get_neighbors(p):
    global grid
    
    [y,x] = p.location
    ngbrs = []

    #point above
    if y != 0:
        if ord(grid[y-1][x]) - ord(grid[y][x]) <= 1:
            ngbrs.append([y-1, x])
    #point below
    if y != len(grid) - 1:
        if ord(grid[y+1][x]) - ord(grid[y][x]) <= 1:
            ngbrs.append([y+1, x])
    #point to left
    if x != 0:
        if ord(grid[y][x-1]) - ord(grid[y][x]) <= 1:
            ngbrs.append([y, x-1])
    #point to right
    if x != len(grid[0]) - 1:
        if ord(grid[y][x+1]) - ord(grid[y][x]) <= 1:
            ngbrs.append([y, x+1])

    return ngbrs


#BFS
def get_shortest_path():
    global paths, end
    
    while len(paths) > 0:
        p = paths.pop(0)
        ngbrs = get_neighbors(p)
        
        for n in ngbrs:
            #reached the end
            if n == end:
                return p.num_steps + 1
            #check if this is a new location and if so add it to path
            else:
                if tuple(n) in visited:
                    continue
                else:
                    new_p = path(n, p.num_steps + 1)
                    visited.add(tuple(n))
                    paths.append(new_p)
        

start   = []
end     = []
grid    = []
paths   = []
visited = set()


f = open('day12.txt')
for x in f:
    x = x.strip()
    if 'S' in x:
        start_y = len(grid)
        start_x = x.index('S')
        start = [start_y, start_x]
        x = x.replace('S', 'a')
    if 'E' in x:
        end_y = len(grid)
        end_x = x.index('E')    
        end = [end_y, end_x]
        x = x.replace('E', 'z')
    grid.append(x)


#add start to paths
s = path(start, 0)
paths.append(s)
visited.add(tuple(start))


#part1
print('Part 1:', get_shortest_path())



#part2
min_path = 1000
print('Part 2:')
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == 'a':
            #reset variables
            paths.clear()
            visited.clear()

            start = [y,x]
            s = path(start, 0)
            paths.append(s)
            visited.add(tuple(start))
            length = get_shortest_path()
            if length != None and length < min_path:
                print(start, length)
                min_path = length
            





