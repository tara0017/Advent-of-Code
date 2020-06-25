#day18
def snd(n):
    global last_sound_played, registers
    last_sound_played = (n, registers[n])

def st(r, v):
    global registers
    #v is given as a letter from the register insted of a value 
    if v.upper() != v:
        v = int(registers[v])
    registers[r] = int(v)

def add(r, v):
    global registers
    registers[r] += int(v)

def mul(r, v):
    global registers
    #v is given as a letter from the register insted of a value 
    if v.upper() != v:
        v = int(registers[v])
    #print(registers[r], int(v))
    registers[r] *= int(v)

def mod(r, v):
    global registers
    #v is given as a letter from the register insted of a value 
    if v.upper() != v:
        v = int(registers[v])
    registers[r] = registers[r] % int(v)

    
instructions = []

f = open('day18_input.txt', 'r')
for x in f:
    #print(x)
    x = x.split()
    instructions.append(x)
    
#print(instructions)

registers = {}
index = 0
last_sound_played = ""

while True:
    step = instructions[index]
    if step[1] not in registers:
        registers[step[1]] = 0

    if step[0] == 'snd':
        snd(step[1])
        index += 1
    elif step[0] == 'set':
        st(step[1], step[2])
        index += 1
    elif step[0] == 'add':
        add(step[1], step[2])
        index += 1
    elif step[0] == 'mul':
        print(step)
        mul(step[1], step[2])
        index += 1
    elif step[0] == 'mod':
        mod(step[1], step[2])
        index += 1
    elif step[0] == 'rcv':
        if int(registers[step[1]]) != 0:
            print("last sound: ", last_sound_played)
            break
        else:
            index += 1
    elif step[0] == 'jgz':
        if int(registers[step[1]]) > 0:
            index += int(step[2])
        else:
            index += 1
        

    
