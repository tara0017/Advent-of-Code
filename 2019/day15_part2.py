def oxi(x, y):
    global newly_oxiginated, points
    for point in points:
        if point[0] == x and point[1] == y:
            newly_oxiginated.add(point)
            points.remove(point)
            break
        

f = open("day15_part2_input.txt", "r")
for i in f:
    s = i.replace('[', '').replace(']', '').replace(',', '').split()
points = set()
for i in range(0, len(s), 3):
    x = (int(s[i]), int(s[i+1]), int(s[i+2]))
    if x[2] == 1:
        points.add(x)


oxiginated = set()
oxiginated.add((16, -16, 2))
#points.remove((16, -16, 2))
#print (oxiginated)
newly_oxiginated = set()
minutes = 0

while len(points) > 0:
    for p in oxiginated:
        x = p[0]
        y = p[1]
        oxi(x+1, y) #point to right
        oxi(x-1, y) #point to left
        oxi(x, y+1) #point above
        oxi(x, y-1) #point below
    minutes += 1
    #print("________________")
    #print("N_O", newly_oxiginated)
    oxiginated = newly_oxiginated.copy()
    #print("OXI", oxiginated)
    newly_oxiginated.clear()

print (minutes)



