#day1
def add_locations(a, b):
    global locations
    if a[0] == b[0]:    #same x value, y changes
        if b[1] > a[1]:
            start = 1
            stop = b[1] - a[1]
        else:
            start = b[1] - a[1]
            stop = -1
        for i in range(start, stop+1):
            p = [a[0], a[1] + i]
            if tuple(p) in locations:
                print(p)
                return 1
            else:
                locations.add(tuple(p))
    else:    #same y value, x changes
        if b[0] > a[0]:
            start = 1
            stop = b[0] - a[0]
        else:
            start = b[0] - a[0]
            stop = -1
        for i in range(start, stop+1):
            p = [a[0] + i, a[1]]
            if tuple(p) in locations:
                print("!!!!!!!!!!!!!!!!",p)
                return 1
            else:
                locations.add(tuple(p))
    return 0


f= open('day1_input.txt', 'r')
for x in f:
    x = x.replace(',', '')
    inst = x.split()
    #print(inst)


locations = set()
location = [0,0]
#locations.add(location)
facing = 0      #0=up   1=right     2=down      3=left

for step in inst:
    old_location = location[:]
    if facing == 0:  #up
        if step[0] == 'R':
            facing = 1
            location[0] += int(step[1:])
        else:
            facing = 3
            location[0] -= int(step[1:])
    elif facing == 2:  #down
        if step[0] == 'R':
            facing = 3
            location[0] -= int(step[1:])
        else:
            facing = 1
            location[0] += int(step[1:])
    elif facing == 1:  #right
        if step[0] == 'R':
            facing = 2
            location[1] -= int(step[1:])
        else:
            facing = 0
            location[1] += int(step[1:])
    elif facing == 3:  #left
        if step[0] == 'R':
            facing = 0
            location[1] += int(step[1:])
        else:
            facing = 2
            location[1] -= int(step[1:])
    #print(step, location, facing)
    if add_locations(old_location, location) == 1:
        break

print(location)


