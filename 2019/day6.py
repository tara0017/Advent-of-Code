#day6
def get_height(node):
    global nodes

    height = 0
    while node != "COM":
        height += 1
        node = nodes[node][0]
    return height

"""
{
node1: (parent, [children])
node2: (parent, [children])
}
"""
nodes = {}
f = open("day6_input.txt", "r")
for x in f:
    x = x[:-1]
    parent = x[:3]
    child  = x[4:]

    #handle parent
    if parent in nodes:     #parent already exists
        nodes[parent][1].append(child)
    else:                   #parent is a new node
        nodes[parent] = ("N-A", [child])
    #handle child
    nodes[child] = (parent, [])

orbits = 0
for node in nodes:
    orbits += get_height(node)
    """
    print(node, nodes[node])
    orbits += 1
    if orbits == 50 :
        break
    """
print (orbits)

#part2
"""
set orbital distance to 0
create orbital distance dictionary
get YOU's parent
set parent's distance to zero
find parent's parent set distance to 1
etc.
"""
def find_dist(a, z):
    global nodes
    
    orbital_dist = {}
    dist = 0
    n = a
    while n != "COM":
        n = nodes[n][0]     #set n to parent of n
        orbital_dist[n] = dist
        dist += 1

    dist = 0
    n = z
    while True:
        n = nodes[n][0]     #set n to parent of n
        if n in orbital_dist:
            print(dist, orbital_dist[n])
            return(dist + orbital_dist[n])
        dist += 1
 

print(find_dist("YOU", "SAN"))



    










