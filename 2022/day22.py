#day22
def get_next_step():
    global steps, step_ind

    end_ind = step_ind + 1
    while steps[end_ind] != 'R' and steps[end_ind] != 'L' and steps[end_ind] != 'N':
        end_ind += 1
        if end_ind == len(steps):
            break

    turn     = steps[end_ind]
    num      = int(steps[step_ind:end_ind])
    step_ind = end_ind + 1
    
    return (num, turn)


def turn(drctn):
    global facing

    # R = 0, D = 1, L = 2, U = 3
    if drctn == 'R':
        facing = (facing + 1) % 4
    elif drctn == 'L':
        facing = (facing - 1) % 4
    else:   #no turn on the end
        return


# 50 x 50 sections A-F
#     A B
#     C
#   D E
#   F
def move2(n):
    global position, facing

    [x,y] = position

    for i in range(n):
        #####facing right
        if facing == 0:
            ################### PART 2
            #wall between sections B to E
            if x+1 == len(grid[0]) and y < 50:  #only happens in section B
                new_x = 99
                new_y = 149 - y

                if grid[new_y][new_x] == '#':   #would hit a wall
                    position = [x,y]
                    return
                else:                           #open tile
                    facing = 2  #left
                    x = new_x
                    y = new_y

            #wall between sections C to B
            elif x+1 == 100 and y in range(50, 100):  #only happens in section C
                new_x = y + 50
                new_y = 49

                if grid[new_y][new_x] == '#':   #would hit a wall
                    position = [x,y]
                    return
                else:                           #open tile
                    facing = 3  #up
                    x = new_x
                    y = new_y

            #wall between sections E to B
            elif x+1 == 100 and y in range(100, 150):  #only happens in section E
                new_x = 149
                new_y = 149 - y

                if grid[new_y][new_x] == '#':   #would hit a wall
                    position = [x,y]
                    return
                else:                           #open tile
                    facing = 2  #left
                    x = new_x
                    y = new_y

            #wall between sections F to E
            elif x+1 == 50 and y in range(150, 200):  #only happens in section F
                new_x = y - 100
                new_y = 149

                if grid[new_y][new_x] == '#':   #would hit a wall
                    position = [x,y]
                    return
                else:                           #open tile
                    facing = 3  #up
                    x = new_x
                    y = new_y
            ###################

            #next location is ' '
            elif grid[y][(x+1) % len(grid[y])] == ' ':
                new_x = x
                #update new_x until wall or open tile is found
                while grid[y][(new_x+1) % len(grid[y])] == ' ':
                    new_x += 1

                #next location is open tile
                if grid[y][(new_x+1) % len(grid[y])] == '.':
                    x = (new_x + 1) % len(grid[0])
                #next location is wall
                elif grid[y][(new_x+1) % len(grid[y])] == '#':
                    position = [x,y]
                    return

            #next location is open tile
            elif grid[y][(x+1) % len(grid[y])] == '.':
                x += 1                
            
            #next location is wall
            elif grid[y][(x+1) % len(grid[y])] == '#':
                x %= len(grid[0])
                position = [x,y]
                return

        #####facing left
        elif facing == 2:
            ################### PART 2
            #wall between sections A to D
            if x-1 == 49 and y in range(0, 50):  #only happens in section A
                new_x = 0
                new_y = 149 - y

                if grid[new_y][new_x] == '#':   #would hit a wall
                    position = [x,y]
                    return
                else:                           #open tile
                    facing = 0  #right
                    x = new_x
                    y = new_y

            #wall between sections C to D
            elif x-1 == 49 and y in range(50, 100):  #only happens in section C
                new_x = y - 50
                new_y = 100

                if grid[new_y][new_x] == '#':   #would hit a wall
                    position = [x,y]
                    return
                else:                           #open tile
                    facing = 1  #down
                    x = new_x
                    y = new_y

            #wall between sections D to A
            elif x-1 == -1 and y in range(100, 150):  #only happens in section D
                new_x = 50
                new_y = 149 - y

                if grid[new_y][new_x] == '#':   #would hit a wall
                    position = [x,y]
                    return
                else:                           #open tile
                    facing = 0  #right
                    x = new_x
                    y = new_y

            #wall between sections F to A
            elif x-1 == -1 and y in range(150, 200):  #only happens in section F
                new_x = y - 100
                new_y = 0

                if grid[new_y][new_x] == '#':   #would hit a wall
                    position = [x,y]
                    return
                else:                           #open tile
                    facing = 1  #down
                    x = new_x
                    y = new_y
            ###################

            #next location is ' '
            elif grid[y][(x-1) % len(grid[y])] == ' ':
                new_x = x
                #update new_x until wall or open tile is found
                while grid[y][(new_x-1) % len(grid[y])] == ' ':
                    new_x -= 1

                #next location is open tile
                if grid[y][(new_x-1) % len(grid[y])] == '.':
                    x = (new_x - 1) % len(grid[0])
                #next location is wall
                elif grid[y][(new_x-1) % len(grid[y])] == '#':
                    position = [x,y]
                    return

            #next location is open tile
            elif grid[y][(x-1) % len(grid[y])] == '.':
                x -= 1                
            
            #next location is wall
            elif grid[y][(x-1) % len(grid[y])] == '#':
                x %= len(grid[0])
                position = [x,y]
                return


        #####facing down
        elif facing == 1:
            ################### PART 2
            #wall between sections B to C
            if x in range(100, 150) and y+1 == 50:  #only happens in section B
                new_x = 99
                new_y = x - 50

                if grid[new_y][new_x] == '#':   #would hit a wall
                    position = [x,y]
                    return
                else:                           #open tile
                    facing = 2  #left
                    x = new_x
                    y = new_y

            #wall between sections E to F
            elif x in range(50, 100) and y+1 == 150:  #only happens in section E
                new_x = 49
                new_y = x + 100

                if grid[new_y][new_x] == '#':   #would hit a wall
                    position = [x,y]
                    return
                else:                           #open tile
                    facing = 2  #left
                    x = new_x
                    y = new_y

            #wall between sections F to B
            elif x in range(0, 50) and y+1 == 200:  #only happens in section F
                new_x = x + 100
                new_y = 0

                if grid[new_y][new_x] == '#':   #would hit a wall
                    position = [x,y]
                    return
                else:                           #open tile
                    facing = 1  #down
                    x = new_x
                    y = new_y
            ###################         
            
            #next location is ' '
            elif grid[(y+1) % len(grid)][x] == ' ':
                new_y = y
                #update new_y until wall or open tile is found
                while grid[(new_y+1) % len(grid)][x] == ' ':
                    new_y += 1

                #next location is open tile
                if grid[(new_y+1) % len(grid)][x] == '.':
                    y = (new_y + 1) % len(grid)
                #next location is wall
                elif grid[(new_y+1) % len(grid)][x] == '#':
                    position = [x,y]
                    return

            #next location is open tile
            elif grid[(y+1) % len(grid)][x] == '.':
                y += 1                
            
            #next location is wall
            elif grid[(y+1) % len(grid)][x] == '#':
                y %= len(grid)
                position = [x,y]
                return    
            
        #####facing up
        elif facing == 3:
            ################### PART 2
            #wall between sections A to F
            if x in range(50, 100) and y-1 == -1:  #only happens in section A
                new_x = 0
                new_y = x + 100

                if grid[new_y][new_x] == '#':   #would hit a wall
                    position = [x,y]
                    return
                else:                           #open tile
                    facing = 0  #right
                    x = new_x
                    y = new_y

            #wall between sections B to F
            elif x in range(100, 150) and y-1 == -1:  #only happens in section B
                new_x = x - 100 #0
                new_y = 199     #x - 100

                if grid[new_y][new_x] == '#':   #would hit a wall
                    position = [x,y]
                    return
                else:                           #open tile
                    facing = 3  #up
                    x = new_x
                    y = new_y
            #wall between sections D to C
            elif x in range(0, 50) and y-1 == 99:  #only happens in section D
                new_x = 50
                new_y = 50 + x

                if grid[new_y][new_x] == '#':   #would hit a wall
                    position = [x,y]
                    return
                else:                           #open tile
                    facing = 0  #right
                    x = new_x
                    y = new_y
            ###################
                    
            #next location is ' '            
            elif grid[(y-1) % len(grid)][x] == ' ':
                new_y = y
                #update new_y until wall or open tile is found
                while grid[(new_y-1) % len(grid)][x] == ' ':
                    new_y -= 1

                #next location is open tile
                if grid[(new_y-1) % len(grid)][x] == '.':
                    y = (new_y - 1) % len(grid)
                #next location is wall
                elif grid[(new_y-1) % len(grid)][x] == '#':
                    position = [x,y]
                    return

            #next location is open tile
            elif grid[(y-1) % len(grid)][x] == '.':
                y -= 1                
            
            #next location is wall
            elif grid[(y-1) % len(grid)][x] == '#':
                y %= len(grid)
                position = [x,y]
                return

    x %= len(grid[0])
    y %= len(grid)
    position = [x,y]
                      
            
    
