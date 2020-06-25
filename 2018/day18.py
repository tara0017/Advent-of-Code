#day18
import copy
def eval_adj_acres(point):
    global grid
    
    adj_points = [ ["trees", 0], ["lumberyards", 0], ["open", 0] ]
    x = point[0]
    y = point[1]
    
    #print(point, "(1, 0): ", grid[(1,0)])
    
    #points above
    for i in range(x-1, x+2):
        if (i, y-1) in grid:
            if grid[(i, y-1)] == "tree":
                adj_points[0][1] += 1
            elif grid[(i, y-1)] == "lumberyard":
                adj_points[1][1] += 1
            elif grid[(i, y-1)] == "open":
                adj_points[2][1] += 1
    #points below
    for i in range(x-1, x+2):
        if (i, y+1) in grid:
            if grid[(i, y+1)] == "tree":
                adj_points[0][1] += 1
            elif grid[(i, y+1)] == "lumberyard":
                adj_points[1][1] += 1
            elif grid[(i, y+1)] == "open":
                adj_points[2][1] += 1
    #point to left
    if (x-1, y) in grid:      
        if grid[(x-1, y)] == "tree":
            adj_points[0][1] += 1
        elif grid[(x-1, y)] == "lumberyard":
            adj_points[1][1] += 1
        elif grid[(x-1, y)] == "open":
            adj_points[2][1] += 1
    #point to right
    if (x+1, y) in grid:
        if grid[(x+1, y)] == "tree":
            adj_points[0][1] += 1
        elif grid[(x+1, y)] == "lumberyard":
            adj_points[1][1] += 1
        elif grid[(x+1, y)] == "open":
            adj_points[2][1] += 1
    return adj_points



def process_row(x):
    global grid, row

    item = ""
    for i in range(len(x)):
        if x[i] == "#":
            item = "lumberyard"
        elif x[i] == ".":
            item = "open"
        elif x[i] == "|":
            item = "tree"
        else:
            break
        point = (i, row)
        grid[point] = item
            
def convert_d_to_list(d):
    a = ()
    for k,v in d.items():
        p = (k,v)
        a += (p, )
    return a


row = 0
grid = {}
new_grid = {}
size = 50

f = open("day18_input.txt", "r")
for x in f:
    process_row(x)
    row += 1
    #print(grid)
    #break

#print(grid)

time = 0
new_grid = copy.deepcopy(grid)
#adj_acres = [ ["trees", num], ["lumberyards", num], ["open", num] ]

grids = {}
g = convert_d_to_list(grid)
grids[g] = time
#print(grids)

#part 2
#grid 551 is identical to grid (551 + 28*n) for any positive integer n
#grid 10**9 is identical to grid 552
while time < 552:
    for x in range(size):
        for y in range(size):
            point = (x, y)
            adj_acres = eval_adj_acres(point)
            if grid[point] == "open":
                if adj_acres[0][1] >= 3:
                    new_grid[point] = "tree"

            elif grid[point] == "tree":
                if adj_acres[1][1] >= 3:
                    new_grid[point] = "lumberyard"

            elif grid[point] == "lumberyard":
                if not (adj_acres[1][1] >= 1 and adj_acres[0][1] >= 1):
                    new_grid[point] = "open"
    time += 1
    grid = copy.deepcopy(new_grid)
    g = convert_d_to_list(grid)
    if g in grids:
        print("duplicate", time, grids[g])
    else:
        grids[g] = time




def find_trees_and_lumberyards():
    global grid
    t = 0
    l = 0
    for key in grid:
        if grid[key] == "tree":
            t += 1
        elif grid[key] == "lumberyard":
            l += 1
    return (t, l)
            


print(time)
(t, l) = find_trees_and_lumberyards()            
print(t, l, t*l)            












