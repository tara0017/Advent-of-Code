# day13

timestamp  = 1004098
bus_ids    = []
all_busses = []

# read data
f = open('day13.txt', 'r')
for x in f:
    x = x.replace('\n', '')
    x = x.split(',')
    
    for i in range(len(x)):
        try:
            n = x[i]
            n = int(n)
            bus_ids.append(n)
            all_busses.append(n)
        except:
            all_busses.append(x[i])


# part 1
next_bus = None
wait_time = timestamp

for b in bus_ids:
    wait = (timestamp // b + 1) * b - timestamp
    if wait < wait_time:
        wait_time = wait
        next_bus  = b

print('Part 1', next_bus, wait_time, next_bus * wait_time)



# part 2
def get_xi(item):
    global N
    Ni = N / item[1]
    x = 1
    
    while (Ni * x) % item[1] != 1:
        x += 1
    return x



offset_ids = []
for i in range(len(all_busses)):
    if x[i] != 'x':
        offset_ids.append((i, all_busses[i]))


N = 1
mods = []   # (bi, ni)

for item in offset_ids:
    N *= item[1]
    
    # id - offset
    b = (item[1] - item[0]) % item[1]

    mods.append((b, item[1]))

total = 0
for item in mods:
    x = get_xi(item)
            #   bi    * Ni             * xi
    total += (item[0] * (N // item[1]) * x)

print('Part 2', total % N)



