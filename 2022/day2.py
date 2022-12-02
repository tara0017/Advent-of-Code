#day2

def get_score(rps):
    scr = 0

    if rps[1] == 'X':    #rock
        scr = 1
        if rps[0] == 'A':
            scr += 3
        elif rps[0] == 'C':
            scr += 6
    elif rps[1] == 'Y': #paper
        scr = 2
        if rps[0] == 'B':
            scr += 3
        elif rps[0] == 'A':
            scr += 6
    elif rps[1] == 'Z': #scissors
        scr = 3
        if rps[0] == 'C':
            scr += 3
        elif rps[0] == 'B':
            scr += 6
            
    return scr
        

def get_score2(rps):
    scr = 0

    if rps[1] == 'X':    #lose
        scr = 0
        if rps[0] == 'A':
            scr += 3
        elif rps[0] == 'B':
            scr += 1
        elif rps[0] == 'C':
            scr += 2
            
    elif rps[1] == 'Y': #draw
        scr = 3
        if rps[0] == 'A':
            scr += 1
        elif rps[0] == 'B':
            scr += 2
        elif rps[0] == 'C':
            scr += 3
            
    elif rps[1] == 'Z': #win
        scr = 6
        if rps[0] == 'A':
            scr += 2
        elif rps[0] == 'B':
            scr += 3
        elif rps[0] == 'C':
            scr += 1
            
    return scr        



score = 0
score2 = 0

f = open("day2.txt", "r")
for x in f:
    x = x.split()
    score += get_score(x)
    score2 += get_score2(x)
    
print(score)
print(score2)
