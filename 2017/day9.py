#day9

f = open("day9_input.txt", "r")
for x in f:
    print(len(x))

#remove ! and next character    
index = 0
while index < len(x):
    if x[index] == "!":
        x = x[:index] + x[index+2:]
    else:
        index += 1
print(len(x))


#remove garbage
index = 0
garbage_count = 0
while '<' in x:
    start_index = x.find('<')
    end_index   = x.find('>')
    x = x[:start_index] + x[end_index + 1:]
    garbage_count += (end_index - start_index - 1)

print (len(x))
print(x)

#calculate total group score
#x = '{{},{}}'
value = 1
total = 0
for i in range(len(x)):
    if x[i] == '{':
        total += value
        value += 1
    elif x[i] == '}':
        value -= 1
print(total)
print(garbage_count)
