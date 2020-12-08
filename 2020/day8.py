# day8

def run_instructions():
    global instructions, acc_value, answer_found
    index = 0
    visited_indices = set()

    while index not in visited_indices:
        if index == len(instructions):
            answer_found = True
            print("Part 2:")
            break
            
        visited_indices.add(index)

        inst = instructions[index]

        if inst[0] == 'nop':
            index += 1
        elif inst[0] == 'acc':
            acc_value += inst[1]
            index += 1
        elif inst[0] == 'jmp':
            index += inst[1]



def switch_command(i):
    global instructions
    
    if instructions[i][0] == 'nop':
        instructions[i][0] = 'jmp'
    else:
        instructions[i][0] = 'nop'
        

# global variables         
instructions = []
acc_value = 0
nop_ind = []
jmp_ind = []


# read file
i = 0
f = open('day8.txt', 'r')
for x in f:
    x = x.split()
    x[1] = int(x[1])
    instructions.append(x)
    

# part 1
run_instructions()
print(acc_value)


# part 2
answer_found = False
current_i = 0

while not answer_found:
    for i in range(current_i, len(instructions)):
        if instructions[i][0] == 'nop' or instructions[i][0] == 'jmp':
            switch_command(i)
            current_i = i
            run_instructions()
            break

    if not answer_found:
        switch_command(current_i)
        current_i += 1
        acc_value = 0
    
print(acc_value)            
            






