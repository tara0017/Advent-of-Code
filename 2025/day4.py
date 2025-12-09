# Day 4
def num_neighbors(p):
    global rolls

    ngbrs = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i,j) == (0,0):
                continue

            if (p[0] + i,p[1] + j) in rolls:
                ngbrs += 1

    return ngbrs


    
rolls = set()

row = 0
f = open('day4.txt','r')
for x in f:
    x = x.strip()
    #print(x)
    for col in range(len(x)):
        if x[col] == '@':
            rolls.add((row, col))
    row += 1


#Part 1
count = 0
for p in rolls:
    if num_neighbors(p) < 4:
        count += 1
        
print(count)


#Part 2
count2 = 0
ngbrs_removed = True

while ngbrs_removed:
    ngbrs_removed = False
    rolls_to_remove = set()
    
    for p in rolls:
        if num_neighbors(p) < 4:
            rolls_to_remove.add(p)

    if len(rolls_to_remove) > 0 :
        ngbrs_removed = True
        for p in rolls_to_remove:
            rolls.remove(p)
            count2 += 1

print(count2)
