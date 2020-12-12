# day12

def part_1():
    global x,y, instructions
    facing = 0      # 0: East, 1: North, 2: West, 3: South

    for inst in instructions:
        if inst[0] == 'E':
            x += int(inst[1:])

        elif inst[0] == 'W':
            x -= int(inst[1:])
        
        elif inst[0] == 'S':
            y -= int(inst[1:])

        elif inst[0] == 'N':
            y += int(inst[1:])

        elif inst[0] == 'L':
            deg = int(inst[1:])
            turns = deg // 90
            facing = (facing + turns) % 4

        elif inst[0] == 'R':
            deg = int(inst[1:])
            turns = deg // 90
            facing = (facing - turns) % 4

        elif inst[0] == 'F':
            dist = int(inst[1:])
            if   facing == 0:   # east
                x += dist
            elif facing == 1:   # north
                y += dist
            elif facing == 2:   # west
                x -= dist
            elif facing == 3:   # south
                y -= dist


def part_2():
    global x,y, instructions
    vector = [10, 1]

    for inst in instructions:
        if inst[0] == 'E':
            vector[0] += int(inst[1:])

        elif inst[0] == 'W':
            vector[0] -= int(inst[1:])
        
        elif inst[0] == 'S':
            vector[1] -= int(inst[1:])

        elif inst[0] == 'N':
            vector[1] += int(inst[1:])


        elif inst[0] == 'L':
            deg = int(inst[1:])
            turns = deg // 90
            for i in range(turns):
                vector = [-1 * vector[1], vector[0]]

        elif inst[0] == 'R':
            deg = int(inst[1:])
            turns = deg // 90
            for i in range(turns):
                vector = [vector[1], -1 * vector[0]]

                          
        elif inst[0] == 'F':
            mult = int(inst[1:])
            x += (mult * vector[0])
            y += (mult * vector[1])


instructions = []
f = open('day12.txt', 'r')
for x in f:
    instructions.append(x)


(x,y) = (0,0)
part_1()
print(x,y, abs(x) + abs(y))


(x,y) = (0,0)
part_2()
print(x,y, abs(x) + abs(y))

