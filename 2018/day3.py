#day3
claims = []

f = open("day3_input.txt", "r")
for g in f:
    g = g.replace(",", " ")
    g = g.replace(":", "")
    g = g.replace("x", " ")
    g = g.replace("#", "")
    g = g.replace("@", "")
    g = (g.split())
    claim = []
    for x in g:
        claim.append(int(x))
    claims.append(claim)

points = set()
duplicated_points = set()
claims_that_do_not_overlap = []     #claim may overlap later with another claim that has not yet been processed

for c in claims:
    start_point = (c[1], c[2])
    claim_does_not_overlap = True
    for w in range(c[3]):
        for h in range(c[4]):
            point = (start_point[0] + w, start_point[1] + h)
            if point in points:
                claim_does_not_overlap = False
                duplicated_points.add(point)
            points.add(point)
    if claim_does_not_overlap:
        claims_that_do_not_overlap.append(c)


print(len(duplicated_points))    

def claims_overlap(c, d):
    points_in_c = []
    start = (c[1], c[2])
    for w in range(c[3]):
        for h in range(c[4]):
            point = (start[0] + w, start[1] + h)
            points_in_c.append(point)
    d_start = (d[1], d[2])
    for w in range(d[3]):
        for h in range(d[4]):
            point = (d_start[0] + w, d_start[1] + h)
            if point in points_in_c:
                return True
    return False




#part2
#look at claims that do not overlap in reverse order
reverse = []
for i in range(len(claims_that_do_not_overlap)-1, -1, -1):
    reverse.append(claims_that_do_not_overlap[i])

for c in reverse:
    answer_found = True
    for d in claims:
        if d == c:  #same claim
            continue
        if claims_overlap(c, d):
            answer_found = False
        if answer_found == False:
            break
    if answer_found:
        print (c)
        break
    
    

                                          

