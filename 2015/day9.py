# day9

def process_line(x):
    global dist

    neighbor = (x[1], int(x[2]))
    if x[0] not in dist:
        dist[x[0]] = [neighbor]
    else:
        dist[x[0]].append(neighbor)
        
        
    neighbor = (x[0], int(x[2]))
    if x[1] not in dist:
        dist[x[1]] = [neighbor]
    else:
        dist[x[1]].append(neighbor)


def get_length(route):
    total = 0
    for i in range(len(route)-1):
        total += get_dist(route[i], route[i+1])
    return total


def get_dist(c1, c2):
    global dist

    for d in dist[c1]:
        if d[0] == c2:
            return d[1]
        

dist = dict() 
        
f = open('day9.txt', 'r')
for x in f:
    x = x.replace('to', '')
    x = x.replace('=', '')
    x = x.replace('\n', '')
    x = x.split()
    process_line(x)


cities = ['Faerun', 'Norrath', 'Tristram', 'AlphaCentauri', 'Arbre', 'Snowdin', 'Tambi', 'Straylight'] 

longest_route = [0, []]
# generate all routes
for a in cities:
    for b in cities:
        if b == a:
            continue
        for c in cities:
            if c == a or c == b:
                continue
            for d in cities:
                if d == a or d == b or d == c:
                    continue
                for e in cities:
                    if e == a or e == b or e == c or e == d:
                        continue
                    for f in cities:
                        if f == a or f == b or f == c or f == d or f == e:
                            continue
                        for g in cities:
                            if g == a or g == b or g == c or g == d or g == e or g == f:
                                continue
                            for h in cities:
                                if h == a or h == b or h == c or h == d or h == e or h == f or h == g:
                                    continue
                                route = [a,b,c,d,e,f,g,h]
                                
                                route_length = get_length(route)
                                if route_length > longest_route[0]:
                                    longest_route = [route_length, route]

print(longest_route)

