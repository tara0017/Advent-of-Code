#day10
import copy


def add_pixel():
    global register, cycle, row, image

    if abs((cycle % 40) - register) <= 1:
        row.append('#')
    else:
        row.append('.')

    if len(row) == 40:
        image.append(copy.deepcopy(row))
        row.clear()
    
    
def addx(n):
    global register, cycle, signal_registers, signal_cycles

    add_pixel()
    
    cycle += 1
    if cycle in signal_cycles:
        signal_registers.append(cycle * register)

    add_pixel()

    cycle += 1   
    register += n
    

    
register = 1
cycle = 0
signal_cycles = {20,60,100,140,180,220}
signal_registers = []
image = []
row = []


f = open('test.txt','r')
for x in f:
    x = x.strip()
    x = x.split()
    #if cycle > 217:
    #    print(cycle, x)
        
    if x[0] == 'addx':
        addx(int(x[1]))
    else:
        #print(cycle, register)
        
        add_pixel()
        cycle += 1

    if cycle in signal_cycles:
        signal_registers.append(cycle * register)
        
    #print(cycle, register)
    #break

print(signal_registers)
print(sum(signal_registers))

for r in image:
    for c in r:
        print(c, end = '')
    print()
    
"""
locate sprite (register position)
draw a pixel in position "cycle"
if sprite in that position '#' else '.'
addx
    draw pixel
    update sprite position

ZOBRJFJZ
ZSBRJFJZ

"""
