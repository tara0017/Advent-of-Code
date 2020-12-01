# day14

def get_dist(d):
    reps = 2503 // (d[2] + d[3])
    dist = reps * d[1] * d[2]

    time = reps*(d[2] + d[3]) + 1
    for i in range(time, time + d[2]):
        if i > 2503:
            break
        dist += d[1]

    return dist


def award_points():
    global d, points
    
    lead = max(d)
    for i in range(len(d)):
        if d[i] == lead:
            points[i] += 1


def track_points():
    global names, d, points, instructions
    
    for time in range(2503):
        for x in instructions:      # [name, speed, duration, rest]
            if time % (x[2] + x[3]) < x[2]:  # moving
                i = names.index(x[0])
                d[i] += x[1]
            else:                           # resting
                continue
        award_points()


# global variables
names  = [] 
d      = []
points = []      
instructions = []

f = open('day14.txt', 'r')
for x in f:
    x = x.split()
    
    names.append(x[0])  # add each reindeer name
    d.append(0)         # initialize distance to 0
    points.append(0)    # initialize points to 0
    
    data = [x[0], int(x[3]), int(x[6]), int(x[-2])]     # [name, speed, duration, rest]
    instructions.append(data)

    # part 1
    # print(get_dist(data))



track_points()
print(max(points))



    
