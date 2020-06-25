#day10
def add_chip(bot, chip_num):
    global inventory, stop
    if bot in inventory:
        inventory[bot].append(chip_num)
        if 17 in inventory[bot] and 61 in inventory[bot]:
            print(bot, inventory[bot])
            #stop = True
    else:
        inventory[bot] = [chip_num]

def distribute_chips(bot):
    global inventory, instructions, outputs
    
    smaller = min(inventory[bot])
    bigger  = max(inventory[bot])
    #assign smaller value if it is to a bot
    if 'bot' in instructions[bot][0]:
        add_chip(int(instructions[bot][0][3:]), smaller)
    else:   #goes to output
        outputs[int(instructions[bot][0][3:])] = smaller
        
    #assign bigger value
    if 'bot' in instructions[bot][1]:
        add_chip(int(instructions[bot][1][3:]), bigger)
    else:   #goes to output
        outputs[int(instructions[bot][1][3:])] = bigger   
    #remove items from inventory[bot]
    inventory[bot] = []
    

stop = False        
inventory    = {}
instructions = {}   #   'bot###' : (small , big)    'out###' : (small, big)
outputs      = {}

f = open('day10_input.txt','r')
for x in f:
    x = x.split()
    if len(x) != 12:
        add_chip(int(x[-1]), int(x[1]))
        #print(x)
    else:
        #print(x)
        instructions[int(x[1])] = (x[5][:3] + x[6], x[-2][:3] + x[-1])
        #print (instructions)
        #break

    
print(inventory)

while stop == False:
    for bot in inventory:
        if len(inventory[bot]) == 2:
            distribute_chips(bot)
            break
    if 0 in outputs and 1 in outputs and 2 in outputs:
        stop = True

print(outputs)
print(outputs[0] * outputs[1] * outputs[2]) 
