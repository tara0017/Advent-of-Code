#day6

def find_marker(x, ind):
    a = set()
    for i in range(ind, len(x)):
        a.clear()
        for j in range(i-3, i+1):
            a.add(x[j])
        if len(a) == 4:
            return i+1
        

def find_marker2(x, ind):
    a = set()
    for i in range(ind, len(x)):
        a.clear()
        for j in range(i-13, i+1):
            a.add(x[j])
        if len(a) == 14:
            return i+1
        
    
f = open('day6.txt','r')
for x in f:
    #print(find_marker(x,3))
    print(find_marker2(x,13))
