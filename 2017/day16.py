#day16
def spin(n):
    global programs
    programs = programs[-n:] + programs[:-n]


def exchange(i, j):
    global programs
    temp_i = programs[i]
    temp_j = programs[j]
    programs = programs[:i] + temp_j + programs[i+1:]
    programs = programs[:j] + temp_i + programs[j+1:]

    
def partner(p1, p2):
    global programs
    i = programs.index(p1)
    j = programs.index(p2)
    programs = programs[:i] + p2 + programs[i+1:]
    programs = programs[:j] + p1 + programs[j+1:]

    
programs = 'abcdefghijklmnop'

f = open('day16_input.txt', 'r')
for x in f:
    x = x.replace(',', ' ')
    x = x.split()

dance_number = 0
final_position = []

while dance_number < 10**9:
    dance_number += 1

    for op in x:
        if op[0] == 's':
            spin(int(op[1:]))
        elif op[0] == 'x':
            op = op.replace('/', ' ')
            op = op.split()
            p1 = int(op[0][1:])
            p2 = int(op[1])
            exchange(p1, p2)
        elif op[0] == 'p':
            p1 = op[1]
            p2 = op[-1]
            partner(p1, p2)
    if programs not in final_position:
        final_position.append(programs)
    else:
        print(dance_number, final_position.index(programs), programs)
    
print(programs)


