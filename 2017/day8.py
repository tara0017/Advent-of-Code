#day8
def make_change(c):
    global d, largest
    amount = int(c[2])
    if c[1] == "dec":
        d[c[0]] -= amount
        if d[c[0]] > largest:
            largest = d[c[0]]
            print("New largest ", largest)
    elif c[1] == "inc":
        d[c[0]] += amount
        if d[c[0]] > largest:
            largest = d[c[0]]
            print("New largest ", largest)
    
def is_condition_true(c):
    global d
    value = int(c[-1])
    entry = d[c[0]]
    if c[1] == "<":
        if entry < value:
            return True
        else:
            return False
    if c[1] == "<=":
        if entry <= value:
            return True
        else:
            return False
    if c[1] == ">":
        if entry > value:
            return True
        else:
            return False
    if c[1] == ">=":
        if entry >= value:
            return True
        else:
            return False
    if c[1] == "==":
        if entry == value:
            return True
        else:
            return False
    if c[1] == "!=":
        if entry != value:
            return True
        else:
            return False
        
d = {}
largest = 0

f= open("day8_input.txt", "r")
for x in f:
    x = x.split()
    if x[0] not in d:
        d[x[0]] = 0
    if x[4] not in d:
        d[x[4]] = 0
    if is_condition_true(x[4:]):
        make_change(x[0:3])
    #print(d)
    #break

print(d)
print("===================================")

for k,v in d.items():
    if v > largest:
        print(k, v)
        largest = v
