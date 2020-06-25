#day16


#addr
def addr(before, instruction):
    after = before[:]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]
    after[C] = after[A] + after[B]
    return(after)

def addi(before, instruction):
    after = before[:]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]
    after[C] = after[A] + B
    return(after)
 
def mulr(before, instruction):
    after = before[:]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]
    after[C] = after[A] * after[B]
    return(after)

def muli(before, instruction):
    after = before[:]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]
    after[C] = after[A] * B
    return(after)

def banr(before, instruction):
    after = before[:]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]
    after[C] = after[A] & after[B]
    return(after)

def bani(before, instruction):
    after = before[:]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]
    after[C] = after[A] & B
    return(after)
    
def borr(before, instruction):
    after = before[:]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]
    after[C] = after[A] | after[B]
    return(after)

def bori(before, instruction):
    after = before[:]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]
    after[C] = after[A] | B
    return(after)    

def setr(before, instruction):
    after = before[:]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]
    after[C] = after[A]
    return(after)
    
def seti(before, instruction):
    after = before[:]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]
    after[C] = A
    return(after)

def gtir(before, instruction):
    after = before[:]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]
    if A > after[B]:
        after[C] = 1
    else:
        after[C] = 0
    return(after)

def gtri(before, instruction):
    after = before[:]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]
    if after[A] > B:
        after[C] = 1
    else:
        after[C] = 0
    return(after)

def gtrr(before, instruction):
    after = before[:]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]
    if after[A] > after[B]:
        after[C] = 1
    else:
        after[C] = 0
    return(after)

def eqir(before, instruction):
    after = before[:]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]
    if A == after[B]:
        after[C] = 1
    else:
        after[C] = 0
    return(after)

def eqri(before, instruction):
    after = before[:]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]
    if after[A] == B:
        after[C] = 1
    else:
        after[C] = 0
    return(after)

def eqrr(before, instruction):
    after = before[:]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]
    if after[A] == after[B]:
        after[C] = 1
    else:
        after[C] = 0
    return(after)



#return a list with the functions that worked
def test_each_opcode(before, instructions):
    global after
    result = []
    if addr(before, instructions) == after:
        result.append("addr")
    if addi(before, instructions) == after:
        result.append("addi")
    if mulr(before, instructions) == after:
        result.append("mulr")
    if muli(before, instructions) == after:
        result.append("muli")
    if banr(before, instructions) == after:
        result.append("banr")
    if bani(before, instructions) == after:
        result.append("bani")
    if borr(before, instructions) == after:
        result.append("borr")
    if bori(before, instructions) == after:
        result.append("bori")
    if setr(before, instructions) == after:
        result.append("setr")
    if seti(before, instructions) == after:
        result.append("seti")
    if gtir(before, instructions) == after:
        result.append("gtir")
    if gtri(before, instructions) == after:
        result.append("gtri")
    if gtrr(before, instructions) == after:
        result.append("gtrr")
    if eqir(before, instructions) == after:
        result.append("eqir")
    if eqri(before, instructions) == after:
        result.append("eqri")
    if eqrr(before, instructions) == after:
        result.append("eqrr")

    return result
    
"""
#part 1

count = 0
f = open("day16_input.txt", "r")
for x in f:
    x = x.replace("[", "")
    x = x.replace("]", "")
    x = x.replace(",", "")
    x = x.replace(":", "")
    x = x.split()
    if len(x) > 0:
        if x[0] == "Before":
            before = [ int(x[1]), int(x[2]), int(x[3]), int(x[4]) ]
        elif len(x) == 4:
            instructions = [ int(x[0]), int(x[1]), int(x[2]), int(x[3]) ]
        elif x[0] == "After":
            after = [ int(x[1]), int(x[2]), int(x[3]), int(x[4]) ]
            result = test_each_opcode(before, instructions)
            if len(result) >= 3:
                count += 1
            #if instructions[0] == 4:
            #if 'setr' in result and len(result) < 5:
            #    print(result, instructions)
            
            #break
    
print(count)
print(before, instructions, after)
"""

before = [0, 0, 0, 0]
f = open("day16_input2.txt", "r")
for x in f:
    x = x.split()
    instructions = [int(x[0]), int(x[1]), int(x[2]), int(x[3])]
    if instructions[0] == 0:
        before = banr(before, instructions)
    elif instructions[0] == 1:
        before = eqrr(before, instructions)
    elif instructions[0] == 2:
        before = setr(before, instructions)
    elif instructions[0] == 3:
        before = eqir(before, instructions)
    elif instructions[0] == 4:
        before = bori(before, instructions)
    elif instructions[0] == 5:
        before = muli(before, instructions)
    elif instructions[0] == 6:
        before = bani(before, instructions)
    elif instructions[0] == 7:
        before = borr(before, instructions)
    elif instructions[0] == 8:
        before = gtir(before, instructions)
    elif instructions[0] == 9:
        before = gtrr(before, instructions)
    elif instructions[0] == 10:
        before = addi(before, instructions)
    elif instructions[0] == 11:
        before = gtri(before, instructions)
    elif instructions[0] == 12:
        before = eqri(before, instructions)
    elif instructions[0] == 13:
        before = addr(before, instructions)
    elif instructions[0] == 14:
        before = mulr(before, instructions)
    elif instructions[0] == 15:
        before = seti(before, instructions)
    print(before)
    
    

#opcode 0 = banr 
#opcode 1 = eqrr
#opcode 2 = setr
#opcode 3 = eqir
#opcode 4 = bori 
#opcode 5 = muli
#opcode 6 = bani
#opcode 7 = borr
#opcode 8 = gtir
#opcode 9 = gtrr
#opcode 10 = addi
#opcode 11 = gtri
#opcode 12 = eqri
#opcode 13 = addr
#opcode 14 = mulr 
#opcode 15 = seti




