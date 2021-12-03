# day2

f = open('day2.txt', 'r')

"""
# part 1
position = [0,0]

for x in f:
    x = x.split()
    #print(x)
    if x[0] == 'forward':
        position[0] += int(x[1])
    elif x[0] == 'down':
        position[1] += int(x[1])
    elif x[0] == 'up':
        position[1] -= int(x[1])

print(position)
print(position[0] * position[1])
"""


# part 2
position2 = [0,0,0]  # horizontal position, aim, depth

for x in f:
    x = x.split()
    if x[0] == 'forward':
        position2[0] += int(x[1])
        position2[2] += (int(x[1]) * position2[1])
    elif x[0] == 'down':
        position2[1] += int(x[1])
    elif x[0] == 'up':
        position2[1] -= int(x[1])

print(position2)
print(position2[0] * position2[2])

