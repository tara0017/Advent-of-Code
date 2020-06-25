#day17

spinlock = [0, 1]
current_location = 1
step = 356

for i in range(2, 50000000):
    #find new location
    current_location = (current_location + step + 1) % len(spinlock)
    #insert value
    spinlock.insert(current_location, i)
    if i % 10**6 == 0:
        print(i)


#print(spinlock)
ind = spinlock.index(0) + 1

print(spinlock[ind])

