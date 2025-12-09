# Day 2

def find_invalid(mn, mx):
    global total

    half_len = len(str(mx)) // 2
    
    for val in range(max(10,mn), mx+1):
        s = str(val)
        
        for ptrn_lngth in range(1, half_len + 1):
            if len(s) % ptrn_lngth != 0:
                continue

            repeat = len(s) // ptrn_lngth

            if s == s[:ptrn_lngth] * repeat:
                total += val
                #print(val)
                break
            

    
total = 0

f = open('day2.txt','r')
for x in f:
    x = x.strip()
    x = x.split(',')

for s in x:
    s = s.split('-')
    #print(s)
    find_invalid(int(s[0]), int(s[1]))


print(total)

# 31680314021 too high
