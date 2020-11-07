# day6
def process_instructions(x):
    # part2
    if x[0] == 'toggle':
        change_brightness(int(x[1]), int(x[2]), int(x[4]), int(x[5]), 2)
    else:               # handle turn on and turn off
        value = -1      # decrease by 1 if 'off'
        if x[1] == 'on':
            value = 1   # increase brightness by 1
        change_brightness(int(x[2]), int(x[3]), int(x[5]), int(x[6]), value)
        
    """
    # part 1
    if x[0] == 'toggle':
        toggle(int(x[1]), int(x[2]), int(x[4]), int(x[5]))
        
    else:               # handle turn on and turn off
        value = 0       # value is 0 if light is off, 1 if light is on
        if x[1] == 'on':
            value = 1   # turn light on
        
        turn(int(x[2]), int(x[3]), int(x[5]), int(x[6]), value)
    """


def change_brightness(x1, y1, x2, y2, value):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            p = (x, y)

            # add point if not already in grid
            if p not in grid:
                grid[p] = 0

            # adjust brightness value
            grid[p] += value

            # 0 is the minimum brightness
            if grid[p] < 0:
                grid[p] = 0
            

                

def turn(x1, y1, x2, y2, value):
    global grid
    
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            p = (x, y)
            grid[p] = value     # value 1 = light is on, value 0 = light is off


def toggle(x1, y1, x2, y2):
    global grid
    
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            p = (x, y)
            if p not in grid:
                current_value = 0
            else:
                current_value = grid[p]
            grid[p] = (current_value + 1) % 2


    
grid = dict()

f = open('day6.txt', 'r')
for x in f:
    x = x.replace('\n', '')
    x = x.replace(',', ' ')
    x = x.split(' ')
    #print(x)
    process_instructions(x)
    # break

# part 2
total = 0
for p in grid:
    total += grid[p]

print(total)

"""
# part1
count = 0
for p in grid:
    if grid[p] == 1:
        count += 1

print(count)
"""


