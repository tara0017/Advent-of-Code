#day13
def check_adjacent(point):
    global grid, visited
    adj_open_loc = []
    x = point[0]
    y = point[1]

    p = (x+1, y)
    if grid[p] == '.' and p not in visited:
        adj_open_loc.append(p)
        visited.add(p)
    p = (x, y+1)
    if grid[p] == '.' and p not in visited:
        adj_open_loc.append(p)
        visited.add(p)
    if x > 0:   #ensure no negative values
        p = (x-1, y)
        if grid[p] == '.' and p not in visited:
            adj_open_loc.append(p)
            visited.add(p)
    if y > 0:   #ensure no negative values            
        p = (x, y-1)
        if grid[p] == '.' and p not in visited:
            adj_open_loc.append(p)
            visited.add(p)

    return adj_open_loc



grid = {}

for x in range(50):
    for y in range(50):
        poly = x*x + 3*x + 2*x*y + y + y*y + 1352
        b = bin(poly)[2:]
        b = b.replace('0', '')
        if len(b) % 2 == 0:
            grid[(x, y)] = '.'
        else:
            grid[(x, y)] = '#'
        
#print(grid[(31,39)])        

start = (1,1)
end = (31, 39)
visited = set()
visited.add(start)
d = 0
distance = {}
distance[start] = d
newly_added_locations = [start]

while True:     #end not in visited:
    d += 1
    next_locations = []
    #find next set of points by looking at adjacent points not yet visited
    for p in newly_added_locations:
        next_locations += check_adjacent(p)
    #update newly_added_points
    newly_added_locations.clear()
    for p in next_locations:
        newly_added_locations.append(p)
        distance[p] = d
    #print(distance)
    if d == 50:
        break

print(len(distance))   
#print(distance[end])

