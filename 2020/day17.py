# day17

def read_row(r, s):
    global grid
    
    for col in range(len(s)):
        if s[col] == '#':
            coord = (col, r, 0)     # (X, Y, Z)
            grid[coord] = 1
            coord2 = (col, r, 0, 0) # (X, Y, Z, W)
            grid2[coord2] = 1


def read_file():
    f = open('day17.txt','r')
    row = 0
    for x in f:
        read_row(row, x)
        row += 1


def update_min_max(coord):
    global min_x, max_x, min_y, max_y, min_z, max_z

    (x,y,z) = coord
    if x < min_x:
        min_x = x
    elif x > max_x:
        max_x = x

    if y < min_y:
        min_y = y
    elif y > max_y:
        max_y = y
        
    if z < min_z:
        min_z = z
    elif z > max_z:
        max_z = z


def update_min_max2(coord):
    global min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w

    (x,y,z, w) = coord
    if x < min_x:
        min_x = x
    elif x > max_x:
        max_x = x

    if y < min_y:
        min_y = y
    elif y > max_y:
        max_y = y
        
    if z < min_z:
        min_z = z
    elif z > max_z:
        max_z = z

    if w < min_w:
        min_w = w
    elif w > max_w:
        max_w = w
        

def get_num_neighbors(coord):
    global grid
    
    (x,y,z) = coord
    num = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                new_coord = (x+i, y+j, z+k)
                if new_coord == coord:  # same point
                    continue
                if new_coord in grid:   # is it a valid key
                    if grid[new_coord] == 1:
                        num += 1
    return num


def get_num_neighbors2(coord):
    global grid2
    
    (x,y,z,w) = coord
    num = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for m in range(-1, 2):
                    new_coord = (x+i, y+j, z+k, w+m)
                    if new_coord == coord:  # same point
                        continue
                    if new_coord in grid2:   # is it a valid key
                        if grid2[new_coord] == 1:
                            num += 1
    return num


def switch_value(c):
    global grid
    
    if c in grid:
        if grid[c] == 1:
            grid[c] = 0
            update_min_max(c)
        else:
            grid[c] = 1
            update_min_max(c)
    else:
        grid[c] = 1
        update_min_max(c)

    
def switch_value2(c):
    global grid2
    
    if c in grid2:
        if grid2[c] == 1:
            grid2[c] = 0
            update_min_max2(c)
        else:
            grid2[c] = 1
            update_min_max2(c)
    else:
        grid2[c] = 1
        update_min_max2(c)

        
def part_1():
    global min_x, max_x, min_y, max_y, min_z, max_z, grid

    for i in range(6):
        coords_to_change = []
        for x in range(min_x - 1, max_x + 2):
            for y in range(min_y - 1, max_y + 2):
                for z in range(min_z - 1, max_z + 2):
                    coord = (x, y, z)
                    num_neighbors = get_num_neighbors(coord)
                
                    if coord in grid:
                        if grid[coord] == 1:    # active
                            if num_neighbors != 2 and num_neighbors != 3:
                                coords_to_change.append(coord) # switch
                                
                        elif grid[coord] == 0:  # inactive
                            if num_neighbors == 3:
                                coords_to_change.append(coord) # switch

                    else:   #new coordinate point (can only be inactive)
                        if num_neighbors == 3:
                            coords_to_change.append(coord)     # switch

        for c in coords_to_change:
            switch_value(c)



def part_2():
    global min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w, grid2

    for i in range(6):
        coords_to_change = []
        for x in range(min_x - 1, max_x + 2):
            for y in range(min_y - 1, max_y + 2):
                for z in range(min_z - 1, max_z + 2):
                    for w in range(min_w - 1, max_w + 2):
                        coord = (x, y, z, w)
                        num_neighbors = get_num_neighbors2(coord)

                        if coord in grid2:
                            if grid2[coord] == 1:    # active
                                if num_neighbors != 2 and num_neighbors != 3:
                                    coords_to_change.append(coord) # switch
                                    
                            elif grid2[coord] == 0:  # inactive
                                if num_neighbors == 3:
                                    coords_to_change.append(coord) # switch

                        else:   #new coordinate point (can only be inactive)
                            if num_neighbors == 3:
                                coords_to_change.append(coord)     # switch
        
        for c in coords_to_change:
            switch_value2(c)


def count_active():
    global grid

    total = 0
    for g in grid:
        if grid[g] == 1:
            total += 1
    return total


def count_active2():
    global grid2

    total = 0
    for g in grid2:
        if grid2[g] == 1:
            total += 1
    return total

            
grid = dict()
grid2 = dict()

read_file()

min_x = -1
max_x = 8
min_y = -1
max_y = 8
min_z = -1
max_z = 8
min_w = -1
max_w = 8
    
part_1()
print('Part 1:', count_active())

part_2()
print('Part 2:', count_active2())
            
