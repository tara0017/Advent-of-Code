#day6

def redistribute(num, ind):
    global data
    d = list(data)
    for i in range(num):
        d[(ind + i) % len(data)] += 1
    data = tuple(d)
           
answer = (14, 13, 12, 11, 9, 8, 8, 6, 6, 4, 4, 3, 1, 1, 0, 12)        
data = (14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4)

history = set()

count = 0

while data not in history:
    history.add(data)
    m = max(data)
    i = data.index(m)
    d = list(data)
    d[i] = 0
    data = tuple(d)
    redistribute(m, i+1)
    count += 1
    if data == answer:
        print(count)

print (count, data)



    
