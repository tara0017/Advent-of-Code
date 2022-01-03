# day 22
import copy

# return [min x, max x, min y, max y, min z, max z]
def process(s):
    inst = [s[0], int(s[2]), int(s[3]), int(s[5]), int(s[6]), int(s[8]), int(s[9])]
    return inst
    
    
def turn_on_off_cubes2(s):
    global cubes, num_lit_cubes
        
    for x in range(s[1], s[2] + 1):
        if x > 50 or x < -50:
            continue
        for y in range(s[3], s[4] + 1):
            if y > 50 or y < -50:
                continue
            for z in range(s[5], s[6] + 1):
                if z > 50 or z < -50:
                    continue
                
                if s[0] == 'on':    # turn on
                    if ((x,y,z) not in cubes) or cubes[(x,y,z)] == 0:
                        num_lit_cubes += 1
                    cubes[(x,y,z)] = 1
                else:               # turn off
                    if (x,y,z) in cubes and cubes[(x,y,z)] == 1:
                        num_lit_cubes -= 1
                    cubes[(x,y,z)] = 0

        
def turn_on_off_cubes(s):
    global cubes, num_lit_cubes
        
    for x in range(s[1], s[2] + 1):
        if x > 50 or x < -50:
            continue
        for y in range(s[3], s[4] + 1):
            if y > 50 or y < -50:
                continue
            for z in range(s[5], s[6] + 1):
                if z > 50 or z < -50:
                    continue
                
                if (x,y,z) in cubes:
                    continue
                
                if s[0] == 'on':    # turn on
                    num_lit_cubes += 1
                    cubes[(x,y,z)] = 1
                else:               # turn off
                    cubes[(x,y,z)] = 0


# global variables
reboot_steps = []
num_lit_cubes = 0

# read input data
f = open('day22.txt','r')
for x in f:
    x = x.strip()
    x = x.replace('..', ' ')
    x = x.replace('=', ' ')
    x = x.replace(',', ' ')
    x = x.split()
    reboot_steps.append(process(x))

# part 1
"""
cubes = dict()
for step in range(len(reboot_steps) - 1, -1, -1):
    turn_on_off_cubes(reboot_steps[step])
print(num_lit_cubes)
"""

# part 2
class region:
    def __init__(self, value, xmin, xmax, ymin, ymax, zmin, zmax):
        self.value = value
        self.xmin  = xmin
        self.xmax  = xmax
        self.ymin  = ymin
        self.ymax  = ymax
        self.zmin  = zmin
        self.zmax  = zmax
        

def turn_on_off_regions(s):
    global regions, num_lit_cubes

    # find region/s of new coordinates
    new_regions = get_new_regions(s)
    
    if new_regions != None:
        # add new regions to global regions dict
        for nr in new_regions:
            regions.add(nr)
            if nr.value == 'on':
                lit = (nr.xmax - nr.xmin + 1) * (nr.ymax - nr.ymin + 1) * (nr.zmax - nr.zmin + 1)
                num_lit_cubes += lit
        

def get_new_regions(s):
    global regions, num_lit_cubes

    new_regions = set()
    reg = region(s[0], s[1], s[2], s[3], s[4], s[5], s[6])
    new_regions.add(reg)

    
    # update set of new_regions based on each region already claimed    
    for r in regions:
        new_regions = trim_regions(new_regions, r)

    #print(len(new_regions))
    return new_regions


# nr_set = set of potential new regions
# r = region already claimed (needs to be removed from each item in nr_set)
def trim_regions(nr_set, r):
    new_regions = set()

    for nr in nr_set:
        #check x coordinates
        tempx = trim_along_x_axis(nr, r)            #returns [set of regions not overlapping, overlapping region]
        for item in tempx[0]:
            new_regions.add(item)

        if tempx[1] != None:        # some overlap exists
            tempy = trim_along_y_axis(tempx[1], r)      #returns [set of regions not overlapping, overlapping region]
            for item in tempy[0]:
                new_regions.add(item)

            if tempy[1] != None:    #some overlap exists
                tempz = trim_along_z_axis(tempy[1], r)      #returns [set of regions not overlapping, overlapping region]
                for item in tempz[0]:
                    new_regions.add(item)
                #item tempz[1] overlaps the original 'r' region and should not be counted 
    return new_regions


