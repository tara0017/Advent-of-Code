# day11


def complete_step():
    global grid, total_flashes

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] += 1
            
    check_for_flashes()
    
    
def check_for_flashes():
    global grid, total_flashes, new_flashes_occur, step_flashes

    new_flashes_occur = False

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            
            # This octopus already flashed during this step
            if grid[y][x] == 'F':
                continue

            # new flash
            elif grid[y][x] > 9:
                grid[y][x] = 'F'
                increment_surrounding(y,x)

    # repeat as long as there were new flashes based off surrounding flashes
    if new_flashes_occur:
        check_for_flashes()

    # count the flashes and reset energy level
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'F':
                total_flashes += 1
                step_flashes += 1
                grid[y][x] = 0
                
                
                
def increment_surrounding(y,x):
    global grid, new_flashes_occur

    for j in range(y-1, y+2):
        for i in range(x-1, x+2):
            # check border/edge locations
            if i < 0 or j < 0 or i >= len(grid[0]) or j >= len(grid):
                continue

            elif grid[j][i] == 'F':
                continue

            else:
                grid[j][i] += 1
                # report new octopusses that should flash
                if grid[j][i] > 9:
                    new_flashes_occur = True
            

def part1():
    for i in range(100):
        complete_step()
    print('Part 1:', total_flashes)


def part2():
    global step_num, step_flashes
    
    while True:
        step_num += 1
        complete_step()

        if step_flashes == 100:
            print('Part 2:', step_num)
            break
        else:
            step_flashes = 0


# global variables    
grid = []
total_flashes = 0
new_flashes_occur = False
step_flashes = 0
step_num = 0


f = open('day11.txt','r')
for x in f:
    row = []
    x = x.strip()
    for i in x:
        row.append(int(i))
    grid.append(row)


#part1()

part2()











    





