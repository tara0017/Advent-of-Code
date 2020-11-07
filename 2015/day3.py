# day3

def drop_present(location):
    global present_map

    if location in present_map:
        present_map[location] += 1
    else:
        present_map[location] = 1

    
santa_location = (0,0)
robo_location  = (0,0)
present_map = dict()

present_map[santa_location] = 1
index = 0

f = open("day3.txt", "r")
for x in f:
    for i in x:
        index += 1

        if index % 2 == 1:  # santa move
            loc = list(santa_location)
        else:               # robo move
            loc = list(robo_location)
            
        if i == "^":
            loc[1] += 1
        elif i == "v":
            loc[1] -= 1
        elif i == ">":
            loc[0] += 1
        elif i == "<":
            loc[0] -= 1

        if index % 2 == 1:  # santa move
            santa_location = tuple(loc)
        else:               # robo move
            robo_location = tuple(loc)
            
        drop_present(tuple(loc))

print(len(present_map))
