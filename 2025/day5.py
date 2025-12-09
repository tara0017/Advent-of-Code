# Day 5

id_ranges = []
is_id_ranges = True
ids = set()

f = open('day5.txt', 'r')
for x in f:
    x = x.strip()

    if x == '':
        is_id_ranges = False
        continue

    if is_id_ranges:
        x = x.split('-')
        id_ranges.append((int(x[0]),int(x[1])))
    else:
        ids.add(int(x))

#print(id_ranges)
#print(ids)

count = 0
for i in ids:
    for r in id_ranges:
        if i >= r[0] and i <= r[1]:
            count += 1
            #print(i)
            break
print(count)



# part 2
full_ranges = set()

for r in id_ranges:
    mn, mx = r
    ranges_to_remove = set()
    
    for fr in full_ranges:

        # [ ( ] )
        if mn >= fr[0] and mn <= fr[1]:
            ranges_to_remove.add(fr)
            mn, mx = fr[0], max(fr[1], mx)
            
        # ( [ ) ]
        elif mx >= fr[0] and mx <= fr[1]:
            ranges_to_remove.add(fr)
            mn, mx = min(mn, fr[0]), fr[1]
            
        # ( [ ] )
        elif mn <= fr[0] and mx >= fr[1]:
            ranges_to_remove.add(fr)
            # mn, mx = mn, mx 
        
    for rtr in ranges_to_remove:
        full_ranges.remove(rtr)
    full_ranges.add((mn,mx))


count2 = 0
for fr in full_ranges:
    count2 += (fr[1] + 1 - fr[0])
print(count2)

            
        
