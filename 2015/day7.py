# day7

wires = dict()
instructions = []

f = open('day7.txt', 'r')
for x in f:
    x = x.replace('\n', '')
    x = x.split(' ')
    if x[1] == '->':
        try:
            value = int(x[0])
            wires[x[2]] = value
            
        except:
            instructions.append(x)
    else:
        instructions.append(x)

wires['temp'] = 1
wires['b'] = 3176   # from part 1

    
def and_gate(inst):
    global wires
    # w AND    w   ->   ans     (ans = w & w)
    return wires[inst[0]] & wires[inst[2]]


def or_gate(inst):
    global wires
    # w OR     w   ->   ans     (ans = w | w)
    return wires[inst[0]] | wires[inst[2]]


def rshift(inst):
    global wires
    # w RSHIFT  #  ->   ans     (ans = w >> #)
    return wires[inst[0]] >> int(inst[2])


def lshift(inst):
    global wires
    # w LSHIFT  #  ->   ans     (ans = w << #)
    return wires[inst[0]] << int(inst[2])


def not_gate(inst):
    global wires
    # NOT      w   ->   ans     (ans = 65535 - w)
    return 65535 - int(wires[inst[1]])

    
while len(instructions) > 0:
    i = 0
    while i < len(instructions):
        inst = instructions[i]

        # replacing those instructions that have a value of 1 instead of a gate
        try:
            if int(inst[0]) == wires['temp']:
                inst[0] = 'temp'
        except:
            pass
            
        if inst[1] == 'AND':
            # if both wires have values assigned
            if inst[0] in wires and inst[2] in wires:
                wires[inst[-1]] = and_gate(inst)

                # remove inst from instructions and back up index
                instructions.remove(inst)
                i -= 1

        elif inst[1] == 'OR':
            # if both wires have values assigned
            if inst[0] in wires and inst[2] in wires:
                wires[inst[-1]] = or_gate(inst)
                
                # remove inst from instructions and back up index
                instructions.remove(inst)
                i -= 1
                
        elif inst[1] == 'RSHIFT':
            # if wire has value assigned
            if inst[0] in wires:
                wires[inst[-1]] = rshift(inst)
                
                # remove inst from instructions and back up index
                instructions.remove(inst)
                i -= 1
                
        elif inst[1] == 'LSHIFT':
            # if wire has value assigned
            if inst[0] in wires:
                wires[inst[-1]] = lshift(inst)
                
                # remove inst from instructions and back up index
                instructions.remove(inst)
                i -= 1
                
        elif inst[0] == 'NOT':
            # if wire has value assigned
            if inst[1] in wires:
                wires[inst[-1]] = not_gate(inst)
                
                # remove inst from instructions and back up index
                instructions.remove(inst)
                i -= 1

        i += 1
     
    if 'lx' in wires:
        break
    

print(wires['lx'])
            






