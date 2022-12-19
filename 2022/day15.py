#day15

class beacon:
    def __init__(self, x, y, nearby_sensors):
        self.x = x
        self.y = y
        self.beacon = beacon
        self.nearby_sensors = nearby_sensors

class sensor:
    def __init__(self, x, y, nearest_beacon, dist_to_beacon = 0):
        self.x = x
        self.y = y
        self.nearest_beacon = nearest_beacon
        self.dist_to_beacon = dist_to_beacon


beacons = set()
sensors = set()
no_beacons = set()
beacon_loc = set()
row = 2000000 

f = open('day15.txt', 'r')
for t in f:
    t = t.strip()
    t = t.replace(':', '')
    t = t.replace(',', '')
    t = t.replace('=', ' ')
    t = t.split()

    b_x = int(t[-3])
    b_y = int(t[-1])
    s_x = int(t[3])
    s_y = int(t[5])

    #has beacon already been created
    is_new_beacon = True
    for b in beacons:
        if b.x == b_x and b.y == b_y:
            is_new_beacon = False
            #create sensor
            s = sensor(s_x, s_y, b)
            b.nearby_sensors.add(s)
            
            sensors.add(s)
            break

    #new beacon
    if is_new_beacon:
        b = beacon(b_x, b_y, set())
        beacons.add(b)
        s = sensor(s_x, s_y, b)
        b.nearby_sensors.add(s)
        beacon_loc.add((b_x,b_y))

        sensors.add(s)

def get_dist(x1, y1, x2, y2):
    horiz = abs(x2 - x1)
    vert  = abs(y2 - y1)
    return (horiz + vert)

     


"""
#part 1
for s in sensors:
    dist_to_beacon = get_dist(s.x,s.y, s.nearest_beacon.x, s.nearest_beacon.y)

    #get vertical distance to row
    dist_to_row = abs(row - s.y)

    for i in range(dist_to_beacon - dist_to_row + 1):
        point_to_left = (s.x - i, row)
        point_to_right = (s.x + i, row)

        if point_to_left not in beacon_loc:
            no_beacons.add(point_to_left)
        if point_to_right not in beacon_loc:
            no_beacons.add(point_to_right)

print(len(no_beacons))
"""


#part 2
p_max = 4000000

def get_points_beyond(s, d):

    points = set()
    for i in range(d + 1):
        p1x = s.x + i
        p1y = s.y + (d - i)
        points.add((p1x,p1y))
        
        p2x = s.x - i
        p2y = s.y - (d - i)
        points.add((p2x,p2y))

        p3x = s.x + i
        p3y = s.y - (d - i)
        points.add((p3x,p3y))

        p4x = s.x - i
        p4y = s.y + (d - i)
        points.add((p4x,p4y))

    return points

        
    

#points beyond the beacon distance and the frequancy in which they occur
border_points = dict()

#locate all the points 1 distance beyond the beacon dist
for s in sensors:
    
    dist_to_beacon = get_dist(s.x,s.y, s.nearest_beacon.x, s.nearest_beacon.y)
    s.dist_to_beacon = dist_to_beacon
    
    points_beyond_beacon_range = get_points_beyond(s, 1 + dist_to_beacon)
    
    for p in points_beyond_beacon_range:
        if p[0] < 0 or p[0] > p_max or p[1] < 0 or p[1] > p_max:
            continue
        else:
            #track frequancy of each point being a border point
            if p in border_points:
                border_points[p] += 1
            else:
                border_points[p] = 1
    

candidates = set()
for k,v in border_points.items():
    if v >= 4 and (4000000*k[0] + k[1]) > 6060440970092:
        is_point_found = True
        
        #for each sensor, distance between sensor and point must be larger than dist between sensor and beacon
        for s in sensors:
            dist_to_candidate = get_dist(k[0], k[1], s.x, s.y)
            if s.dist_to_beacon >= dist_to_candidate:
                is_point_found = False
                break

        if is_point_found == True:
            print('Part 2:', k, 4000000*k[0] + k[1])
            break

    
