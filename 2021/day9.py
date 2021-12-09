# day 9
import copy

def get_point(y,x):
    global grid

    # edge points
    if x < 0 or y < 0:
        return 10
    if x >= len(grid[0]) or y >= len(grid):
        return 10

    return int(grid[y][x])

def part1():
    low_points = dict()

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            height = int(grid[y][x])
            # check if point is smaller than point above
            if height >= get_point(y-1,x):
                continue
            
            # check if point is smaller than point below
            if height >= get_point(y+1,x):
                continue
                
            # check if point is smaller than point to the left
            if height >= get_point(y,x-1):
                continue
            
            # check if point is smaller than point to the right
            if height >= get_point(y,x+1):
                continue

            low_points[(y,x)] = height

    # calculate sum of low points (risk_level)
    risk_level = 0
    for k,v in low_points.items():
        risk_level += (1+v)

    print('Risk level =', risk_level)


# looks at all adjacent points mapping out the basin,
# determines basin size,
# converts these points to a height of 9, returns size
def get_basin_size(y,x):
    points_to_test = set()
    points_to_test.add((y,x))
    new_points     = set() 
    size           = 1

    row = grid[y]
    row = row[:x] + '9' + row[x + 1:]
    grid[y] = row
    
    while True:
        for point in points_to_test:
                
            # check surrounding points
            if get_point(point[0]-1,point[1]) < 9:    #point above
                new_points.add((point[0]-1,point[1]))
                
            if get_point(point[0]+1,point[1]) < 9:    #point below
                #if point == (0, 6):
                #    print('now here')
                new_points.add((point[0]+1,point[1]))
                
            if get_point(point[0],point[1]-1) < 9:    #point left
                new_points.add((point[0],point[1]-1))
                
            if get_point(point[0],point[1]+1) < 9:    #point right
                new_points.add((point[0],point[1]+1))

        if len(new_points) == 0:    # no more new points
            return size
        else:                       # new points found
            # change the height of these new points to 9
            for point in new_points:
                row = grid[point[0]]
                row = row[:point[1]] + '9' + row[point[1] + 1:]
                grid[point[0]] = row
                
            size += len(new_points)
            points_to_test = copy.deepcopy(new_points)
            new_points.clear()
    

def part2():
    basin_sizes = []
    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            height = int(grid[y][x])
            if height == 9:
                continue
            else:
                basin_sizes.append(get_basin_size(y,x))
    
    basin_sizes.sort()
    print('Largest basins:', basin_sizes[-1], basin_sizes[-2], basin_sizes[-3])
    print('Product =', basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])



grid = []
f = open('day9.txt','r')
for x in f:
    x = x.strip()
    #x = x.split()
    grid.append(x)


     
part1()
part2()

