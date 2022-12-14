#day14
import copy

def create_rocks(s):
    global rocks, max_y, min_x, max_x

    loc = s[0]
    rocks.add(loc)
    for i in range(1, len(s)):
        
        #check if vertical line
        if s[i][0] == loc[0]:
            #check if up
            if s[i][1] < loc[1]:
                while loc != s[i]:
                    y = loc[1] - 1
                    loc = (loc[0], y)
                    rocks.add(loc)

                    #update min/max values
                    if y > max_y:
                        max_y = y
                        
            #check if down
            if s[i][1] > loc[1]:
                while loc != s[i]:
                    y = loc[1] + 1
                    loc = (loc[0], y)
                    rocks.add(loc)
                    
                    #update min/max values
                    if y > max_y:
                        max_y = y
                        
            
        #horizontal line
        else:
            #check if right
            if s[i][0] > loc[0]:
                while loc != s[i]:
                    x = loc[0] + 1
                    loc = (x, loc[1])
                    rocks.add(loc)

                    #update min/max values
                    if x < min_x:
                        min_x = x
                    if x > max_x:
                        max_x = x

                    
            #check if left
            if s[i][0] < loc[0]:
                while loc != s[i]:
                    x = loc[0] - 1
                    loc = (x, loc[1])
                    rocks.add(loc)

                    #update min/max values
                    if x < min_x:
                        min_x = x
                    if x > max_x:
                        max_x = x
        

def drop_grain():
    global sand, rocks, max_y
    
    (x,y) = (500, 0)

    while True:
        #try to drop down
        while (x, y+1) not in rocks and (x, y+1) not in sand:
            y += 1
            
            #check if below last rock
            if y > max_y + 3:
                return -1

        #if down is blocked, try to drop left and restart drop down
        if (x-1, y+1) not in rocks and (x-1, y+1) not in sand:
            x -= 1
            y += 1

        #if down and left are blocked try to drop right and restart
        elif (x+1, y+1) not in rocks and (x+1, y+1) not in sand:
            x += 1
            y += 1

        #come to rest
        else:
            return (x,y)


        
#global variables
rocks = set()
sand = set()
max_y = 0
min_x = 1000
max_x = 0


#read data and create rock formation
f = open('day14.txt','r')
for x in f:
    x = x.split('->')
    for i in range(len(x)):
        x[i] = x[i].strip()
        x[i] = eval(x[i])
    create_rocks(x)

create_rocks([(min_x - 10000, max_y + 2), (max_x + 10000, max_y + 2)])


new_locations_avail = True
while new_locations_avail:
    new_locations_avail = False
    location = drop_grain()
    if location != -1:
        if location != (500, 0):
            new_locations_avail = True
        sand.add(location)

        
print('Part 2:', len(sand))
         


"""
def create_rocks(s):
    global rocks, max_y, min_x, max_x
    
    loc = s[0]
    rocks.add(loc)
    for i in range(1, len(s)):
        
        #check if vertical line
        if s[i][0] == loc[0]:
            #check if up
            if s[i][1] < loc[1]:
                while loc != s[i]:
                    y = loc[1] - 1
                    loc = (loc[0], y)
                    rocks.add(loc)
            
            #check if down
            if s[i][1] > loc[1]:
                while loc != s[i]:
                    y = loc[1] + 1
                    loc = (loc[0], y)
                    rocks.add(loc)
                    
                    #update min/max values
                    if y > max_y:
                        max_y = y
                        
            
        #horizontal line
        else:
            #check if right
            if s[i][0] > loc[0]:
                while loc != s[i]:
                    x = loc[0] + 1
                    loc = (x, loc[1])
                    rocks.add(loc)

                    #update min/max values
                    if x > max_x:
                        max_x = x

                    
            #check if left
            if s[i][0] < loc[0]:
                while loc != s[i]:
                    x = loc[0] - 1
                    loc = (x, loc[1])
                    rocks.add(loc)

                    #update min/max values
                    if x < min_x:
                        min_x = x


    
def drop_grain():
    global sand, rocks, max_y
    
    (x,y) = (500, 0)

    while True:
        #try to drop down
        while (x, y+1) not in rocks and (x, y+1) not in sand:
            y += 1
            
            #check if below last rock
            if y > max_y:
                return -1

        #if down is blocked, try to drop left and restart drop down
        if (x-1, y+1) not in rocks and (x-1, y+1) not in sand:
            x -= 1
            y += 1

        #if down and left are blocked try to drop right and restart
        elif (x+1, y+1) not in rocks and (x+1, y+1) not in sand:
            x += 1
            y += 1

        #come to rest
        else:
            return (x,y)


        
#global variables
rocks = set()
sand = set()
max_y = 0
min_x = 1000
max_x = 0


#read data and create rock formation
f = open('day14.txt','r')
for x in f:
    x = x.split('->')
    for i in range(len(x)):
        x[i] = x[i].strip()
        x[i] = eval(x[i])
    create_rocks(x)


new_locations_avail = True
while new_locations_avail:
    new_locations_avail = False
    location = drop_grain()
    if location != -1:
        new_locations_avail = True
        sand.add(location)

        
print('Part 1:', len(sand))
"""            





