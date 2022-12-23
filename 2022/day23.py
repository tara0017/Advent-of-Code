#day23
import math

class elf:
    def __init__(self, position, new_position):
        self.position = position
        self.new_position = new_position
        

    def propose_new_location(self):
        global elves, x_range, y_range, rnd, proposed_new_positions, duplicate_new_positions, num_isolated

        rnd_copy = rnd
        [y,x] = self.position
        
        #check if no neighbors around
        is_isolated = True
        for e in elves:
            if e == self:
                continue
            else:
                if abs(e.position[0] - self.position[0]) <= 1 and abs(e.position[1] - self.position[1]) <= 1:
                    is_isolated = False
                    break

        if is_isolated: #no neighbors around
            proposed_new_positions.add(tuple(self.position))
            num_isolated += 1
            return self.position

        else: #not isolated
            for i in range(4):  #check four directions
                new_pos_found = True
                
                if rnd_copy == 0:    #check North
                    for e in elves:
                        if e.position[0] == y-1 and e.position[1] in range(x-1, x+2):
                            new_pos_found = False
                            break

                    if new_pos_found:
                        #print(y,x, 'NORTH')
                        if (y-1,x) in proposed_new_positions:
                            duplicate_new_positions.add((y-1, x))
                        else:
                            proposed_new_positions.add((y-1, x))
                        return [y-1, x]

                elif rnd_copy == 1:    #check South
                    for e in elves:
                        if e.position[0] == y+1 and e.position[1] in range(x-1, x+2):
                            new_pos_found = False
                            break

                    if new_pos_found:
                        #print(y,x, 'SOUTH')
                        if (y+1,x) in proposed_new_positions:
                            duplicate_new_positions.add((y+1, x))
                        else:
                            proposed_new_positions.add((y+1, x))
                        return [y+1, x]

                elif rnd_copy == 2:    #check West
                    for e in elves:
                        if e.position[0] in range(y-1, y+2) and e.position[1] == x-1:
                            new_pos_found = False
                            break

                    if new_pos_found:
                        #print(y,x, 'WEST')
                        if (y,x-1) in proposed_new_positions:
                            duplicate_new_positions.add((y, x-1))
                        else:
                            proposed_new_positions.add((y, x-1))
                        return [y, x-1]

                elif rnd_copy == 3:    #check East
                    for e in elves:
                        if e.position[0] in range(y-1, y+2) and e.position[1] == x+1:
                            new_pos_found = False
                            break

                    if new_pos_found:
                        #print(y,x, 'EAST')
                        if (y,x+1) in proposed_new_positions:
                            duplicate_new_positions.add((y, x+1))
                        else:
                            proposed_new_positions.add((y, x+1))
                        return [y, x+1]

                rnd_copy = (rnd_copy + 1) % 4

            #all sides blocked (stay)
            return [y,x]

                        
def count_spaces():
    global elves

    count = 0
    locations = set()
    
    for e in elves:
        locations.add(tuple(e.position))

    for y in range(y_range[0], y_range[1] + 1):
        for x in range(x_range[0], x_range[1] + 1):
            if (y,x) not in locations:
                count += 1
    print(count)


#global variables
grid         = []
elves        = set()
x_range      = [math.inf, 0]
y_range      = [math.inf, 0]
rnd          = 0
total_rounds = 0
num_isolated = 0
proposed_new_positions  = set()
duplicate_new_positions = set()


#read data
f = open('day23.txt','r')
for x in f:
    x = x.strip()
    grid.append(x)


#create elves and get min/max values
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '#':
            e = elf([y,x], None)
            elves.add(e)
            
            x_range[0] = min(x_range[0], x)
            x_range[1] = max(x_range[1], x)
            
            y_range[0] = min(y_range[0], y)
            y_range[1] = max(y_range[1], y)

#simulate rounds
while num_isolated < len(elves):    #total_rounds < 10:
    num_isolated = 0
    
    #each elf proposes a new location
    for e in elves:
        e.new_position = e.propose_new_location()
        
    #each elf move if possible
    for e in elves:
        if tuple(e.new_position) not in duplicate_new_positions:
            e.position = e.new_position

            #update min/max values
            x_range[0] = min(x_range[0], e.position[1])
            x_range[1] = max(x_range[1], e.position[1])
            y_range[0] = min(y_range[0], e.position[0])
            y_range[1] = max(y_range[1], e.position[0])

    #update/reset variables
    rnd = (rnd + 1) % 4
    total_rounds += 1
    proposed_new_positions.clear()
    duplicate_new_positions.clear()

    if total_rounds == 10:
        print('Part 1:')
        count_spaces()
    

print('Part 2:',total_rounds, 'rounds')    



