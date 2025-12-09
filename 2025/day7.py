# Day 7

def drop_one_level():
    global splits, grid, beams

    new_beams = set()
    for b in beams:
        y,x = b

        if grid[y+1][x] == '^':
            new_beams.add((y+1, x-1))
            new_beams.add((y+1, x+1))
            splits += 1
        else:
            new_beams.add((y+1, x))            

    beams = new_beams




    
def drop_one_level2():
    global grid, beams2

    new_beams = dict()
    for b,v in beams2.items():
        y,x = b

        if grid[y+1][x] == '^':
            if (y+1, x-1) in new_beams:
                new_beams[(y+1, x-1)] += v
            else:
                new_beams[(y+1, x-1)] = v
            
            if (y+1, x+1) in new_beams:
                new_beams[(y+1, x+1)] += v
            else:
                new_beams[(y+1, x+1)] = v


        else:
            if (y+1, x) in new_beams:
                new_beams[(y+1, x)] += v
            else:
                new_beams[(y+1, x)] = v


    #print('nb ', new_beams)
    beams2 = new_beams

    
grid  = []
beams = set()
beams2 = dict()

f = open('day7.txt','r')
for x in f:
    x = x.strip()
    if len(grid) == 0:
        b = x.index('S')
        beams.add((0,b))
        beams2[(0,b)] = 1
    grid.append(x)

"""
print(beams)
for g in grid:
    print(g)
"""

# Part 2
level  = 0
print(len(grid))

while level < len(grid) - 1:
    level +=1
    drop_one_level2()
    print(level)
    #print(beams2)

count = 0
for k,v in beams2.items():
    count += v
print(count)

"""
# Part 1
level  = 0
splits = 0
while level < len(grid) - 1:
    level +=1
    drop_one_level()
    
print(splits)    
"""


