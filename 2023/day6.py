#day 6

def count_wins(t, d):
    mid = t // 2
    wins = 0
    
    while mid * (t - mid) > d:
        wins += 1
        mid  -= 1
    
    if t % 2 == 0:
        return 2 * wins - 1
    return 2 * wins


    
f = open('day6.txt', 'r')

time = None
dist = None

for x in f:
    x = x.split()
    if x[0] == 'Time:':
        time = x
    elif x[0] == 'Distance:':
        dist = x


wins = []
for i in range(1, len(time)):
    wins.append(count_wins(int(time[i]), int(dist[i])))

product = 1
for w in wins:
    product *= w
    
print('Part 1: ', product)



#part 2
t = ''
d = ''
for i in range(1, len(time)):
    t += time[i]
    d += dist[i]


print('Part 2: ', count_wins(int(t), int(d)))
    

