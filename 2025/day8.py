# Day 8
import math

class junction_box:
    def __init__(self, coord, connections, distances):
        self.coord = coord                  #(x,y,z)
        self.connections = connections      #set(jb)
        self.distances = distances          #[(jb, dist)] sort by dist

    def get_dist(self):
        global junction_boxes

        x1,y1,z1 = self.coord
        for jb in junction_boxes:
            if self == jb:
                continue
            else:
                x2,y2,z2 = jb.coord
                dist = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
                self.distances.append((jb, dist))

        #sort by distance
        self.distances.sort(key = lambda item: item[1])
        """
        print('===== ', self.coord)
        for n in self.distances:
            print(n[0].coord, n[1])
        """


def get_closest_neighbors():
    global junction_boxes
    
    dist = math.inf
    nbrs = (None, None)

    for jb in junction_boxes:
        if jb.distances[0][1] < dist:
            dist = jb.distances[0][1]
            nbrs = (jb, jb.distances[0][0])
    return nbrs     # (jb1, jb2)



def merge_connections(jb1,jb2):
    s = {jb1, jb2}
    s = s.union(jb1.connections)
    s = s.union(jb2.connections)

    for jb in s:
        jb.connections = s
    
    

junction_boxes = []
f = open('day8.txt', 'r')
for x in f:
    x = x.strip()
    x = x.split(',')
    jb = junction_box((int(x[0]), int(x[1]), int(x[2])), set(), [])
    junction_boxes.append(jb)

for jb in junction_boxes:
    #print(jb.coord)
    jb.get_dist()


for num_connections in range(1000):
    jb1, jb2 = get_closest_neighbors()
    #print(jb1.coord, jb2.coord)
    
    jb1.distances.pop(0)
    jb2.distances.pop(0)
    merge_connections(jb1,jb2)

#find 3 largest circuits
largest = [] #(jb, size)

for jb in junction_boxes:
    #print(jb.coord, len(jb.connections))

    # if jb already in 3 largest
    jb_already_used = False
    for large in largest:
        if jb in large[0].connections:
            jb_already_used = True

    if not jb_already_used:
        # jb not in 3 largest connections
        # less than 3 circuits in largest
        if len(largest) < 3:
            largest.append((jb, len(jb.connections)))
            largest.sort(key = lambda item: item[1])

        #3 circuits in largest
        else:
            if len(jb.connections) > largest[2][1]:
                largest.append((jb, len(jb.connections)))
                largest.pop(0)
            elif len(jb.connections) > largest[1][1]:
                largest[0] = largest[1]
                largest[1] = (jb, len(jb.connections))
            elif len(jb.connections) > largest[0][1]:
                largest[0] = (jb, len(jb.connections))
        
product = 1            
for item in largest:
    product *= item[1]
    print(item[0].coord, item[1])
    
print(product)
    
###########################
#Part 2

def are_all_connected():
    global junction_boxes

    for jb in junction_boxes:
        if len(jb.connections) != len(junction_boxes):
            return False
    return True



while True:
    jb1, jb2 = get_closest_neighbors()
    #print(jb1.coord, jb2.coord)
    
    jb1.distances.pop(0)
    jb2.distances.pop(0)
    merge_connections(jb1,jb2)

    if are_all_connected():
        print(jb1.coord, jb2.coord, jb1.coord[0] * jb2.coord[0])
        break
############################



    
