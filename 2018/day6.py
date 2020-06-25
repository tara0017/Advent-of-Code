#day6
def find_next_set_of_points(points):    #points (x, y, letter_id)
    global unassigned_points
    print('-----------------------------------------', len(unassigned_points))
    #print(points)
    new_set_of_points = []
    #for each point in points
    for p in points:
        #find point above, below, left, and right
        x = p[0]
        y = p[1]
        p_id = p[2]
        adj_points = [(x, y-1, p_id),(x, y+1, p_id),(x+1, y, p_id),(x-1, y, p_id)]
        for q in adj_points:
            #if the point is in unassigned points
            if (q[0], q[1]) in unassigned_points:
                #remove it from unassigned points
                unassigned_points.remove((q[0], q[1]))
                #add it to new points to assign
                new_set_of_points.append(q)
            #if it is not in unassigned points
            else:
                #check that it is not in new set of points
                for r in new_set_of_points:
                    if (r[0], r[1]) == (q[0], q[1]) and r[2] != q[2]:
                        new_set_of_points.remove(r)
                        break
    #return new points to assign
    return new_set_of_points
    

def assign_point(p):
    global assigned_points
    point = (p[0], p[1])
    assigned_points[p[2]].append(point)

    
x_range = [1000, 0]
y_range = [1000, 0]

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
    if p[0] < x_range[0]:
        x_range[0] = p[0]
    if p[0] > x_range[1]:
        x_range[1] = p[0]

    if p[1] < y_range[0]:
        y_range[0] = p[1]
    if p[1] > y_range[1]:
        y_range[1] = p[1]
    

#print (x_range)        # [42, 353]
#print (y_range)        # [60, 342]

assigned_points      = {}   #{A: [ (x, y), (m, n)...], B: [...]}
unassigned_points    = []   #[(a, b), (c, d)... ]
new_points_to_assign = points[:]   


#create grid with all points unassigned
for x in range(42, 354):
    for y in range(60, 343):
        point = (x, y)
        unassigned_points.append(point)

for p in new_points_to_assign:
    point = (p[0], p[1])
    assigned_points[p[2]] = [ point ]
    unassigned_points.remove(point)
    
    

while len(unassigned_points) > 0:
    #save last set of points added    
    last_points_added = new_points_to_assign[:]
    ####clear new points to assign
    ####new_points_to_assign.clear()
    #find next set of points to assign
    new_points_to_assign = find_next_set_of_points(last_points_added)
    #assign new points
    for p in new_points_to_assign:
        assign_point(p)


for k in assigned_points:
    print(k, len(assigned_points[k]), assigned_points[k])
    



