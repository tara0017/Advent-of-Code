#day10
import math
def read_data():
    f = open("day10_input.txt", "r")
    data = []
    
    for line in f:
        data.append(line.strip())
    return data


def locate_asteroids():
    global data
    locations = []
    row = 0
    
    for line in data:
        col = 0
        for char in line:
            if char == "#":
                locations.append((col, row))
            col += 1
        row += 1
    return locations


def find_gcf(a, b):
    while(b): 
        a, b = b, a % b 
    return a


def is_visible(p1, p2):
    global locations
    delta_x = p2[0] - p1[0]
    delta_y = p2[1] - p1[1]
    gcf = find_gcf(abs(delta_x), abs(delta_y))
    if gcf == 1:
        return True
    else:
        delta_x = int(delta_x / gcf)
        delta_y = int(delta_y / gcf)
        (x, y) = (p1[0] + delta_x, p1[1] + delta_y)
        while (x, y) != p2:
            if (x, y) in locations:
                return False
            (x, y) = (x + delta_x, y + delta_y)
        return True

    
data                   = read_data()
locations              = locate_asteroids()
most_visible_asteroids = 0

#part2
def dot(p1, p2):
    return (p1[0]*p2[0] +p1[1]*p2[1])

def mag_product(p1, p2):
    return (norm(p1)*norm(p2))

def norm(p):
    return (math.sqrt(p[0]**2 + p[1]**2))

def find_angle(p1, p2):
    p1 = (p1[0], 25 - p1[1])
    p2 = (p2[0], 25 - p2[1])

    v1 = (0, 1)
    v2 = (p2[0]-p1[0], p2[1] - p1[1])
    
    d = dot(v1, v2)
    m = mag_product(v1, v2)
    return math.acos(d/m)
    
point_0 = (20, 21)    #(11, 13) #practice data
laser_visible_asteroids = []
for point_1 in locations:
    if point_0 == point_1:  #same point
        continue
    else:
        if is_visible(point_0, point_1):
            laser_visible_asteroids.append(point_1)

angles = []
for point in laser_visible_asteroids:
    if point[0] < point_0[0] and point[1] < point_0[1]:
        a = find_angle(point_0, point)
        angles.append((point[0], point[1], a))

    
astr = sorted(angles, key = lambda x: x[2])
print (astr[47])             #247 visible asteroids - 47th from end of visible


"""
#part1
for point_0 in locations:
    visible_asteroids = 0
    for point_1 in locations:
        if point_0 == point_1:  #same point
            continue
        else:
            if is_visible(point_0, point_1):
                visible_asteroids += 1
    if visible_asteroids > most_visible_asteroids:
        most_visible_asteroids = visible_asteroids
        print(point_0, visible_asteroids)
"""
