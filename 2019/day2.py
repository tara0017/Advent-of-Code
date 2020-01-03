#day2
def opcode(i):
    global data
    
    if data[i] == 99:
        return 99
    if data[i] == 1:
        data[data[i+3]] = data[data[i+1]] + data[data[i+2]] 
        return i+4
    if data[i] == 2:
        data[data[i+3]] = data[data[i+1]] * data[data[i+2]] 
        return i+4
    
    

f = open("day2_input.txt", "r") 

for i in f:
    data = i.strip().split(",")

for j in range(len(data)):
    data[j] = int(data[j])


"""
#practice input data
data = [1,0,0,0,99]
data = [2,3,0,3,99]
data = [1,1,1,4,99,5,6,0,99]
"""


"""
#part 1
data[1] = 12
data[2] = 2
index = 0
while data[index] != 99:
    index = opcode(index)
print (data)
"""

#part 2
initial_data = data[:]
is_solution_found = False

for noun in range(0, 100):
    if is_solution_found == True:
        break
    for verb in range(0, 100):
        data = initial_data[:]
        data[1] = noun
        data[2] = verb
        index = 0
        while data[index] != 99:
            index = opcode(index)
        if data[0] == 19690720:
            print(noun, verb)
            print(data)
            is_solution_found = True
            break
        
        











