#day24
def read_file():
    starting_map = []
    f = open("day24_input.txt", "r")
    for line in f:
        x = line[:-1]
        starting_map += list(x)
    return starting_map

def map_to_string(m):
    global border_indices
    map_index = 0
    string = ""
    for i in range(border_indices[-1] + 1):
        if i in border_indices: #border square
            string += "0"
        else:                   #map square
            #get value from map
            if m[map_index] == "#": #bug here
                string += "1"
            else:
                string += "0"       #no bug
            map_index += 1
    return string
        
def string_to_map(s):
    global border_indices
    for i in range(len(s)):
        if i in border_indices:
            print("B", end = "")
        elif s[i] == "0":
                print(".", end = "")
        elif s[i] == "1":
            print("#", end = "")
        if i%7 == 6:
            print()
    

def update_map(current):
    global map_indices
    next_map = ""
    #print("25 - ", current[25])
    for i in range(len(current)):
        if i in map_indices:    #current location is in map
            bugs_adj = num_adjacent(i, current)
            if current[i] == "1":     #bug currently present
                if bugs_adj != 1:   #not exactly 1 bug adjacent to current position
                    #print(i)
                    next_map += "0" #the bug dies
                else:
                    next_map += "1" #the bug lives
            else:   #currently no bug present
                if bugs_adj == 1 or bugs_adj == 2:
                    next_map += "1" #bug takes over spot
                else:
                    next_map += "0" #stays empty
        else:   #border (do not change)
            next_map += current[i]
    return next_map


###this function only looks at map indices (not border indices)
def num_adjacent(i, current):   
    count = 0
    if current[i-7] == "1": #point above
        count += 1
    if current[i+7] == "1": #point below
        count += 1
    if current[i-1] == "1": #point to the left
        count += 1        
    if current[i+1] == "1": #point to the right
        count += 1
    return count
        

maps = set()
border_indices = []
map_indices = []

#get border and map indices
for i in range(49):
    if i < 7 or i >= 42 or i%7 == 0 or i%7 == 6:
        border_indices.append(i)
    else:
        map_indices.append(i)
#print(border_indices)
#print("----------------------")
#print(map_indices)


starting_map = read_file()  # string with 1=bug and border "0000000010110110...    " 
current_map = map_to_string(starting_map)

"""
print(current_map, "-----", len(current_map))
#string_to_map(current_map)

#print("KKKKKKKK")
print(num_adjacent(25, current_map))
#print("KKKKKKKK")
p = update_map(current_map)
q = update_map(p)
r = update_map(q)
s = update_map(r)
string_to_map(s)

"""
while True:
    maps.add(current_map)
    #print("==========================")
    #string_to_map(current_map)
    next_map = update_map(current_map)
    if(next_map in maps):
        print(next_map)
        print("-------------------")
        string_to_map(next_map)
        break
    else:
        current_map = next_map


string_to_map(next_map)
print(map_indices)

biodiversity = 0
for i in range(len(map_indices)):
    map_index = map_indices[i]
    if next_map[map_index] == "1":     #bug present
        tile_value = 2**i
        biodiversity += tile_value
print (biodiversity) 
    
    
"""
0 	1 	2 	3 	4 	5 	6 	
7 	[8 	9 	10 	11 	12] 	13 	
14 	[15 	16 	17 	18 	19] 	20 	
21 	[22 	23 	24 	25 	26] 	27 	
28 	[29 	30 	31 	32 	33] 	34 	
35 	[36 	37 	38 	39 	40] 	41 	
42 	43 	44 	45 	46 	47 	48
"""

                
            



