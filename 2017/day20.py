#day20
def clean(x):
    x = x[3:]
    x = x.replace(',', ' ')
    x = x.replace('>', ' ')
    x = x.split()
    a = []
    for v in x:
        a.append(int(v))
    return a

def total_accel(a):
    total = 0
    for v in a:
        total += abs(v)
    return total

particles = []
particle_number = 0

f = open("day20_input.txt", "r")
for x in f:
    x = x.split()
    #print(x)
    p = clean(x[0])
    v = clean(x[1])
    a = clean(x[2])
    particle = [particle_number, p, v, a]
    particles.append(particle)
    """
    s = total_accel(a)
    if s <= 3:
        print(particle_number, a, s, x)
    """
    particle_number += 1

def update_vel(p):
    new_vel = []
    for i in range(len(p[2])):
        new_vel.append(p[2][i] + p[3][i])
    return new_vel

def update_pos(p):
    new_pos = []
    for i in range(len(p[1])):
        new_pos.append(p[1][i] + p[2][i])
    return new_pos

def del_colliding_particles():
    global collisions, particles
    #print("COLLISIONS", collisions)
    remove = []
    if len(collisions) > 0:
        for p in particles:
            if tuple(p[1]) in collisions:
                #print("removed ", p)
                remove.append(p)
    for p in remove:
        particles.remove(p)


positions = set()
collisions = set()
count = 0

while count < 5000:
    #repeat this until all collisions occur (5000 times???)
    #print(count, collisions)
    for particle in particles:
        particle[2] = update_vel(particle)
        #print(particle)
        #break
        particle[1] = update_pos(particle)

        #print(particle)
        #break
        if tuple(particle[1]) in positions:
            collisions.add(tuple(particle[1]))
        else:
            positions.add(tuple(particle[1]))
    del_colliding_particles()
    collisions.clear()
    positions.clear()
    count += 1

print(len(particles))       
    




