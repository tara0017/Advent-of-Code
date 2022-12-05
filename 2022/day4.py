#day4

def fully_contained(s):
    if s[0] >= s[2] and s[1] <= s[3]:
        return True
    if s[0] <= s[2] and s[1] >= s[3]:
        return True
    return False


def overlap(s):
    if s[0] >= s[2] and s[0] <= s[3]:
        return True
    if s[1] >= s[2] and s[1] <= s[3]:
        return True
    
    if s[2] >= s[0] and s[2] <= s[1]:
        return True
    if s[3] >= s[0] and s[3] <= s[1]:
        return True
    
    return False

    
num_contained = 0
num_overlap = 0

f = open("day4.txt", "r")
for x in f:
    x = x.strip()
    x = x.replace('-', ',')
    x = x.split(',')
    for i in range(len(x)):
        x[i] = int(x[i])
        
    if fully_contained(x):
        num_contained += 1

    if overlap(x):
        num_overlap += 1


print(num_contained)
print(num_overlap)
