#day23
def st(r, v):
    global registers
    #v is given as a letter from the register insted of a value 
    if v.upper() != v:
        v = int(registers[v])
    registers[r] = int(v)

def sub(r, v):
    global registers
    #v is given as a letter from the register insted of a value 
    if v.upper() != v:
        v = int(registers[v])    
    registers[r] -= int(v)

def mul(r, v):
    global registers, mul_count
    mul_count += 1
    #v is given as a letter from the register insted of a value 
    if v.upper() != v:
        v = int(registers[v])
    #print(registers[r], int(v))
    registers[r] *= int(v)

mul_count = 0
instructions = []
registers = {}
index = 0

f = open('day23_input.txt', 'r')
for x in f:
    x = x.split()
    instructions.append(x)

print(instructions)
print(len(instructions))

reg = 'abcdefgh'
for r in reg:
    registers[r] = 0

registers['a'] = 1
h = 1

while True:
    if index >31 or index < 0:
        break
    step = instructions[index]
    #if step[1] not in registers:
    #    registers[step[1]] = 0
    print(step)
    if step[0] == 'set':
        st(step[1], step[2])
        index += 1
    elif step[0] == 'sub':
        sub(step[1], step[2])
        index += 1
    elif step[0] == 'mul':
        #print(step)
        mul(step[1], step[2])
        index += 1
    elif step[0] == 'jnz':
        #print(step[1])
        #given as a letter from the register insted of a value 
        if step[1].upper() != step[1]:    
            if int(registers[step[1]]) != 0:
                index += int(step[2])
            else:
                index += 1
        else:
            if step[1] != 0:
                index += int(step[2])
            else:
                index += 1
    
        

    
#print(mul_count)
print(registers)