def move(n):
    global position, facing

    [x,y] = position

    for i in range(n):
        #####facing right
        if facing == 0:
            #next location is ' '
            if grid[y][(x+1) % len(grid[y])] == ' ':
                new_x = x
                #update new_x until wall or open tile is found
                while grid[y][(new_x+1) % len(grid[y])] == ' ':
                    new_x += 1

                #next location is open tile
                if grid[y][(new_x+1) % len(grid[y])] == '.':
                    x = (new_x + 1) % len(grid[0])
                #next location is wall
                elif grid[y][(new_x+1) % len(grid[y])] == '#':
                    position = [x,y]
                    return

            #next location is open tile
            elif grid[y][(x+1) % len(grid[y])] == '.':
                x += 1                
            
            #next location is wall
            elif grid[y][(x+1) % len(grid[y])] == '#':
                x %= len(grid[0])
                position = [x,y]
                return

        #####facing left
        elif facing == 2:
            #next location is ' '
            if grid[y][(x-1) % len(grid[y])] == ' ':
                new_x = x
                #update new_x until wall or open tile is found
                while grid[y][(new_x-1) % len(grid[y])] == ' ':
                    new_x -= 1

                #next location is open tile
                if grid[y][(new_x-1) % len(grid[y])] == '.':
                    x = (new_x - 1) % len(grid[0])
                #next location is wall
                elif grid[y][(new_x-1) % len(grid[y])] == '#':
                    position = [x,y]
                    return

            #next location is open tile
            elif grid[y][(x-1) % len(grid[y])] == '.':
                x -= 1                
            
            #next location is wall
            elif grid[y][(x-1) % len(grid[y])] == '#':
                x %= len(grid[0])
                position = [x,y]
                return

        #####facing down
        elif facing == 1:
            #next location is ' '
            if grid[(y+1) % len(grid)][x] == ' ':
                new_y = y
                #update new_y until wall or open tile is found
                while grid[(new_y+1) % len(grid)][x] == ' ':
                    new_y += 1

                #next location is open tile
                if grid[(new_y+1) % len(grid)][x] == '.':
                    y = (new_y + 1) % len(grid)
                #next location is wall
                elif grid[(new_y+1) % len(grid)][x] == '#':
                    position = [x,y]
                    return

            #next location is open tile
            elif grid[(y+1) % len(grid)][x] == '.':
                y += 1                
            
            #next location is wall
            elif grid[(y+1) % len(grid)][x] == '#':
                y %= len(grid)
                position = [x,y]
                return    
            
        #####facing up
        elif facing == 3:
            #next location is ' '            
            if grid[(y-1) % len(grid)][x] == ' ':
                new_y = y
                #update new_y until wall or open tile is found
                while grid[(new_y-1) % len(grid)][x] == ' ':
                    new_y -= 1

                #next location is open tile
                if grid[(new_y-1) % len(grid)][x] == '.':
                    y = (new_y - 1) % len(grid)
                #next location is wall
                elif grid[(new_y-1) % len(grid)][x] == '#':
                    position = [x,y]
                    return

            #next location is open tile
            elif grid[(y-1) % len(grid)][x] == '.':
                y -= 1                
            
            #next location is wall
            elif grid[(y-1) % len(grid)][x] == '#':
                y %= len(grid)
                position = [x,y]
                return

    x %= len(grid[0])
    y %= len(grid)
    position = [x,y]
                      
  
    
#global variables
grid = []
steps = ''
step_ind = 0
facing = 0      # R = 0, D = 1, L = 2, U = 3
position = None

#read data
instructions = False
f = open('day22.txt','r')
for x in f:
    if instructions:
        steps = x.replace('\n', '')
    else:
        if x == '\n':
            instructions = True
        else:
            row = x.replace('\n', '')
            grid.append(row)
steps += 'N'    #add a no turn on the end


#get starting point
for i in range(len(grid[0])):
    if grid[0][i] == '.':
        position = [i, 0]
        break

#add blank spaces on the end of each row to match length
for i in range(len(grid)):
    while len(grid[i]) < len(grid[0]):
        grid[i] += ' '


while step_ind < len(steps):
    #get next step
    step = get_next_step()

    #move steps
    #move(step[0]) ##### PART 1 #####
    move2(step[0]) ##### PART 2 #####
    
    #turn
    turn(step[1])
    

#update final position since rows/columns start at 1
column = position[0] + 1
row    = position[1] + 1

print('Password:', 1000 * row + 4 * column + facing)


