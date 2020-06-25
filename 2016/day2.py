#day2
def get_key(s):
    global key_pad, current_key
    #print(s)
    x = current_key[1]
    y = current_key[0]
    for i in s:
        if i == "U":
            if y > 0:
                y -= 1
        elif i == "D":
            if y < 2:
                y += 1
        elif i == "R":
            if x < 2:
                x += 1
        elif i == "L":
            if x > 0:
                x -= 1
        current_key = [y,x]
        #print(i, current_key)
    return key_pad[y][x]

def get_key2(s):
    global key_pad2, current_key
    #print(s)
    x = current_key[1]
    y = current_key[0]
    for i in s:
        if i == "U":
            if y > 0:
                if key_pad2[y-1][x] != '0':
                    y -= 1
        elif i == "D":
            if y < 4:
                if key_pad2[y+1][x] != '0':
                    y += 1
        elif i == "R":
            if x < 4:
                if key_pad2[y][x+1] != '0':
                    x += 1
        elif i == "L":
            if x > 0:
                if key_pad2[y][x-1] != '0':
                    x -= 1
        current_key = [y,x]
        #print(i, current_key)
    return key_pad2[y][x]


key_pad = ['123', '456', '789']
key_pad2 = ['00100', '02340', '56789', '0ABC0', '00D00']
current_key = [2,0]     

f = open('day2_input.txt', 'r')
for x in f:
    k = get_key2(x)
    print(k)
    





        
