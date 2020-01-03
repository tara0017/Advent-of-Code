#day3
class point:
    def __init__(self, x, y, steps):
        self.x = x
        self.y = y
        self.steps = steps

        
#part2
def vertical(move):
    global current_location, path1, steps
    length = int(move[1:])
    change = 1
    if move[0] == "D":
        change = -1
    for i in range(length):
        steps += 1
        current_location[1] += change
        path1[current_location[0]].add(current_location[1])
        p = point(current_location[0], current_location[1], steps)
        points.append(p)


def horizontal(move):
    global current_location, path1, steps
    length = int(move[1:])
    change = 1
    if move[0] == "L":
        change = -1
    for i in range(length):
        steps += 1
        current_location[0] += change
        if current_location[0] in path1:
            path1[current_location[0]].add(current_location[1])
        else:
            s = set()
            s.add(current_location[1])
            path1[current_location[0]] = s
        p = point(current_location[0], current_location[1], steps)
        points.append(p)



def check_vertical(move):
    global current_location, path1, smallest_dist, steps
    length = int(move[1:])
    change = 1
    if move[0] == "D":
        change = -1
    for i in range(length):
        steps += 1
        current_location[1] += change
        check_num_steps()


def check_horizontal(move):
    global current_location, path1, smallest_dist, steps
    length = int(move[1:])
    change = 1
    if move[0] == "L":
        change = -1
    for i in range(length):
        steps += 1
        current_location[0] += change
        check_num_steps()



def check_num_steps():
    global current_position, steps, points, least_steps

    if current_location[0] in path1:    #x is in path1
        if current_location[1] in path1[current_location[0]]: #(x, y) in path

            total_steps = steps + get_steps_from_path1()
            if total_steps < least_steps[0] and total_steps > 0: 
                least_steps[0] = total_steps
                least_steps[1] = current_location[0]
                least_steps[2] = current_location[1]


def get_steps_from_path1():
    global points, current_location

    for p in points:
        if p.x == current_location[0] and p.y == current_location[1]:
            return p.steps
        

                    

f = open("day3_input.txt", "r") 
data = []
least_steps = [10**6, 0, 0]
points = []
steps = 0

for i in f:
    data.append(i)

p1 = data[0].split(',')
p2 = data[1].split(',')

"""
#practice input data
p1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
p2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
p1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
p2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
"""


current_location = [0,0]
path1 = {}      # x: set of y-coordinates
s = set()
s.add(0)
path1[0] = s

#find coordinates for 1st path
for move in p1:
    if move[0] == "R" or move[0] == "L":
        horizontal(move)
    else:
        vertical(move)


steps = 0
#check 2nd path for duplicate points
current_location = [0,0]
for move in p2:
    if move[0] == "R" or move[0] == "L":
        check_horizontal(move)
    else:
        check_vertical(move)
    

print(least_steps)



"""
#part 1
def vertical(move):
    global current_location, path1
    length = int(move[1:])
    change = 1
    if move[0] == "D":
        change = -1
    for i in range(length):
        current_location[1] += change
        path1[current_location[0]].add(current_location[1])


def horizontal(move):
    global current_location, path1
    length = int(move[1:])
    change = 1
    if move[0] == "L":
        change = -1
    for i in range(length):
        current_location[0] += change
        if current_location[0] in path1:
            path1[current_location[0]].add(current_location[1])
        else:
            s = set()
            s.add(current_location[1])
            path1[current_location[0]] = s



def check_vertical(move):
    global current_location, path1, smallest_dist
    length = int(move[1:])
    change = 1
    if move[0] == "D":
        change = -1
    for i in range(length):
        current_location[1] += change
        check_dist()



def check_horizontal(move):
    global current_location, path1, smallest_dist
    length = int(move[1:])
    change = 1
    if move[0] == "L":
        change = -1
    for i in range(length):
        current_location[0] += change
        check_dist()



def check_dist():
    global current_location, smallest_dist
    
    if current_location[0] in path1:    #x is in path1
        if current_location[1] in path1[current_location[0]]: #(x, y) in path
            dist = abs(current_location[0]) + abs(current_location[1])
            if dist < smallest_dist[0] and dist > 0:    #closer to origin
                smallest_dist[0] = dist
                smallest_dist[1] = current_location[0]
                smallest_dist[2] = current_location[1]




                    

f = open("day3_input.txt", "r") 
data = []
smallest_dist = [10**6,0,0]

for i in f:
    data.append(i)

p1 = data[0].split(',')
p2 = data[1].split(',')


current_location = [0,0]
path1 = {}      # x: set of y-coordinates
s = set()
s.add(0)
path1[0] = s

#find coordinates for 1st path
for move in p1:
    if move[0] == "R" or move[0] == "L":
        horizontal(move)
    else:
        vertical(move)


#check 2nd path for duplicate points
current_location = [0,0]
for move in p2:
    if move[0] == "R" or move[0] == "L":
        check_horizontal(move)
    else:
        check_vertical(move)
    

print(smallest_dist)
"""
