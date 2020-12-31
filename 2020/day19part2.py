# day19part2

def get_values(s):

    s = s.replace('91', 'b')
    s = s.replace('77', 'a')
    s = s.split()

    if '|' in s:
        if len(s) == 5:
            return [[s[0], s[1]], [s[3], s[4]]]
        elif len(s) == 3:
            return [[s[0]], [s[2]]]

    else:
        if len(s) == 1:
            return [[s[0]]]       
        elif len(s) == 2:
            return [[s[0], s[1]]] 

                    
def add_inst(x):
    global instructions

    x = x.split(':')
    instructions[x[0]] = get_values(x[1])   


def read_file():
    global instructions, messages
    inst = True
    msg  = False
    f = open('day19.txt', 'r')
    for x in f:
        if msg == True:     # messages
            x = x.strip()
            messages.add(x)

        elif x == '\n':     # seperation of instructions and messages
            inst = False
            msg  = True
            
        else:               # instructions
            x = x.replace('"', '')      # for "a" and "b"
            x = x.strip()
            add_inst(x)


# replaces the value at index i and returns a list of 1 or 2 potential lists
def replace(m, i):
    global instructions
    
    replacements = []
    rep = instructions[m[i]]

    if len(rep) == 1:
        lst_1 = m[:i] + rep[0] + m[i+1:]
        replacements.append(lst_1)
        
    elif len(rep) == 2:
        lst_1 = m[:i] + rep[0] + m[i+1:]
        replacements.append(lst_1)
        lst_2 = m[:i] + rep[1] + m[i+1:]
        replacements.append(lst_2)

    return replacements


# returns a boolean to indicate if list is comprised entirely of a's and b's
def is_all_a_b(s):
    for c in s:
        if c not in 'ab':
            return False
    return True


# given a list comprised of a's and b's, returns the corresponding string
def get_str(s):
    a = ''
    for c in s:
        a += c
    return a


# returns a list of all possible sequances when starting with 'n'
def seq_starting_w(n):
    s = set()
    queue = []
    queue.append([n])
    
    while len(queue) > 0:
        m = queue.pop(0)

        #find first non-'ab' string
        for i in range(len(m)):
            if m[i] not in 'ab':

                #replace that 1 value in m based off of instructions dictionary
                replacements = replace(m, i)    #returns a list of 1 or 2 potential replacements

                #check if all values have been replaced with 'a' or 'b'
                for r in replacements:

                    #if it is made up entirely of a's and b's, add it to set
                    if is_all_a_b(r):
                        r = get_str(r)
                        s.add(r)
                        
                    else:   # still values left to replace
                        queue.append(r)
    return s


def is_valid(m):
    global set_42, set_31
    
    reps_of_b = 0
    reps_of_a = 0

    # look at m in sections of length 8
    if len(m) % 8 != 0:
        return False

    ind = 0
    # count instances of items from set_42
    while ind < len(m):
        s = m[ind : ind + 8]
        if s in set_42:
            reps_of_b += 1
            ind += 8
        else:
            break

    # count instances of items from set_31    
    while ind < len(m):
        s = m[ind : ind + 8]
        if s in set_31:
            reps_of_a += 1
            ind += 8
        else:
            break        
            
    if ind == len(m):
        if min(reps_of_a, reps_of_b) > 0 and reps_of_b > reps_of_a:
            return True
        
    return False




# global variables
instructions = dict()       # key = number :    value = [[num1, num2], [num3, num4]]
messages = set()
valid_msg = set()

# read the file and populate global variables
read_file()

# fix outputs for '8' and '11'
instructions['8'] = [['42'], ['42','8']]
instructions['11'] = [['42', '31'], ['42','11', '31']]

# find all sequences for repeating elements
set_42 = seq_starting_w('42')
set_31 = seq_starting_w('31')

# count valid messages
count = 0
for m in messages:
    if is_valid(m):
        count += 1
print('Part 2:', count)

