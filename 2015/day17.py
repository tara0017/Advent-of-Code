# day17

import itertools

# input data        
containers = [33,14,18,20,45,35,16,35,1,13,18,13,50,44,48,6,24,41,30,42]
count   = 0

least_num_buckets        = 0
num_ways_to_fill_buckets = 0

for num_buckets in range(len(containers)):
    for combo in itertools.combinations(containers, num_buckets):
        if sum(combo) == 150:
            count += 1
    if least_num_buckets == 0 and count != 0:
        least_num_buckets = num_buckets
        num_ways_to_fill_buckets = count

print(count)
print(least_num_buckets, num_ways_to_fill_buckets)



