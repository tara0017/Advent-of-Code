# day23

def increase(reg):
    global a, b
    if reg == 'a':
        a += 1
    elif reg == 'b':
        b += 1

def triple(reg):
    global a, b
    if reg == 'a':
        a *= 3
    elif reg == 'b':
        b *= 3

def half(reg):
    global a, b
    if reg == 'a':
        a /= 2
    elif reg == 'b':
        b /= 2

def jump(amount):
    global i
    i += amount
    
def even_jump(reg, amount):
    global i, a, b
    if reg == 'a':
        if a%2 == 0:    # a is even, jump
            i += amount
        else:           # if a is not even i increases???
            i += 1
    elif reg == 'b':
        if b%2 == 0:    # b is even, jump
            i += amount
        else:           # if b is not even i increases???
            i += 1

def one_jump(reg, amount):
    global i, a, b
    if reg == 'a':
        if a == 1:    # a is odd, jump
            i += amount
        else:           # if a is not odd i increases???
            i += 1
    elif reg == 'b':
        if b == 1:    # b is odd, jump
            i += amount
        else:           # if b is not odd i increases???
            i += 1

            
instructions = []

f = open('day23.txt','r')
for x in f:
    x = x.replace(',', '')
    x = x.split()
    instructions.append(x)

#for j in range(len(instructions)):
#    print(j, instructions[j])

# part 1
a = 0
# part 2
a = 1
b = 0
i = 0

while i < len(instructions) and i >= 0:
    if instructions[i][0] == 'inc':
        increase(instructions[i][1])
        i += 1
    elif instructions[i][0] == 'tpl':
        triple(instructions[i][1])
        i += 1
    elif instructions[i][0] == 'hlf':
        half(instructions[i][1])
        i += 1
    elif instructions[i][0] == 'jmp':
        jump(int(instructions[i][1]))    
    elif instructions[i][0] == 'jie':
        even_jump(instructions[i][1], int(instructions[i][2]))
    elif instructions[i][0] == 'jio':
        one_jump(instructions[i][1], int(instructions[i][2]))

print(a, b)
