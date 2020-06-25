#day12
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




def inc(r):
    global registers
    registers[r] += 1

def dec(r):
    global registers
    registers[r] -= 1    

def jnz(r, v):
    global registers, index
    #r is given as a letter from insted of a value 
    if r.upper() != r:
        r = int(registers[r])

    #print('======================')
    #print(registers)
    #print(r, v, index, '======================')
    if r == 0:
        index += 1
    else:
        index += int(v)
    #print(index)
    
def cpy(v, r):
    global registers
    #v is given as a letter from the register insted of a value 
    if v.upper() != v:
        v = int(registers[v])
    registers[r] = int(v)

    
    
instructions = []

f = open('day12_input.txt', 'r')
for x in f:
    #print(x)
    x = x.split()
    instructions.append(x)
    
print(instructions)


registers = {}
index = 0
last_sound_played = ""

registers['a'] = 0
registers['b'] = 0
registers['c'] = 1
registers['d'] = 0


while True:
    step = instructions[index]
    #print(index, step)
    if step[0] == 'cpy':
        reg = step[2]
    else:
        reg = step[1]

    if step[0] == 'cpy':
        cpy(step[1], step[2])
        index += 1
    elif step[0] == 'inc':
        inc(step[1])
        index += 1
    elif step[0] == 'dec':
        dec(step[1])
        index += 1
    elif step[0] == 'jnz':
        jnz(step[1], step[2]) 

    if index < 0 or index >= len(instructions):
        break

print(registers)
        
