# day11

def read_line(x):
    row = []
    x = x.replace('\n', '')
    for c in x:
        row.append(c)
    return row


def seats_to_switch():
    global grid
    flip = []
    
    for j in range(len(grid)):
        row = grid[j]
        
        for i in range(len(row)):
            seat = row[i]
            
            if seat == '.':
                continue
            else:
                # part 2
                n = get_surrounding_part2(j, i)
                if seat == 'L':
                    if n == 0:      # no occupied seats around
                        flip.append((j,i))
                elif seat == '#':
                    if n >= 5:
                        flip.append((j,i))
               
                """
                # part 1
                n = get_surrounding(j, i)
                if seat == 'L':
                    if n == 0:      # no occupied seats around
                        flip.append((j,i))
                elif seat == '#':
                    if n >= 4:
                        flip.append((j,i))
                """
    return flip


def get_surrounding(r, c):
    global grid

    num_occupied_seats = 0
    for j in range(-1,2):
        for i in range(-1,2):
            if i == 0 and j == 0:   # current seat
                continue
            elif (r + j) < 0 or (c + i) < 0:
                continue
            try:
                if grid[r + j][c + i] == '#':
                    num_occupied_seats += 1
            except:
                continue

    return num_occupied_seats


def get_surrounding_part2(r, c):
    global grid
    num_occupied_seats = 0

    # check north
    y = r-1
    while y >= 0:
        if grid[y][c] == 'L':
            break
        elif grid[y][c] == '#':
            num_occupied_seats += 1
            break
        y -= 1

    # check south
    y = r+1
    while y < len(grid):
        if grid[y][c] == 'L':
            break
        elif grid[y][c] == '#':
            num_occupied_seats += 1
            break
        y += 1

    # check east
    x = c + 1
    while x < len(grid[0]):
        if grid[r][x] == 'L':
            break
        elif grid[r][x] == '#':
            num_occupied_seats += 1
            break
        x += 1

    # check west
    x = c - 1
    while x >= 0:
        if grid[r][x] == 'L':
            break
        elif grid[r][x] == '#':
            num_occupied_seats += 1
            break
        x -= 1

    # check northeast
    x = c + 1
    y = r - 1
    while y >= 0 and x < len(grid[0]):
        if grid[y][x] == 'L':
            break
        elif grid[y][x] == '#':
            num_occupied_seats += 1
            break
        y -= 1
        x += 1

    # check northwest
    x = c - 1
    y = r - 1
    while y >= 0 and x >= 0:
        if grid[y][x] == 'L':
            break
        elif grid[y][x] == '#':
            num_occupied_seats += 1
            break
        y -= 1
        x -= 1

    # check southeast
    x = c + 1
    y = r + 1
    while y < len(grid) and x < len(grid[0]):
        if grid[y][x] == 'L':
            break
        elif grid[y][x] == '#':
            num_occupied_seats += 1
            break
        y += 1
        x += 1

    # check southwest
    x = c - 1
    y = r + 1
    while y < len(grid) and x >= 0:
        if grid[y][x] == 'L':
            break
        elif grid[y][x] == '#':
            num_occupied_seats += 1
            break
        y += 1
        x -= 1
        
    return num_occupied_seats



def flip_seat(s):
    global grid
    j = s[0]
    i = s[1]
    if grid[j][i] == 'L':
        grid[j][i] = '#'  
    elif grid[j][i] == '#':
        grid[j][i] = 'L'

    
def count_occupied():
    global grid
    count = 0
    
    for row in grid:
        for s in row:
            if s == '#':
                count += 1
    return count
    
grid = []

f = open('day11.txt', 'r')
for x in f:
    row = read_line(x)
    grid.append(row)


round = 0
while True:
    round += 1
    change = seats_to_switch()

    # are there any seats to flip?
    if len(change) == 0:
        break

    # flip seats
    for c in change:
        flip_seat(c)

print(count_occupied())
