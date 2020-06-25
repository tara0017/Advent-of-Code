#day4
def get_id(a):
    global letters
    result = ''
    
    count = letters.copy()
    for word in a:
        for letter in word:
            count[ord(letter)] += 1

    for i in range(5):
        m = max(count, key=count.get)
        result += chr(m)
        count[m] = 0
        #print(m, chr(m), count[m])
    return(result)


def get_name(a, n):
    s = ''
    for word in a:
        s += word
        s+= ' '
    #print('SSSS', s)
    
    shift = n%26
    result = ''
    for letter in s:
        if letter == ' ':
            result += ' '
        else:
            #shift letter
            new_letter = shift + ord(letter)
            if new_letter > 122:
                new_letter += (96-122)
            result += chr(new_letter)
    #print(s, n, result)
    return result

    
letters = {}
for i in range(97, 123):
    letters[i] = 0
#print (letters)
    
total = 0
f = open('day4_input.txt', 'r')
for x in f:
    x = x.replace('-', ' ')
    x = x.replace('[', ' ')
    x = x.replace(']', ' ')
    x = x.split()
    room = x[-1]
    room_id = int(x[-2])
    i = get_id(x[:-2])
    if i == room:
        total += room_id
        name = get_name(x[:-2], room_id)
        print(name, room_id)
        if 'north' in name:
            break
    #print(x)

print(total)







