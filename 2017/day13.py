#day13

d = {}
offset = 0

f = open("day13_input.txt", "r")
for x in f:
    x = x.replace(":", "")
    x = x.split()
    d[int(x[0])] = int(x[1])
    
#print(d)
severity = 0

answer_found = False

while not answer_found:
    answer_found = True
    for layer, ran in d.items():
        if (layer + offset) % ((ran - 1)*2 ) == 0:
            answer_found = False
            #severity += (layer * ran)
            #print(offset, layer, ran)
            offset += 1
            break
        
#print(severity)
print(offset)
