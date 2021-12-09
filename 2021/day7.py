# day7
def get_total_dist(pos):
    global crabs
    total_distance = 0
    
    for c in crabs:
        total_distance += abs(pos - c)
    return total_distance
        
def get_total_dist2(pos):
    global crabs
    total_distance = 0
    
    for c in crabs:
        d = abs(pos - c)
        total_distance += int(d * (d+1) / 2)
    return total_distance


crabs = []
total = 0

f = open('day7.txt','r')
for x in f:
    x = x.strip()
    x = x.split(',')
    for v in x:
        crabs.append(int(v))
        total += int(v)
    

avg_position = total / len(crabs)
pos = int(avg_position)

def part1():
    global crabs, pos
    smallest_total_distance = (get_total_dist(pos))
    pos += 1
    n = get_total_dist(pos)

    # if total is decreasing
    if n < smallest_total_distance:
        #print('yes')
        while True:
            n = get_total_dist(pos)
            if n < smallest_total_distance:
                smallest_total_distance = n
                pos += 1
            else:
                print('Part 1:', pos - 1, smallest_total_distance)
                break

    # total went up
    else:
        
        pos -= 1
        while True:
            #print(pos)
            n = get_total_dist(pos - 1)
            if n < smallest_total_distance:
                smallest_total_distance = n
                pos -= 1
            else:
                print('Part 1:', pos, smallest_total_distance)
                break

def part2():
    global crabs, pos
    smallest_total_distance = (get_total_dist2(pos))
    pos += 1
    n = get_total_dist2(pos)

    # if total is decreasing
    if n < smallest_total_distance:
        #print('yes')
        while True:
            n = get_total_dist2(pos)
            if n < smallest_total_distance:
                smallest_total_distance = n
                pos += 1
            else:
                print('Part 2:', pos - 1, smallest_total_distance)
                break

    # total went up
    else:
        
        pos -= 1
        while True:
            #print(pos)
            n = get_total_dist2(pos - 1)
            if n < smallest_total_distance:
                smallest_total_distance = n
                pos -= 1
            else:
                print('Part 2:', pos, smallest_total_distance)
                break
            

part1()
part2()


