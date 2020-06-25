#day11
def get_dist():
    global d
    return (d['sw'] + d['nw'] - d['se'] - d['ne'])

f = open("day11_input.txt", "r")
for x in f:
    x = x.replace(",", " ")
    x = x.split()

d = {}
d['s']  = 0
d['se'] = 0
d['sw'] = 0
d['n']  = 0
d['ne'] = 0
d['nw'] = 0


farthest = 0
for v in x:
    d[v] += 1
    dist = get_dist()
    if dist > farthest:
        farthest = dist

print(farthest)



"""
while 's' in x:
    if 'n' in x:
        x.remove('s')
        x.remove('n')
    else:
        break
        
while 'se' in x:
    if 'nw' in x:
        x.remove('se')
        x.remove('nw')
    else:
        break
    
while 'sw' in x:
    if 'ne' in x:
        x.remove('sw')
        x.remove('ne')
    else:
        break


    
print(d)
"""
