#day8
def rect(x, y):
    global grid
    x = int(x)
    y = int(y)
    for i in range(x):
        for j in range(y):
            grid[(i, j)] = 1

def rotate(a, n):
    global grid
    n = int(n)

    if a[0] == 'y':
        new_row = []
        
        row = int(a[2:])
        print(row)
        for i in range(50):
            #print('i=', i+n+1)
            new_row.append(grid[(-n + i)%50, row])
        for i in range(50):
            grid[(i, row)] = new_row[i]
    else:
        new_col = []
        
        col = int(a[2:])
        for i in range(6):
            new_col.append(grid[col, (-n+i)%6])
        for i in range(6):
            grid[(col, i)] = new_col[i]

def print_grid():
    global grid
    for y in range(6):
        for x in range(50):
            p = (x, y)
            print(grid[p], end = '')
        print()
        
def print_grid2():
    global grid
    for y in range(6):
        for x in range(50):
            p = (x, y)
            if grid[p] == 1:
                print('X', end = '')
            else:
                print(' ', end = '')
            if x%5 == 4:
                print('     ', end = '')

        print()
        
        
grid = {}
for x in range(50):
    for y in range(6):
        p = (x,y)
        grid[p] = 0
        

f = open('day8_input.txt','r')
for x in f:
    x = x.split()
    if len(x) == 2:
        x = x[1].replace('x', ' ').split()
        rect(int(x[0]), int(x[1]))
        #print(x)
        #print_grid()
    else:
        rotate(x[2], x[4])
        #print(x)
        #print_grid()
        #break

print_grid()

count = 0
for x in range(50):
    for y in range(6):
        if grid[(x, y)] == 1:
            count += 1

print(count)

print_grid2()
        
