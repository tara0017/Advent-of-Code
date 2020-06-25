#day6_part2
def find_distance(point):
    global points
    d = 0
    for p in points:
        d += abs(point[0] - p[0])
        d += abs(point[1] - p[1])
    return d


#print (x_range)        # [42, 353]
#print (y_range)        # [60, 342]

letter = 65
points = []


f = open("day6_input.txt", "r")
for x in f:
    x = x.replace(",", "")
    x = x.split()
    p = [int(x[0]), int(x[1]), chr(letter)]
    letter += 1
    if letter == 91:
        letter = 97
    points.append(p)


dist_grid = {}



for y in range(60, 343):
    for x in range(42, 354):
        p = (x, y)
        dist_grid[p] = find_distance(p)

        
count = 0
for k,v in dist_grid.items():
    #print(k, v)
    
    if v < 10000:
        #print(k , v)
        count += 1
print("COUNT = ", count)
