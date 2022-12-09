#day9

#part1
def move_up(n):
    global head_pos, visited, tail_pos

    for i in range(n):
        head_pos[1] += 1
        move_tail()
        visited.add(tuple(tail_pos))

def move_down(n):
    global head_pos, visited, tail_pos

    for i in range(n):
        head_pos[1] -= 1
        move_tail()
        visited.add(tuple(tail_pos))
    
def move_right(n):
    global head_pos, visited, tail_pos

    for i in range(n):
        head_pos[0] += 1
        move_tail()
        visited.add(tuple(tail_pos))

def move_left(n):
    global head_pos, visited, tail_pos

    for i in range(n):
        head_pos[0] -= 1
        move_tail()
        visited.add(tuple(tail_pos))
        
def is_not_adjacent():
    global head_pos, tail_pos

    if abs(head_pos[0] - tail_pos[0]) > 1:
        return True
    if abs(head_pos[1] - tail_pos[1]) > 1:
        return True
    return False

    
def move_tail():
    global head_pos, tail_pos

    if is_not_adjacent():
        #move up/down
        if head_pos[0] == tail_pos[0]:
            if head_pos[1] > tail_pos[1]: #head is higher
                tail_pos[1] += 1
            else: #head is lower
                tail_pos[1] -= 1
                
        #move right/left
        elif head_pos[1] == tail_pos[1]:
            if head_pos[0] > tail_pos[0]: #head is to right
                tail_pos[0] += 1
            else: #head is to left
                tail_pos[0] -= 1
                
        #move diagonal
        else:
            #up and right
            if head_pos[1] > tail_pos[1] and head_pos[0] > tail_pos[0]:
                tail_pos[1] += 1
                tail_pos[0] += 1
            #up and left
            elif head_pos[1] > tail_pos[1] and head_pos[0] < tail_pos[0]:
                tail_pos[1] += 1
                tail_pos[0] -= 1
            #down and right
            elif head_pos[1] < tail_pos[1] and head_pos[0] > tail_pos[0]:
                tail_pos[1] -= 1
                tail_pos[0] += 1
            #down and left
            elif head_pos[1] < tail_pos[1] and head_pos[0] < tail_pos[0]:
                tail_pos[1] -= 1
                tail_pos[0] -= 1




#part2
class knot:
    def __init__(self, name, location = [0,0], head = None, tail = None):
        self.name = name
        self.location = location
        self.head = head
        self.tail = tail
        
    def print_detail(self):
        print(self.name)
        print(self.location)
        if self.head == None:
            print("None")
        else:
            print(self.head.name)
        if self.tail == None:
            print("None")
        else:
            print(self.tail.name)
        print('-------------------')
        
   
def move_up2(n):
    global visited2,knots

    for i in range(n):
        knots[0].location[1] += 1
        move_tails()
        visited2.add(tuple(knots[-1].location))

def move_down2(n):
    global visited2,knots

    for i in range(n):
        knots[0].location[1] -= 1
        move_tails()
        visited2.add(tuple(knots[-1].location))
    
def move_right2(n):
    global visited2,knots

    for i in range(n):
        knots[0].location[0] += 1
        move_tails()
        visited2.add(tuple(knots[-1].location))

def move_left2(n):
    global visited2,knots

    for i in range(n):
        knots[0].location[0] -= 1
        move_tails()
        visited2.add(tuple(knots[-1].location))

    
def move_tails():
    global knots

    for k in knots:
        #skip the head (already moved)
        if k.head == None:
            continue

        else:
            if is_not_adjacent_to_head(k):
                h_coord = k.head.location
                
                #move up/down
                if h_coord[0] == k.location[0]: #same x coordinate
                    #head is higher
                    if h_coord[1] > k.location[1]: 
                        k.location[1] += 1
                    #head is lower
                    else: 
                        k.location[1] -= 1

                #move left/right
                elif h_coord[1] == k.location[1]: #same y coordinate
                    #head is to right
                    if h_coord[0] > k.location[0]: 
                        k.location[0] += 1
                    #head is to left
                    else: 
                        k.location[0] -= 1

                #move diagonal
                else:
                    #up and right
                    if h_coord[1] > k.location[1] and h_coord[0] > k.location[0]:
                        k.location[1] += 1
                        k.location[0] += 1
                    #up and left
                    elif h_coord[1] > k.location[1] and h_coord[0] < k.location[0]:
                        k.location[1] += 1
                        k.location[0] -= 1

                    #down and right
                    elif h_coord[1] < k.location[1] and h_coord[0] > k.location[0]:
                        k.location[1] -= 1
                        k.location[0] += 1
                    #down and left
                    elif h_coord[1] < k.location[1] and h_coord[0] < k.location[0]:
                        k.location[1] -= 1
                        k.location[0] -= 1



def is_not_adjacent_to_head(k):
    global knots
    h_coord = k.head.location

    if abs(h_coord[0] - k.location[0]) > 1:
        return True
    if abs(h_coord[1] - k.location[1]) > 1:
        return True
    return False



#global variables
visited = set()
visited2 = set()

#create head/tail PART 1
head_pos = [0,0]
tail_pos = [0,0]

#create knots PART 2
k0 = knot('k0')
knots = [k0]
for i in range(1,10):
    name = 'k' + str(i)
    k = knot(name, [0,0], knots[-1], None)
    knots[-1].tail = k
    knots.append(k)

#add starting location to visited sets
visited.add(tuple(tail_pos))
visited2.add(tuple(knots[-1].location))


#read/process data
f = open('day9.txt','r')
for x in f:
    x = x.split()
    if x[0] == 'U':
        move_up(int(x[1]))  #part 1
        move_up2(int(x[1])) #part 2
    elif x[0] == 'D':
        move_down(int(x[1]))
        move_down2(int(x[1]))
    elif x[0] == 'R':
        move_right(int(x[1]))
        move_right2(int(x[1]))
    elif x[0] == 'L':
        move_left(int(x[1]))
        move_left2(int(x[1]))
            

print('Part 1:', len(visited))
print('Part 2:', len(visited2))
