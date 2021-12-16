# day 15
import copy

def value_above(p):
    global risk_value, grid
    return (risk_value[p] + grid[p[0] - 1][p[1]])

def value_below(p):
    global risk_value, grid
    return (risk_value[p] + grid[p[0] + 1][p[1]])
  
def value_left(p):
    global risk_value, grid
    return (risk_value[p] + grid[p[0]][p[1] - 1])

def value_right(p):
    global risk_value, grid
    return (risk_value[p] + grid[p[0]][p[1] + 1])


    
def find_risk_values():
    global risk_value, grid
    points_to_check     = [(0,0)]

    while len(points_to_check) > 0:
        new_points_to_check = []

        for p in points_to_check:
            (y,x) = p
            
            #update point above
            if y > 0:   # not top row
                v = value_above(p)
                p_above = (y-1, x)
                if p_above not in risk_value:     #first time point appears
                    risk_value[p_above] = v
                    new_points_to_check.append(p_above)
                elif v < risk_value[p_above]:     #new path is cheaper than previous path
                    risk_value[p_above] = v
                    new_points_to_check.append(p_above)
                
            #update point below
            if y < (len(grid) - 1):   # not bottom row
                v = value_below(p)
                p_below = (y+1, x)
                if p_below not in risk_value:     #first time point appears
                    risk_value[p_below] = v
                    new_points_to_check.append(p_below)
                elif v < risk_value[p_below]:     #new path is cheaper than previous path
                    risk_value[p_below] = v
                    new_points_to_check.append(p_below)
                    
            #update point to left
            if x > 0:   # not first column
                v = value_left(p)
                p_left = (y, x-1)
                if p_left not in risk_value:     #first time point appears
                    risk_value[p_left] = v
                    new_points_to_check.append(p_left)
                elif v < risk_value[p_left]:     #new path is cheaper than previous path
                    risk_value[p_left] = v
                    new_points_to_check.append(p_left)
                
            #update point to right
            if x < (len(grid[0]) - 1):   # not last column
                v = value_right(p)
                p_right = (y, x+1)
                if p_right not in risk_value:     #first time point appears
                    risk_value[p_right] = v
                    new_points_to_check.append(p_right)
                elif v < risk_value[p_right]:     #new path is cheaper than previous path
                    risk_value[p_right] = v
                    new_points_to_check.append(p_right)

        points_to_check = new_points_to_check
        
# part 1
def part1():
    global grid
    find_risk_values()
    print('Part 1:', risk_value[(len(grid) - 1), len(grid[0]) - 1])




# part 2
def part2():
    global grid
    
    # expand grid to the right 4 times
    expanded_grid = copy.deepcopy(grid)
    for i in range(1,5):
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                original_v = grid[y][x]
                new_v      = original_v + i
                while new_v > 9:
                    new_v -= 9
                    
                expanded_grid[y].append(new_v)


    grid = copy.deepcopy(expanded_grid)
    # expand grid down 4 times
    for i in range(1,5):
        for y in range(len(grid)):
            new_row = []
            for x in range(len(grid[0])):
                original_v = grid[y][x]
                new_v      = original_v + i
                while new_v > 9:
                    new_v -= 9

                new_row.append(new_v)   
            expanded_grid.append(new_row)

    grid = copy.deepcopy(expanded_grid)   
        


    find_risk_values()
    print('Part 2:', risk_value[(len(grid) - 1), len(grid[0]) - 1])



grid = []
risk_value = dict()
risk_value[(0,0)] = 0


f= open('day15.txt')
for x in f:
    x = x.strip()
    row = []
    for c in x:
        row.append(int(c))
    grid.append(row)






#part1()
part2()




