#day 12
class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.position = [x, y, z]
        self.velocity = [0,0,0]
        #self.next_vel = [0,0,0]
    

def update_velocity(m):
    global moons
    v = m.velocity
    for moon in moons:
        if m == moon:
            continue
        for i in range(len(m.position)):
            if m.position[i] > moon.position[i]:
                v[i] -= 1
            elif m.position[i] < moon.position[i]:
                v[i] += 1
    return v

def update_position(m):
    p = []
    for i in range(len(m.position)):
        p.append(m.position[i] + m.velocity[i])
    return p
    
def pot_energy(m):
    pe = 0
    for p in m.position:
        pe += abs(p)
    return pe

def kin_energy(m):
    ke = 0
    for v in m.velocity:
        ke += abs(v)
    return ke

def get_condition():
    state = ""
    for m in moons:
        for p in m.position:
            state = state + str(p)
        for v in m.velocity:
            state = state + str(v)
    return state
            
"""
def get_condition():
    state = []
    for m in moons:
        row = (m.position, m.velocity)
        state.append(row)
        #print(state)
    return state
"""

#sample data
#moons = [Moon(-1, 0, 2), Moon(2, -10, -7), Moon(4, -8, 8), Moon(3, 5, -1)]
"""
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
"""
#moons = [Moon(-8, -10, 0), Moon(5, 5, 10), Moon(2, -7, 3), Moon(9, -8, -3)]
"""
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>
"""


moons = [Moon(6, -2, -7), Moon(-6, -7, -4), Moon(-9, 11, 0), Moon(-3, -4, 6)]
#print("CONDITION", get_condition())

    
time = 0
states = []
states.append(get_condition())





#part1
while time < 1000:
    #if time %10 == 0:
    #    print("=========================")
    #    print(time)
    #    for m in moons:
    #        print (m.position, "\t", m.velocity)
    for m in moons:
        m.velocity = update_velocity(m)
    for m in moons:
        m.position = update_position(m)
    time += 1

for m in moons:
    print (m.position, "\t", m.velocity)
    
total_energy = 0
for m in moons:
    print(pot_energy(m), kin_energy(m))
    total_energy += pot_energy(m)*kin_energy(m)
print(total_energy)


"""
while time < 1000000:
    for m in moons:
        m.velocity = update_velocity(m)
    for m in moons:
        m.position = update_position(m)
    cond = get_condition()
    time += 1
    if cond in states:
        print("TIME: ", time, "\t", cond)
        break
    else:
        states.append(cond)
    
    if time == 11:
        break
    for m in moons:
        print ("------------", time, m.position, "\t", m.velocity)
    

for m in moons:
    print (time, m.position, "\t", m.velocity)
"""
