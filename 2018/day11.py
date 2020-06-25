#day11
def get_hund_digit(p):
    if p < 100:
        return 0
    s = str(int(p/100))
    return int(s[-1])

def get_power(x, y):
    global grid
    p = 0
    for i in range(3):
        for j in range(3):
            p += grid[(x+i, y + j)]
    return p


def get_power(x, y, size):
    global grid
    p = 0
    for i in range(size):
        for j in range(size):
            p += grid[(x+i, y + j)]
    return p


def find_largest_power(size):
    global largest_power, largest_power_coord
    print(size)
    for y in range(1, 302 - size):     
        for x in range(1, 302 - size):
            p = get_power(x, y, size)
            if p > largest_power:
                largest_power = p
                largest_power_coord = (x, y)
                largest_power_size = size
                print(size, largest_power, largest_power_coord)


grid = {}
serial_number = 5177

#create grid
for x in range(1, 301):
    for y in range(1, 301):
        rack_id = x+10
        power_level = rack_id * y + serial_number
        power_level *= rack_id
        d = get_hund_digit(power_level)
        p = d - 5
        point = (x, y)
        grid[point] = p

largest_power = 0
largest_power_coord = (0, 0)
largest_power_size = 0
    
#part 2
for size in range(1, 301):
    find_largest_power(size)
    
    



"""
#part 1
for y in range(1, 299):     #last 3x3 square [298   299   300]
    for x in range(1, 299):
        p = get_power(x, y)
        if p > largest_power:
            largest_power = p
            largest_power_coord = (x, y)

"""
print("--------------")
print(largest_power)
print(largest_power_coord)
print(largest_power_size)


