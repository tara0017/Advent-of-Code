# day 5

def find_value(s):
    if len(s) == 7:
        rng = [0,127]
    else:
        rng = [0,7]

    i = 0
    while rng[1] > rng[0]:
        if s[i] == 'B' or s[i] == 'R':
            # keep upper half
            diff = rng[1] - rng[0]
            rng[0] += (diff // 2 + 1)
            
        elif s[i] == 'F' or s[i] == 'L':
            # keep lower half
            diff = rng[1] - rng[0]
            rng[1] -= (diff // 2 + 1)
        i += 1
    return rng[0]


def get_seat_id(r,c):
    return 8 * r + c


seats = set()
highest_seat_id = 0

row_range = [100, 0]
col_range = [100, 0]

f = open('day5.txt','r')
for x in f:
    row = find_value(x[:7])
    col = find_value(x[7:])

    seat_id = get_seat_id(row, col)
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id
    seats.add((row, col))

    if row > row_range[1]:
        row_range[1] = row
    if row < row_range[0]:
        row_range[0] = row
    if col > col_range[1]:
        col_range[1] = col
    if col < col_range[0]:
        col_range[0] = col    

# part 1    
print(highest_seat_id)

# part 2
print('missing seats:')
for r in range(row_range[0], row_range[1] + 1): 
    for c in range(col_range[0], col_range[1] + 1):
        if (r,c) not in seats:
            print((r,c), get_seat_id(r,c))
