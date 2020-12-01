# day13

# part 2
def get_value(order):
    global values
    total = 0
    for i in range(len(order)-1):
        if order[i] == 'Me' or order[i+1] == 'Me':
            continue
        else:
            total += values[(order[i], order[i+1])]
            total += values[(order[i+1], order[i])]
    return total




names = ['Me', 'Alice', 'Bob', 'Carol', 'David', 'Eric', 'Frank', 'George', 'Mallory']

values = dict()

f = open('day13.txt','r')
for x in f:
    x = x.replace('.', '')
    x = x.split()
    p1 = x[0]
    p2 = x[-1]
    v = int(x[3])
    if x[2] == 'lose':
        v *= -1
    values[(p1, p2)] = v
    # print(x)

highest = 0
# create all arrangments
for a in names:
    for b in names:
        if a == b:
            continue
        for c in names:
            if c == a or c == b:
                continue
            for d in names:
                if d == a or d == b or d == c:
                    continue
                for e in names:
                    if e == a or e == b or e == c or e == d:
                        continue
                    for f in names:
                        if f == a or f == b or f == c or f == d or f == e:
                            continue
                        for g in names:
                            if g == a or g == b or g == c or g == d or g == e or g == f:
                                continue
                            for h in names:
                                if h == a or h == b or h == c or h == d or h == e or h == f or h == g:
                                    continue
                                for i in names:
                                    if i == a or i == b or i == c or i == d or i == e or i == f or i == g or i == h:
                                        continue
                                    order = [i,a,b,c,d,e,f,g,h,i]
                                    v = get_value(order)
                                    if v > highest:
                                        print(v, order)
                                        highest = v




"""
# part 1
names = ['Alice', 'Bob', 'Carol', 'David', 'Eric', 'Frank', 'George', 'Mallory']

values = dict()

f = open('day13.txt','r')
for x in f:
    x = x.replace('.', '')
    x = x.split()
    p1 = x[0]
    p2 = x[-1]
    v = int(x[3])
    if x[2] == 'lose':
        v *= -1
    values[(p1, p2)] = v
    # print(x)

highest = 0
# create all arrangments
for a in names:
    for b in names:
        if a == b:
            continue
        for c in names:
            if c == a or c == b:
                continue
            for d in names:
                if d == a or d == b or d == c:
                    continue
                for e in names:
                    if e == a or e == b or e == c or e == d:
                        continue
                    for f in names:
                        if f == a or f == b or f == c or f == d or f == e:
                            continue
                        for g in names:
                            if g == a or g == b or g == c or g == d or g == e or g == f:
                                continue
                            for h in names:
                                if h == a or h == b or h == c or h == d or h == e or h == f or h == g:
                                    continue
                                order = [h,a,b,c,d,e,f,g,h]
                                v = get_value(order)
                                if v > highest:
                                    print(v, order)
                                    highest = v


"""

                    
    
