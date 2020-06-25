#day18
def is_trap(x, y):
    global grid

    previous_row = []
    if (x-1, y-1) in grid:
        previous_row.append(grid[(x-1, y-1)])
    else:
        previous_row.append(0)

    if (x, y-1) in grid:
        previous_row.append(grid[(x, y-1)])
    else:
        previous_row.append(0)

    if (x+1, y-1) in grid:
        previous_row.append(grid[(x+1, y-1)])
    else:
        previous_row.append(0)
        
    
    if sum(previous_row) == 1:
        if previous_row[1] == 0:
            return 1
        else:
            return 0
    if sum(previous_row) == 2:
        if previous_row[1] == 1:
            return 1
        else:
            return 0
    return 0


data = '.^^..^...^..^^.^^^.^^^.^^^^^^.^.^^^^.^^.^^^^^^.^...^......^...^^^..^^^.....^^^^^^^^^....^^...^^^^..^'
#data = '.^^.^.^^^^'
grid = {}
safe_count = 0

y = 0
for x in range(len(data)):
    point = (x, y)
    if data[x] == '.':
        value = 0
        safe_count += 1
    else:
        value = 1
    grid[point] = value
    
print(grid)

for y in range(1, 400000):
    #print(safe_count)
    for x in range(len(data)):
        value = is_trap(x, y)
        grid[(x, y)] = value
        if value == 0:
            safe_count += 1
        #print(value, end = '')
        #remove old rows
        if (x, y-2) in grid:
            del grid[(x, y-2)]
    #print()
    
    

            
print(safe_count)


    

