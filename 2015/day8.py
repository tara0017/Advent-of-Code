# day8

# part 2

added_chars = 0

f = open('day8.txt', 'r')
for x in f:
    x = x.replace('\n', '')
    x = x[1:len(x)-1]

    added_chars += 4    # need 4 chars for starting and ending quotation mark

    for c in x:
        if c == '\"' or c == '\\':
            added_chars += 1

print(added_chars)


"""
# part 1
total_chars  = 0
total_string_chars = 0
count = 0


f = open('day8.txt', 'r')
for x in f:
    x = x.replace('\n', '')
    
    chars  = len(x)
    string_chars = (len(x) - 2)

    i = 0
    while '\\\\' in x[i:] and i < len(x)-1:
        string_chars -= 1
        i += x[i:].index('\\\\') + 2
        if (x[i] =='x'):
             temp = x[:i] + 'a' + x[i+1:]
             #print('x    = ',x)
             #print('temp = ', temp)
             x = temp
        

    i = 0
    while '\\"' in x[i:len(x)-1]:
        string_chars -= 1
        i += x[i:].index('\\"') + 2

    i = 0
    while '\\x' in  x[i:]:
        string_chars -= 3
        i += x[i:].index('\\x') + 3

    count += 1

    total_chars += chars
    total_string_chars += string_chars
        
print(total_chars)
print(total_string_chars)
print(total_chars - total_string_chars)

"""
