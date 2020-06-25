#day12
def find_connected_programs(p):
    global s, d, newly_connected_programs
    connected_p = d[p]

    for x in connected_p:
        if x not in s and x not in newly_connected_programs:
            newly_connected_programs.append(x)

            
d = {}

sets = []

newly_connected_programs = []
is_finished = False

f = open("day12_input.txt", "r")
for x in f:
    x = x.split()
    d[x[0]] = []
    for v in x[2:]:
        v = v.replace(',', '')
        d[x[0]].append(v)


programs = []

while is_finished == False:
    s = set()
    is_finished = True
    for k in d:
        if k not in programs:
            is_finished = False
            #print('----------', k)
            newly_connected_programs.append(k)
            break
        
    while len(newly_connected_programs) > 0:
        program = newly_connected_programs.pop(0)
        s.add(program)
        #print(program)
        find_connected_programs(program)
    sets.append(s)
    for p in s:
        programs.append(p)
    #print(programs)
    #s.clear()

print(len(sets))
for i in range(len(sets)):
    print(len(sets[i]))