# returns [set of regions not overlapping, overlapping region]
def trim_along_x_axis(nr, r):
    no_overlap = set()

    #nr completely enclosed by r
    if (nr.xmax <= r.xmax) and (nr.xmin >= r.xmin):
        return [no_overlap, nr]
    
    # no overlap at all (nr completely to right/left of r)
    elif (nr.xmax < r.xmin) or (nr.xmin > r.xmax):
        no_overlap.add(nr)
        return [no_overlap, None]

    # partial overlap to the left of r
    elif (nr.xmin < r.xmin) and (nr.xmax <= r.xmax):
        nr1 = copy.deepcopy(nr)     #non-overlapping portion
        nr1.xmax = r.xmin - 1
        no_overlap.add(nr1)

        nr2 = copy.deepcopy(nr)     #overlaping portion
        nr2.xmin = r.xmin
        
        return [no_overlap, nr2]

    # partial overlap to the right of r
    elif (nr.xmin >= r.xmin) and (nr.xmax > r.xmax):
        nr1 = copy.deepcopy(nr)     #non-overlapping portion
        nr1.xmin = r.xmax + 1
        no_overlap.add(nr1)

        nr2 = copy.deepcopy(nr)     #overlaping portion
        nr2.xmax = r.xmax
        
        return [no_overlap, nr2]
        
    #nr completely engulfs r
    elif (nr.xmin < r.xmin) and (nr.xmax > r.xmax):
        nr1 = copy.deepcopy(nr)     #left non-overlapping portion
        nr1.xmax = r.xmin - 1
        no_overlap.add(nr1)

        nr2 = copy.deepcopy(nr)     #right non-overlapping portion
        nr2.xmin = r.xmax + 1
        no_overlap.add(nr2)

        nr3 = copy.deepcopy(nr)     #overlaping portion
        nr3.xmin = r.xmin
        nr3.xmax = r.xmax
        
        return [no_overlap, nr3]
    

# returns [set of regions not overlapping, overlapping region]
def trim_along_y_axis(nr, r):
    no_overlap = set()

    #nr completely enclosed by r
    if (nr.ymax <= r.ymax) and (nr.ymin >= r.ymin):
        return [no_overlap, nr]
    
    # no overlap at all (nr completely to right/left of r)
    elif (nr.ymax < r.ymin) or (nr.ymin > r.ymax):
        no_overlap.add(nr)
        return [no_overlap, None]

    # partial overlap to the left of r
    elif (nr.ymin < r.ymin) and (nr.ymax <= r.ymax):
        nr1 = copy.deepcopy(nr)     #non-overlapping portion
        nr1.ymax = r.ymin - 1
        no_overlap.add(nr1)

        nr2 = copy.deepcopy(nr)     #overlaping portion
        nr2.ymin = r.ymin
        
        return [no_overlap, nr2]

    # partial overlap to the right of r
    elif (nr.ymin >= r.ymin) and (nr.ymax > r.ymax):
        nr1 = copy.deepcopy(nr)     #non-overlapping portion
        nr1.ymin = r.ymax + 1
        no_overlap.add(nr1)

        nr2 = copy.deepcopy(nr)     #overlaping portion
        nr2.ymax = r.ymax
        
        return [no_overlap, nr2]
        
    #nr completely engulfs r
    elif (nr.ymin < r.ymin) and (nr.ymax > r.ymax):
        nr1 = copy.deepcopy(nr)     #left non-overlapping portion
        nr1.ymax = r.ymin - 1
        no_overlap.add(nr1)

        nr2 = copy.deepcopy(nr)     #right non-overlapping portion
        nr2.ymin = r.ymax + 1
        no_overlap.add(nr2)

        nr3 = copy.deepcopy(nr)     #overlaping portion
        nr3.ymin = r.ymin
        nr3.ymax = r.ymax
        
        return [no_overlap, nr3]
    

# returns [set of regions not overlapping, overlapping region]
def trim_along_z_axis(nr, r):
    no_overlap = set()

    #nr completely enclosed by r
    if (nr.zmax <= r.zmax) and (nr.zmin >= r.zmin):
        return [no_overlap, nr]
    
    # no overlap at all (nr completely to right/left of r)
    elif (nr.zmax < r.zmin) or (nr.zmin > r.zmax):
        no_overlap.add(nr)
        return [no_overlap, None]

    # partial overlap to the left of r
    elif (nr.zmin < r.zmin) and (nr.zmax <= r.zmax):
        nr1 = copy.deepcopy(nr)     #non-overlapping portion
        nr1.zmax = r.zmin - 1
        no_overlap.add(nr1)

        nr2 = copy.deepcopy(nr)     #overlaping portion
        nr2.zmin = r.zmin
        
        return [no_overlap, nr2]

    # partial overlap to the right of r
    elif (nr.zmin >= r.zmin) and (nr.zmax > r.zmax):
        nr1 = copy.deepcopy(nr)     #non-overlapping portion
        nr1.zmin = r.zmax + 1
        no_overlap.add(nr1)

        nr2 = copy.deepcopy(nr)     #overlaping portion
        nr2.zmax = r.zmax
        
        return [no_overlap, nr2]
        
    #nr completely engulfs r
    elif (nr.zmin < r.zmin) and (nr.zmax > r.zmax):
        nr1 = copy.deepcopy(nr)     #left non-overlapping portion
        nr1.zmax = r.zmin - 1
        no_overlap.add(nr1)

        nr2 = copy.deepcopy(nr)     #right non-overlapping portion
        nr2.zmin = r.zmax + 1
        no_overlap.add(nr2)

        nr3 = copy.deepcopy(nr)     #overlaping portion
        nr3.zmin = r.zmin
        nr3.zmax = r.zmax
        
        return [no_overlap, nr3]

    
regions = set()
for step in range(len(reboot_steps) - 1, -1, -1):
    turn_on_off_regions(reboot_steps[step])
    print(step)


print(num_lit_cubes)








    




