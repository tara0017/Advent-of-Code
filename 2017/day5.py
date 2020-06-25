#day5

instructions = []
f = open("day5_input.txt", "r")
for x in f:
    instructions.append(int(x))
#print(instructions)

#instructions = [0, 3, 0, 1, -3]    
steps = 0
index = 0
while index >= 0 and index < len(instructions):
    #print(steps, instructions)
    next_index = index + instructions[index]
    if instructions[index] >= 3:
        instructions[index] -= 1
    else:    
        instructions[index] += 1
    index = next_index
    steps += 1
    
print(steps)

