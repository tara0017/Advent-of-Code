def process_key2(line):
    global key2

    input_key = []
    output = []
    for i in range(len(line)):
        if i < 2:   #input
            if line[i][0] == '.':
                a = 0
            else:
                a = 1
            if line[i][1] == '.':
                b = 0
            else:
                b = 1
            in_key = add(a, b)
            input_key.append(in_key)
            
        else:       #output
            out = []
            for j in range(len(line[i])):
                if line[i][j] == '.':
                    out.append(0)
                else:
                    out.append(1)
            output.append(out)
    key2[tuple(input_key)] = output
    #print(key2)

def process_key3(line):
    global key3

    input_key = []
    output = []
    for i in range(len(line)):
        if i < 3:   #input
            if line[i][0] == '.':
                a = 0
            else:
                a = 1
            if line[i][1] == '.':
                b = 0
            else:
                b = 1
            if line[i][2] == '.':
                c = 0
            else:
                c = 1
            in_key = add3(a, b, c)
            input_key.append(in_key)
            
        else:       #output
            out = []
            for j in range(len(line[i])):
                if line[i][j] == '.':
                    out.append(0)
                else:
                    out.append(1)
            output.append(out)
    key3[tuple(input_key)] = output
    #print('==================================')
    #print(key3)
    
def add(a,b):
    result = []
    result.append(a)
    result.append(b)
    return tuple(result)

def add3(a,b, c):
    result = []
    result.append(a)
    result.append(b)
    result.append(c)
    return tuple(result)

def print_grid():
    global grid
    x = 0
    y = 0
    while True:
        while True:
            if grid[(x, y)] == 0:
                print('.', end = '')
            else:
                print('#', end = '')
            x += 1
            if (x, y) not in grid:
                break
        y += 1
        print()
        x = 0
        if (x, y) not in grid:
            break

def get_next_grid(size):
    global grid, next_grid
    x = 0
    y = 0
    while True:
        while True:
            get_block(x, y, size)
            x += size
            if (x, y) not in grid:
                break
        x = 0
        y += size
        if (x, y) not in grid:
            break
    grid = next_grid.copy()

    
def get_block(x, y, size):
    global grid, next_grid

    k = get_key(x, y, size)

    for i in range(len(k)):
        for j in range(len(k)):
            next_x = size*x + j
            next_y = size*y + i
            next_grid[(next_x,next_y)] = k[i][j]

def get_key(x, y, size):
    global key2, key3, grid
    points = []
    for i in range(size):
        p = []
        for j in range(size):
            p.append(grid[(x+j, y+i)])
        points.append(tuple(p))
    points = tuple(points)

    if size == 2:
        legend = key2
    else:
        legend = key3

    for item in legend:
        for p in points:
            key_found = True
            if p not in item:
                key_found = False
                break
        if key_found:
            return legend[item]


        

key2 = {}    #{ tuple((0,0), (0,0)): [[0,0,0],[0,0,0],[0,0,1]] } >>>> ../.. => .../.../..#
key3 = {}

f = open('day21_input.txt', 'r')
for x in f:
    x = x.replace('/', ' ')
    x = x.replace('=>', '')
    x = x.split()
    if len(x) == 5:
        process_key2(x)
    elif len(x) == 7:
        process_key3(x)
    #print(x)
    #print(len(x))

print(key2)
"""
.#.
..#
###
"""
grid = {}       #{(x,y): 1, ...  }
next_grid = {}

grid[(0,0)] = 0
grid[(1,0)] = 1
grid[(2,0)] = 0
grid[(0,1)] = 0
grid[(1,1)] = 0
grid[(2,1)] = 1
grid[(0,2)] = 1
grid[(1,2)] = 1
grid[(2,2)] = 1
#print(grid)
print_grid()


iterations = 0
while iterations < 5:
    if iterations % 2 == 0:
        get_next_grid(3)
    else:
        get_next_grid(2)
    print_grid()





            
                



            



