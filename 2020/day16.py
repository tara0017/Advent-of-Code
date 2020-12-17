# day16
import copy

def check_if_tix_valid(tix):
    global possible_values, scan_error, valid_tix

    valid = True
    
    tix = tix.split(',')
    for t in tix:
        t = int(t)
        if t not in possible_values:
            scan_error += t
            valid = False
            
    if valid == True:
        valid_tix.append(tix)


def add_field(f):
    global fields, field_lst, possible_values

    field = f[0]
    field_lst.append(field)
    
    value = f[1].replace(' or ', '-')
    value = value.split('-')
    fields[field] = value

    for i in range(int(value[0]), int(value[1]) + 1):
        possible_values.add(i)
    
    for i in range(int(value[2]), int(value[3]) + 1):
        possible_values.add(i)


# read file
def read_file():
    global my_tix
    
    flds     = True
    nrby_tix = False
    my_t = False
    
    f = open('day16.txt', 'r')
    for x in f:
        x = x.strip()
        if 'your ticket' in x:
            flds = False
            my_t = True
        elif my_t == True:
            x = x.split(',')
            for v in x:
                my_tix.append(v)
            my_t = False
            
        elif flds == True:
            x = x.split(':')
            if len(x) > 1: # ensure it is not an empty line
                add_field(x)
        elif nrby_tix == True:
            check_if_tix_valid(x)
        elif 'nearby tickets' in x:
            nrby_tix = True


def trim_fields(t):
    global field_order
    
    for i in range(len(t)):
        v = int(t[i])
        
        flds_to_remove = []

        
        for field in field_order[i]:
            rng = fields[field] #array [start, stop, start2,, stop2]
            
            # if v is not in the range of fields[field]:
            if not ((int(rng[0]) <= v and int(rng[1]) >= v) or (int(rng[2]) <= v and int(rng[3]) >= v)):
                # add it to list of fields to remove
                flds_to_remove.append(field)

        #remove flds_to_remove from field_order[i]
        if (len(flds_to_remove) > 0):
            for f in flds_to_remove:
                
                field_order[i].remove(f)


def values_match(values, rng):
    global fields
    m0 = int(rng[0])
    m1 = int(rng[1])
    m2 = int(rng[2])
    m3 = int(rng[3])

    for v in values:
        if not ((v >= m0 and v <= m1) or (v >= m2 and v <= m3)):
            return False
    return True




# global variables
field_lst  = []
fields     = dict()
tickets    = []
valid_tix  = []
my_tix     = []
scan_error = 0
possible_values = set()




# part 1
read_file()
print('Part 1:', scan_error)


# part 2
# assign ALL fields to each index location
field_order = []
for i in range(len(field_lst)):
    field_order.append(copy.deepcopy(field_lst))


# remove fields that do not match values
for t in valid_tix:
    trim_fields(t)


# get indices that include 'departure'
departure_indices = set()
for i in range(len(my_tix) - 2):
    for i in range(len(field_order)):
        f = field_order[i]

        if len(f) == 1:
            fld = f[0]

            if 'departure' in fld:
                departure_indices.add(i)
                
            for j in range(len(field_order)):
                if j == i:
                    continue
                else:
                    try:
                        field_order[j].remove(fld)
                    except:
                        continue


product = 1
for i in range(len(my_tix)):
    if i in departure_indices:
        product *= int(my_tix[i])

print('Part 2:', product)
                
                
        




