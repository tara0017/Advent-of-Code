#day1



f= open("day1_input.txt", "r")
for x in f:
    x = x.strip()
    print (x)

#part 2
total = 0
dist = int(len(x)/2)

for i in range(-1, len(x) - 1):
    if x[i] == x[(i+dist) % len(x)]:
        total += int(x[i])
    
print("Total = ", total)



"""
#part 1
total = 0
for i in range(-1, len(x) - 1):
    if x[i] == x[i+1]:
        total += int(x[i])
    
print("Total = ", total)
"""
