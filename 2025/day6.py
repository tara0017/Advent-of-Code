# Day 6
def add(i):
    global lines

    total = 0
    for ln in lines:
        total += ln[i]
    return total


def multiply(i):
    global lines

    total = 1
    for ln in lines:
        total *= ln[i]
    return total

    
lines = []
operations = []
rev_lines = []

f = open('day6.txt','r')
for x in f:
    #print(len(x))
    rev_lines.append(x[-2::-1])
    x = x.split()
    

    if x[0] == '+' or x[0] == '*':
        operations = x
    else:
        line = []
        for n in x:
            line.append(int(n))
        lines.append(line)

"""
for l in lines:
    print(l)
print(operations)
"""

total = 0
for i in range(len(operations)):
    if operations[i] == '+':
        total += add(i)
    elif operations[i] == '*':
        total += multiply(i)

print(total)


# Part 2

def get_next_op_ind(op_ind):
    s = rev_lines[-1]

    for i in range(op_ind + 1, len(s)):
        if s[i] == '+' or s[i] == '*':
            return i
    return -1


def get_val_at_index(i):
    global rev_lines

    v = 0
    for rl in rev_lines[:-1]:
        if rl[i] != ' ':
            v = v*10 + int(rl[i])
    #print('v = ', v)
    return v
            

def add2(start, end):
    #print('+ s,e ', start, end)
    total = 0
    for i in range(start, end + 1):
        v = get_val_at_index(i)
        total += v
    return total


def multiply2(start, end):
    #print('* s,e ', start, end)
    total = 1
    for i in range(start, end + 1):
        v = get_val_at_index(i)
        total *= v
    return total

"""
for rl in rev_lines:
    print(rl)
"""

op_ind  = 0
num_ind = 0
nxt_ind = get_next_op_ind(op_ind)
total2 = 0

while nxt_ind != -1:
    if rev_lines[-1][nxt_ind] == '+':
        total2 += add2(num_ind, nxt_ind)
    elif rev_lines[-1][nxt_ind] == '*':
        total2 += multiply2(num_ind, nxt_ind)

    op_ind  = nxt_ind
    num_ind = nxt_ind + 2
    nxt_ind = get_next_op_ind(op_ind)
    
print(total2)



