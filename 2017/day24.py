#day24
parts = set()

f= open('day24_input.txt', 'r')
for x in f:
    x = x.replace('/', ' ')
    x = x.split()
    s = (int(x[0]), int(x[1]))
    parts.add(s)

print(parts)
"""
class node:
    def __init__(self, value, parent, visited_nodes):
        self.value = value
        self.parent = parent
        self.children = []


"""
cue = []    #[last_value, total, route, set of parts not yet used]

longest = 34
strongest = 0
cue.append([0, 0, [], parts])
            
print()
while len(cue) > 0:
    s = cue.pop(0)
    last_value =s[0]
    total = s[1]
    route = s[2]
    unvisited = s[3].copy()
    found_end = True
    
    for p in s[3]:
        if last_value in p:
            found_end = False
            #find new last value
            if p[0] == last_value:
                lv = p[1]
            else:
                lv = p[0]
            #update total
            t = total + p[0] + p[1]
            #update route
            r = route[:]
            r.append(p)
            #update unvisited parts
            uv = unvisited.copy()
            uv.remove(p)

            #add new state back to cue
            state = [lv, t, r, uv]
            cue.append(state)
    if found_end:
        if len(route) >= longest:
            print(total, len(route), route)
            print('------------------------------------')
            longest = len(route)
        """
        if total > strongest:
            print(total, route)
            print('------------------------------------')
            strongest = total
        """
