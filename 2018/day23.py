#day23
def is_in_range(n):
    global point_with_largest_range
    distance = 0
    for i in range(3):
        distance += abs(point_with_largest_range[i] - n[i])
    if distance <= point_with_largest_range[-1]:
        return True
    return False

grid = []
largest_range = 0
x_range = [0,0]
y_range = [0,0]

f = open("day23_input.txt", "r")
for x in f:
    x = x.replace("pos=<", " ")
    x = x.replace(",", " ")
    x = x.replace(">", " ")
    x = x.replace("r=", " ")
    x = x.split()
    point = [int(x[0]), int(x[1]), int(x[2]), int(x[3])]
    grid.append(point)
    if point[-1] > largest_range:
        point_with_largest_range = point
        largest_range = point[-1]
    #define range for x and y
    if point[0] < x_range[0]:
        x_range[0] = point[0]
    if point[0] > x_range[1]:
        x_range[1] = point[0]

    if point[1] < y_range[0]:
        y_range[0] = point[1]
    if point[1] > y_range[1]:
        y_range[1] = point[0]

#part 1        
print(point_with_largest_range)
count = 0

for nano in grid:
    if is_in_range(nano):
        count += 1

print(count)
print(x_range, y_range)



#part 2
def b_in_range_of_a(a, b):
    distance = 0
    for i in range(3):
        distance += abs(a[i] - b[i])
    if distance <= a[-1]:
        return True
    return False

"""
most_neighbors_in_range = 0
for a in grid:
    count = 0
    for b in grid:
        if b_in_range_of_a(a, b):
            count += 1
    if count > most_neighbors_in_range:
        most_neighbors_in_range = count
        print("=========", a, count)
"""

print("grid length = ", len(grid))
most_nanos_in_range = 0
for x in range(3*(10**7), 4*(10**7)):
    for y in range(43*(10**6), 50*(10**6)):
        for z in range(47*(10**6), 57*(10**6)):
            p = [x, y, z]
            #print(p)
            nanos_in_range = 0
            for nano in grid:
                if b_in_range_of_a(nano, p):
                    nanos_in_range += 1
            if nanos_in_range > most_nanos_in_range:
                most_nanos_in_range = nanos_in_range
                print(p, nanos_in_range)
    
