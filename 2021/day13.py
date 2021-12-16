# day 13

def fold_up(y):
    global dots
    dots_to_move = []
    
    for d in dots:
        if d[1] > y:    #if the point is below the line
            dots_to_move.append(d)

    for d in dots_to_move:
        dots.remove(d)
        temp = (d[0], d[1] - 2*(d[1] - y))
        dots.add(temp)


def fold_left(x):
    global dots
    dots_to_move = []
    
    for d in dots:
        if d[0] > x:    #if the point is left of the line
            dots_to_move.append(d)

    for d in dots_to_move:
        dots.remove(d)
        temp = (d[0] - 2*(d[0] - x), d[1])
        dots.add(temp)



        
dots = set()
instructions = []
grid = []


f = open('day13.txt', 'r')
fold_inst = False
for x in f:
    if x == '\n':
        fold_inst = True
        continue
    if fold_inst:
        x = x.strip()
        x = x.split()
        x = x[2].split('=') 
        instructions.append(x)
    else:
        x = x.strip()
        x = x.split(',')
        x = (int(x[0]), int(x[1]))
        dots.add(x)


for i in instructions:
    if i[0] == 'y':
        fold_up(int(i[1]))
    else:
        fold_left(int(i[1]))
    



for y in range(6):
    for x in range(40):
        if (x,y) in dots:
            print('#', end = '')
        else:
            print(' ', end = '')
    print()










            


