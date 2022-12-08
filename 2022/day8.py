#day8

def is_visible(y,x):
    global forest
    visibility = True
    
    #check up
    for i in range(0,y):
        if forest[i][x] >= forest[y][x]:
            visibility = False
            break
    if visibility:
        return True
    else:
        visibility = True
    
    #check down
    for i in range(y+1, len(forest)):
        if forest[i][x] >= forest[y][x]:
            visibility = False
            break
    if visibility:
        return True
    else:
        visibility = True
    
    #check left
    for i in range(0, x):
        if forest[y][i] >= forest[y][x]:
            visibility = False
            break
    if visibility:
        return True
    else:
        visibility = True

    #check right
    for i in range(x+1, len(forest[0])):
        if forest[y][i] >= forest[y][x]:
            visibility = False
            break
    if visibility:
        return True
    
    return False


def get_scenic_score(y,x):
    global forest
    directional_score = [0,0,0,0]

    #check up
    for i in range(y-1, -1, -1):
        if forest[i][x] < forest[y][x]:
            directional_score[0] += 1
        else:
            directional_score[0] += 1
            break

    #check down
    for i in range(y+1, len(forest)):
        if forest[i][x] < forest[y][x]:
            directional_score[1] += 1
        else:
            directional_score[1] += 1
            break

    #check left
    for i in range(x-1, -1, -1):
        if forest[y][i] < forest[y][x]:
            directional_score[2] += 1
        else:
            directional_score[2] += 1
            break

    #check right
    for i in range(x+1, len(forest[0])):
        if forest[y][i] < forest[y][x]:
            directional_score[3] += 1
        else:
            directional_score[3] += 1
            break

    score = directional_score[0]*directional_score[1]*directional_score[2]*directional_score[3]
    return score
        

#global variables    
scenic_score = 0
num_visible = 0
forest = []

#read data
f = open('day8.txt','r')
for x in f:
    x= x.strip()
    x = list(x)
    x = [int(s) for s in x]
    forest.append(x)

#process data
for i in range(1, len(forest)-1):
    for j in range(1, len(forest[0])-1):
        if is_visible(i,j):
            num_visible += 1
            
        s = get_scenic_score(i,j)
        scenic_score = max(s, scenic_score)

#add the border trees to the number of visible trees
num_visible += 4*(len(forest)-1)


print('Part 1:', num_visible)
print('Part 2:', scenic_score)
        
