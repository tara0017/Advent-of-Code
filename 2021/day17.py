# day 17
def get_min_x_value(v):
    x = 1
    # sum of values from 0 up to x must be >= v
    while (x * (x + 1) / 2) < v:
        x += 1
    return x

def hits_target(xv, yv):
    global target_x_range, target_y_range
    x = 0
    y = 0
    step = 0
    while (x <= target_x_range[1]) and (y >= target_y_range[0]):
        x += max(0, xv - step)
        y += (yv - step)
        if x >= target_x_range[0] and x <= target_x_range[1]:
            if y >= target_y_range[0] and y <= target_y_range[1]:
                return True
        step += 1
        
    return False


f = open('day17.txt', 'r')
for x in f:
    #x = 'target area: x=20..30, y=-10..-5'
    x = x.strip()
    x = x.replace('..', ' ')
    x = x.replace('=', ' ')
    x = x.replace(',', '')
    x = x.split()
    target_y_range = [int(x[-2]), int(x[-1])]
    target_x_range = [int(x[-5]), int(x[-4])]
    

# part 1
temp = abs(target_y_range[0]) - 1
h = int(temp * (temp + 1) / 2)
print('Max height:', h)


# part 2
# min/max values to check for x_velocity and y_velocity
min_xv = get_min_x_value(target_x_range[0])
max_xv = target_x_range[1]

min_yv = target_y_range[0]
max_yv = abs(target_y_range[0]) - 1

initial_velocities = []
for xv in range(min_xv, max_xv + 1):
    for yv in range(min_yv, max_yv + 1):
        if hits_target(xv, yv):
            initial_velocities.append((xv, yv))
            
print('Number of initial velocities:', len(initial_velocities))












