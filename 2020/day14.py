# day14
import itertools

# read input file
def read_file():
    global data
    
    f = open('day14.txt', 'r')
    group = []
    for x in f:
        x = x.strip()
        x = x.split(' = ')
        if x[0] == 'mask':
            if len(group) > 0:      # ignore the first one
                data.append(group)
            group = []
            group.append(x[1])
        else:
            group.append(x)         # [ mem[loc], value ]
    # add last group
    data.append(group)

    
def get_converted_value(msk, item):
    value   = int(item[1])
    b       = bin(value)[2:]

    #match length of address to length of mask
    while len(b) < len(msk):
        b = '0' + b

    v = 0
    for i in range(len(msk)):
        j = len(msk) - i - 1
        
        if msk[j] == '1':
            v += (2**i)        
        elif msk[j] == 'X':
            # if b has a one at that index location
            if b[j] == '1':                
                # increase value by 2**i
                v += (2**i)
    return v


def get_mem_address(msk, address):
    b = bin(address)[2:]

    #match length of address to length of mask
    while len(b) < len(msk):
        b = '0' + b

    s = ''
    for i in range(len(msk)):
        if msk[i] == '1':
            s += '1'
        elif msk[i] == 'X':
            s += 'X'
        elif msk[i] == '0':
            s += b[i]

    # return list of all possible memory addresses
    return get_all_combos(s)
    
     

def get_all_combos(s):
    total_value = 0         # total w/o floating values
    float_i_values = [0]
    
    for i in range(len(s)):
        if s[i] == '1':
            total_value += (2**(len(s) - i - 1))
        elif s[i] == 'X':
            v = (2**(len(s) - i - 1))
            float_i_values.append(v)

    floating_sums = set()
    for n in range(1, len(float_i_values)):
        comb = itertools.combinations(float_i_values, n)
        for i in list(comb):
            floating_sums.add(sum(i))

    lst = []
    for fs in floating_sums:
        lst.append(fs + total_value) 

    return lst


# part 1
def part_1():
    global data
    for grp in data:
        for i in range(len(grp)):
            if i == 0:
                mask = grp[i]
            else:
                val         = get_converted_value(mask, grp[i])
                mem_address = grp[i][0][4:-1]

                memory[mem_address] = val
    print('Part 1:')
    print(get_total())


# part 2
def part_2():
    for grp in data:
        for i in range(len(grp)):
            if i == 0:
                mask = grp[i]
            else:
                val         = int(grp[i][1])
                address     = grp[i][0][4:-1]
                mem_address = get_mem_address(mask, int(address))
                
                #print (mem_address, val)
                for m in mem_address:
                    memory[m] = val

    print('Part 2:')
    print(get_total())

    
def get_total():
    global memory
    total = 0
    for m in memory:
        total += memory[m]
    return total



#global variables       
data = []
memory = dict()


read_file()
part_1()
memory.clear()
part_2()


