# day 19
import math
"""
class beacon:
    def __init__(self, scanner, dist_to_neighbors = dict()):
        self.scanner = scanner
        self.dist_to_neighbors = dist_to_neighbors
"""

class scanner:
    def __init__(self, name, beacons):
        self. name = name
        self.beacons = beacons

    """
    returns dictionary of SQUARED distances for each neighboring beacon 
    """
    def get_dist_to_neighbors(self, beacon):
        distances = dict()
        for b in self.beacons:
            if b == beacon:
                continue
            dist = (beacon[0] - b[0])**2 + (beacon[1] - b[1])**2 +  (beacon[2] - b[2])**2
            distances[b] = dist
        return distances
            


"""
transformation must be in the form ('','','') with 
each string's 1st char a '1' or '-', 2nd char 'x', 'y', or 'z' and 
the rest of the expression '+###' or '-##'

ex. ('1y+147', '1x+155', '-z-1150')  =>   (x, y, z)
"""
def get_adjusted_pos(point, transformation):
    p = [0,0,0]
    #check for rotation in x coordinate
    if 'y' in transformation[0]:
        p[0] = point[1]
    elif 'z' in transformation[0]:
        p[0] = point[2]
    else:
        p[0] = point[0]
    #check for rotation in y coordinate
    if 'y' in transformation[1]:
        p[1] = point[1]
    elif 'z' in transformation[1]:
        p[1] = point[2]
    else:
        p[1] = point[0]
    #check for rotation in z coordinate
    if 'y' in transformation[2]:
        p[2] = point[1]
    elif 'z' in transformation[2]:
        p[2] = point[2]
    else:
        p[2] = point[0]

    #check for reflections and translate
    for i in range(3):
        if transformation[i][0] == '-':
            p[i] *= -1

        p[i] += int(transformation[i][2:])

    return tuple(p)

    
        


"""
adds the scanner and associated beacons to the global map (orientation
is based on scanner 0's position)
global_map =>    key: global (x,y,z)      value: scanner/beacon
"""
def add_reading_to_global_map(scanner_name, transformation):
    global global_map, scanners
    
    for s in scanners:
        if s.name != scanner_name:
            continue
        else:
            # add adjusted scanner position to gloabl map
            p = get_adjusted_pos((0,0,0), transformation)
            global_map[p] = 'scanner'
            
            for b in s.beacons:
                #add adjusted beacon position to global map
                p = get_adjusted_pos(b, transformation)
                global_map[p] = 'beacon'
            


def count_matches(d, next_d):
    count = 0
    
    for item in d.values():
        if item in next_d.values():
            count += 1
    return count

def find_overlapping_scanners(name):
    # Find overlapping scanners
    for s in scanners:
        if s.name != name:
            continue
        for b in s.beacons:
            d = s.get_dist_to_neighbors(b)

            for next_s in scanners:
                if next_s == s or next_s.name in processed_scanners:
                    continue
                for next_b in next_s.beacons:
                    next_d = next_s.get_dist_to_neighbors(next_b)
                    if count_matches(d, next_d) >= 11:
                        print(s.name, b, '\t', next_s.name, next_b)
                        break


def print_dist_to_beacon(s_name, point):
    #print distances for given point
    for s in scanners:
        if s.name != s_name:
            continue
        print(s.name)
        print('---------------------------------------')
        for b in s.beacons:
            if b != point :
                continue
            print(b)
            d = s.get_dist_to_neighbors(b)
            for k,v in d.items():
                print(k, '\t', v)
            break
        break

                    
def get_dist_to_beacon(s_name, point):
    #print distances for given point
    for s in scanners:
        if s.name != s_name:
            continue
        print(s.name)
        print('---------------------------------------')
        for b in s.beacons:
            if b != point :
                continue
            print(b)
            d = s.get_dist_to_neighbors(b)
            distances = []
            for k,v in d.items():
                distances.append(v)
            return distances
        break


def match_dist(dist):
    # match distances
    for s in scanners:
        
        for b in s.beacons:
            d = s.get_dist_to_neighbors(b)
            if dist in d.values():
                print(s.name)
                print(b)
                print('---------------------------------------')
                        
                for k,v in d.items():
                    print(k, '\t', v)
                print()


def get_largest_dist(s):
    global scnrs

    max_dist = 0
    for sc in scnrs:
        d = 0
        for i in range(3):
            d += abs(s[i] - sc[i])
        if d > max_dist:
            max_dist = d
    return max_dist

    
# global variables                          
global_map = dict()     # key: global (x,y,z)      value: scanner/beacon
scanners = set()
scanner_name = ''
beacons = set()

# read input data and create scanners
f = open('day19.txt', 'r')
for x in f:
    x = x.strip()
    if x == '':
        #print(beacons)
        s = scanner(scanner_name, beacons)
        scanners.add(s)
        beacons = set()
    elif x[0:2] == '--':
        scanner_name = x
    else:
        x = x.split(',')
        for i in range(len(x)):
            x[i] = int(x[i])
        beacons.add(tuple(x))


# create global map by rotating and/or translating each scanner reading
add_reading_to_global_map('--- scanner 0 ---', ('1x+0', '1y+0', '1z+0'))
add_reading_to_global_map('--- scanner 38 ---', ('1y+147', '1x+155', '-z-1150'))
add_reading_to_global_map('--- scanner 15 ---', ('1z-1111', '-x-15', '-y-1172'))
add_reading_to_global_map('--- scanner 17 ---', ('-y+84', '-x-12', '-z-2408'))
add_reading_to_global_map('--- scanner 35 ---', ('-z-1069', '1y+1334', '1x-1335'))
add_reading_to_global_map('--- scanner 10 ---', ('1y+140', '1z+1336', '1x-2439'))
add_reading_to_global_map('--- scanner 4 ---', ('-z+152', '1y+57', '1x-3678'))
add_reading_to_global_map('--- scanner 5 ---', ('-y-1125', '-z+2470', '1x-1239'))
add_reading_to_global_map('--- scanner 31 ---', ('1x-1172', '1y+1211', '1z-2375'))
add_reading_to_global_map('--- scanner 6 ---', ('-x+73', '1z+2415', '1y-2429'))
add_reading_to_global_map('--- scanner 33 ---', ('1x+91', '-z+1367', '1y-3627'))
add_reading_to_global_map('--- scanner 36 ---', ('1x+25', '-z-1081', '1y-3562'))
add_reading_to_global_map('--- scanner 26 ---', ('-y-1061', '1z+3690', '-x-1300'))
add_reading_to_global_map('--- scanner 18 ---', ('1y-2300', '1x+2420', '-z-1172'))
add_reading_to_global_map('--- scanner 2 ---', ('1y-2296', '-z+1210', '-x-2351'))
add_reading_to_global_map('--- scanner 29 ---', ('-y+130', '-z+2535', '1x-3661'))
add_reading_to_global_map('--- scanner 28 ---', ('1z+61', '-y+1318', '1x-4788'))
add_reading_to_global_map('--- scanner 22 ---', ('-y+40', '1x-2227', '1z-3679'))
add_reading_to_global_map('--- scanner 34 ---', ('1x+37', '-z+3619', '1y-1177'))
add_reading_to_global_map('--- scanner 7 ---', ('1x-1041', '-z+3750', '1y-2376'))
add_reading_to_global_map('--- scanner 23 ---', ('-x-7', '-y+2465', '1z-4812'))
add_reading_to_global_map('--- scanner 8 ---', ('-x-1166', '1y+2471', '-z-3551'))
add_reading_to_global_map('--- scanner 3 ---', ('1z-1230', '-y+1218', '1x-4909'))
add_reading_to_global_map('--- scanner 21 ---', ('-x+1189', '-z+1325', '-y-4821'))
add_reading_to_global_map('--- scanner 13 ---', ('-y-1133', '1z-2226', '-x-3620'))
add_reading_to_global_map('--- scanner 1 ---', ('1x+39', '1z-3432', '-y-3735'))
add_reading_to_global_map('--- scanner 20 ---', ('1z+43', '1x-2315', '1y-2539'))
add_reading_to_global_map('--- scanner 14 ---', ('-z+86', '-x+4852', '1y-1290'))
add_reading_to_global_map('--- scanner 16 ---', ('1z-1168', '1y+4811', '-x-2507'))
add_reading_to_global_map('--- scanner 37 ---', ('1z+30', '1x+2407', '1y-5973'))
add_reading_to_global_map('--- scanner 25 ---', ('-x+1176', '-y+1237', '1z-5981'))
add_reading_to_global_map('--- scanner 9 ---', ('-z-2428', '-y-2405', '-x-3634'))
add_reading_to_global_map('--- scanner 12 ---', ('-z+10', '1x+4959', '-y+1'))
add_reading_to_global_map('--- scanner 19 ---', ('1x+51', '-y+6081', '-z-1202'))
add_reading_to_global_map('--- scanner 30 ---', ('1y+1182', '1x+2551', '-z-6086'))
add_reading_to_global_map('--- scanner 32 ---', ('1y+4', '-z+6024', '-x-123'))
add_reading_to_global_map('--- scanner 39 ---', ('-y-1091', '1z+4964', '-x-52'))
add_reading_to_global_map('--- scanner 27 ---', ('1y-1201', '1z+6159', '1x-1249'))
add_reading_to_global_map('--- scanner 24 ---', ('-x+139', '1z+7342', '1y-1144'))
add_reading_to_global_map('--- scanner 11 ---', ('1y-2393', '-x+4828', '1z-81'))


processed_scanners = {'--- scanner 0 ---', '--- scanner 38 ---','--- scanner 15 ---', '--- scanner 17 ---', 
                      '--- scanner 35 ---', '--- scanner 10 ---','--- scanner 4 ---', '--- scanner 5 ---',
                      '--- scanner 31 ---', '--- scanner 6 ---','--- scanner 33 ---', '--- scanner 36 ---',
                      '--- scanner 26 ---', '--- scanner 18 ---','--- scanner 2 ---', '--- scanner 29 ---',
                      '--- scanner 28 ---', '--- scanner 22 ---','--- scanner 34 ---', '--- scanner 7 ---',
                      '--- scanner 23 ---', '--- scanner 8 ---', '--- scanner 3 ---', '--- scanner 21 ---',
                      '--- scanner 13 ---', '--- scanner 1 ---', '--- scanner 20 ---', '--- scanner 14 ---',
                      '--- scanner 16 ---', '--- scanner 37 ---', '--- scanner 25 ---', '--- scanner 9 ---',
                      '--- scanner 12 ---', '--- scanner 19 ---', '--- scanner 30 ---', '--- scanner 39 ---',
                      '--- scanner 32 ---', '--- scanner 27 ---', '--- scanner 24 ---', '--- scanner 11 ---'}                      



            
scnrs = set()
count = 0

for k,v in global_map.items():
    if v == 'beacon':
        count += 1
    else:
        scnrs.add(k)
print('Part 1:', count)


largest_dist = 0
for s in scnrs:
    d = get_largest_dist(s)
    if d > largest_dist:
        largest_dist = d
print('Part 2:', largest_dist)
    

    



      
"""
#find_overlapping_scanners('--- scanner 11 ---')
#print_dist_to_beacon('--- scanner 39 ---', (300, 541, 493))
#match_dist(12701)    


    ================  MATCHES  ==================================
    --- scanner 39 ---           --- scanner 11 ---         Distance
    (362, 517, 402)     -        (-538, 785, -333) 	 12701
    (300, 541, 493)     -        (-629, 761, -271)

    (470, 562, 446)     -        (-582, 740, -441) 	 15625
    (362, 517, 402)     -        (-538, 785, -333)
    
    TRANSFORMATION:
    scanner 39                   scanner 11
    (-z+29, -y+1302, -x-136)    =>   (x, y, z)
    (y-1302-1091, -x-136+4964, z-29-52) = (1y-2393, -x+4828, 1z-81)


    ================  MATCHES  ==================================
    --- scanner 19 ---           --- scanner 27 ---         --- scanner 24 ---      Distance
    (-755, -742, 564)    -       (-517, 497, 664)  	    (843, -622, -519) 	 1677         
    (-723, -755, 542)    -       (-495, 529, 677)           (811, -600, -506)
 
    (-755, -742, 564)    -       (-517, 497, 664)  	    (843, -622, -519) 	 28404         
    (-887, -838, 522)    -       (-475, 365, 760)           (975, -580, -423)

    TRANSFORMATION:
    scanner 19                   scanner 27                 scanner 24
    (y-1252, -z-78, -x+47)   =>   (x, y, z)
    (y-1252+51, z+78+6081, x-47-1202) = (1y-1201, 1z+6159, 1x-1249)
    
    (-x+88, -z-1261, -y-58)                                     =>  (x,y,z)
    (-x+88+51, z+1261+6081, y+58-1202) = (-x+139, z+7342, 1y-1144)


    ================  MATCHES  ==================================
    --- scanner 12 ---           --- scanner 32 ---         --- scanner 39 ---      Distance
    (779, 438, 534)    -       (314, -528, 286)  	    (385, -567, 774) 	    20939          
    (674, 383, 617)    -       (259, -611, 391)             (330, -484, 669)

    (670, 428, 450)    -       (304, -444, 395)  	    (375, -651, 665) 	    29930          
    (674, 383, 617)    -       (259, -611, 391)             (330, -484, 669)
    
    TRANSFORMATION:
    scanner 12                   scanner 32                 scanner 39
    (-z+1065, x+124, -y+6)   =>   (x, y, z)
    (y-6+10, -z+1065+4959, -x-124+1) = (y+4, -z+6024, -x-123)
    
    (z+5, x+53, y+1101)                                     =>  (x,y,z)
    (-y-1101+10, z+5+4959, -x-53+1) = (-y-1091, 1z+4964, -x-52)


    ================  MATCHES  ==================================
    --- scanner 37 ---           --- scanner 30 ---         Distance
    (640, 354, 474)     -        (496, -678, -467) 	 3099
    (593, 373, 497)     -        (449, -655, -486)

    (640, 354, 474)     -        (496, -678, -467) 	 1104301
    (466, -682, 501)    -        (322, -651, 569) 	 
    
    TRANSFORMATION:
    scanner 37                   scanner 30
    (x+144, -z-113, y+1152)    =>   (x, y, z)
    (y+1152+30, x+144+2407, -z-113-5973) = (1y+1182, 1x+2551, -z-6086)


    ================  MATCHES  ==================================
    --- scanner 14 ---           --- scanner 12 ---         --- scanner 19 ---      Distance
    (-692, 732, -558)    -       (585, 559, -634)	    (593, 537, -644) 	    945          
    (-718, 719, -568)    -       (611, 572, -644)           (603, 511, -631)

    (-671, 818, -584)    -       (564, 473, -660)	    (619, 558, -730) 	 12266        
    (-718, 719, -568)    -       (611, 572, -644)           (603, 511, -631)
    
    TRANSFORMATION:
    scanner 14                   scanner 12                 scanner 19
    (-x-107, -y+1291, z+76)   =>   (x, y, z)
    (-z-76+86, x+107+4852, -y+1291-1290) = (-z+10, x+4959, -y+1)
    
    (y-1229, -z+88, -x+35)                              =>  (x,y,z)
    (x-35+86, -y+1229+4852, -z+88-1290) = (1x+51, -y+6081, -z-1202)


    ================  MATCHES  ==================================
    --- scanner 13 ---           --- scanner 9 ---         Distance
    (515, 496, 321)     -        (501, -500, -799) 	 7574
    (505, 453, 396)     -        (491, -575, -842)
	 
    (552, 340, 344)     -        (538, -523, -955) 	 17682
    (505, 453, 396)     -        (491, -575, -842) 	 
    
    TRANSFORMATION:
    scanner 13                   scanner 9
    (x+14, z+1295, -y-179)    =>   (x, y, z)
    (-z-1295-1133, -y-179-2226, -x-14-3620) = (-z-2428, -y-2405, -x-3634)


    ================  MATCHES  ==================================
    --- scanner 23 ---           --- scanner 37 ---         Distance
    (-534, -535, -788)     -     (593, 373, 497) 	 3099
    (-511, -582, -807)     -     (640, 354, 474)

    (-534, -535, -788)     -     (593, 373, 497) 	 29977
    (-573, -369, -818)      -    (427, 343, 536)
    
    TRANSFORMATION:
    scanner 23                   scanner 37
    (-z-37, -x+58, y-1161)    =>   (x, y, z)
    (1z+37-7, x-58+2465, y-1161-4812) = (1z+30, 1x+2407, 1y-5973)


    ================  MATCHES  ==================================
    --- scanner 34 ---           --- scanner 14 ---         Distance
    (857, 329, -541)     -       (692, 442, -808) 	 7277
    (911, 273, -506)     -       (727, 386, -862)

    (884, 492, -537)     -       (696, 605, -835) 	 49651
    (911, 273, -506)     -       (727, 386, -862)
    
    TRANSFORMATION:
    scanner 34                   scanner 14
    (-z+49, y-113, x-1233)    =>   (x, y, z)
    (-z+49+37, -x+1233+3619, 1y-113-1177) = (-z+86, -x+4852, 1y-1290)


    ================  MATCHES  ==================================
    --- scanner 22 ---           --- scanner 13 ---         --- scanner 1 ---         --- scanner 20 ---         Distance
    (-912, 442, 686)    -       (-627, -731, -913)	   (-441, -742, 293) 	      (-824, -454, -445)         6770
    (-844, 487, 697)    -       (-638, -686, -845)         (-486, -753, 361)          (-756, -443, -490)

    --- scanner 22 ---           --- scanner 13 ---         --- scanner 1 ---         --- scanner 20 ---         Distance
    (-934, 385, 605)    -       (-546, -788, -935)	   (-384, -661, 271) 	      (-846, -535, -388)         26968
    (-844, 487, 697)    -       (-638, -686, -845)         (-486, -753, 361)          (-756, -443, -490)
    
    TRANSFORMATION:
    scanner 22                   scanner 13                 scanner 1                scanner 20
    (z+1, y+1173, -x+59)   =>   (x, y, z)
    (-y-1173+40, z+1-2227, -x+59-3679) = (-y-1133,z-2226, -x-3620)
    
    (z-1205, -x+1, -y-56)                              =>  (x,y,z)
    (x-1+40, z-1205-2227, -y-56-3679) = (x+39, z-3432, -y-3735)

    (x-88, -z-3, y+1140)                                                          =>  (x,y,z)
    (z+3+40, x-88-2227, y+1140-3679) = (z+43, x-2315, y-2539)


    ================  MATCHES  ==================================
    --- scanner 28 ---           --- scanner 21 ---         Distance
    (507, -630, 712)     -       (416, -540, -623) 	    38342
    (694, -572, 709)     -       (419, -727, -565)

    (662, -753, 703)     -       (425, -695, -746) 	    33821
    (694, -572, 709)     -       (419, -727, -565)
    
    TRANSFORMATION:
    scanner 28                   scanner 21
    (-y-33, z-7, 1128-x)    =>   (x, y, z)
    (-x+1128+61, -z+7+1318, -y-33-4788)    = (-x+1189, -z+1325, -y-4821)


    ================  MATCHES  ==================================
    --- scanner 28 ---           --- scanner 3 ---         Distance
    (-740, 728, -759)    -       (-619, 628, 532) 	   9962
    (-829, 732, -714)    -       (-708, 632, 577)

    (-682, 752, -692)    -       (-561, 652, 599) 	   22493
    (-829, 732, -714)    -       (-708, 632, 577)
    
    TRANSFORMATION:
    scanner 28                   scanner 3
    (x-121, y+100, z-1291)    =>   (x, y, z)
    (z-1291+61, -y-100+1318, x-121-4788)    = (z-1230, -y+1218, x-4909)


    ================  MATCHES  ==================================
    --- scanner 29 ---           --- scanner 23 ---         --- scanner 8 ---         Distance
    (-763, 511, -428)    -       (374, -498, 388)	   (-785, 492, 873) 	      7589           
    (-795, 509, -509)    -       (372, -579, 356)          (-787, 573, 905)

    (-763, 511, -428)    -       (374, -498, 388)	   (-785, 492, 873) 	      46194           
    (-794, 723, -445)    -       (586, -515, 357)          (-573, 509, 904)
    
    TRANSFORMATION:
    scanner 29                   scanner 23                 scanner 8
    (z-1151, x+137, y+70)   =>   (x, y, z)
    (-x-137+130, -y-70+2535, z-1151-3661) = (-x-7, -y+2465, 1z-4812)
    
    (-z+110, x+1296, -y+64)                              =>  (x,y,z)
    (-x-1296+130, y-64+2535, -z+110-3661)  = (-x-1166, y+2471, -z-3551)


    ================  MATCHES  ==================================
    --- scanner 26 ---           --- scanner 34 ---         --- scanner 7 ---         Distance
    (687, -391, -675)    -       (-707, -810, 604)	   (371, 389, 735)            17298            
    (790, -311, -692)    -       (-787, -913, 621)         (291, 286, 752)

    (687, -391, -675)    -       (-707, -810, 604)	   (371, 389, 735)            9603            
    (598, -390, -716)    -       (-708, -721, 645)         (370, 478, 776)

    
    TRANSFORMATION:
    scanner 26                   scanner 34                 scanner 7
    (-y-123, -x-1098, -z-71)  => (x, y, z)
    (x+1098-1061, -z-71+3690, y+123-1300) = (x+37, -z+3619, y-1177)
    
    (-y+1076, -x-20, -z+60)                              =>  (x,y,z)
    (x+20-1061, -z+60+3690, y-1076-1300)  = (x-1041, -z+3750, y-2376)


    ================  MATCHES  ==================================
    --- scanner 36 ---           --- scanner 22 ---         Distance
    (607, 534, 479)    -        (667, -592, 651) 	    12990
    (636, 527, 589)    -        (557, -621, 644)

    --- scanner 36 ---           --- scanner 22 ---         Distance
    (614, 430, 426)    -        (720, -599, 547) 	    36462
    (636, 527, 589)    -        (557, -621, 644)
    
    TRANSFORMATION:
    scanner 36                   scanner 22
    (-y+15, z-117, -x+1146)    =>   (x, y, z)
    (-y+15+25, x-1146-1081, z-117-3562)    = (-y+40, x-2227, z-3679)


    ================  MATCHES  ==================================
    --- scanner 33 ---           --- scanner 28 ---         Distance
    (733, -484, 725)    -        (677, 676, 763)           12957
    (693, -495, 831)    -        (666, 782, 723)

    (733, -484, 725)    -        (677, 676, 763)   	   61381
    (705, -475, 971)    -        (686, 922, 735)
    
    TRANSFORMATION:
    scanner 33                   scanner 28
    (z-30, x-1161, y+49)    =>   (x, y, z)
    (z-30+91, -y-49+1367, x-1161-3627)    = (z+61, -y+1318, x-4788)


    ================  MATCHES  ==================================
    --- scanner 6 ---           --- scanner 29 ---         Distance
    (-386, -334, -442)    -      (898, -329, 562)           5548
    (-368, -352, -512)    -      (880, -311, 632)
    
    (-368, -399, -275)    -      (833, -311, 395) 	            58378
    (-368, -352, -512)    -      (880, -311, 632)
    
    TRANSFORMATION:
    scanner 6                   scanner 29
    (y-57, x-1232,-z+120)  =>   (x, y, z)
    (-y+57+73, -z+120+2415, x-1232-2429)    = (-y+130, -z+2535, x-3661)


    ================  MATCHES  ==================================
    --- scanner 31 ---           --- scanner 2 ---         Distance
    (-764, -671, -524)    -      (548, 360, 670)           16981
    (-686, -630, -428)    -      (452, 438, 629)
    
    (-706, -585, -631)    -      (655, 418, 584)           43634
    (-686, -630, -428)    -      (452, 438, 629)
    
    TRANSFORMATION:
    scanner 31                   scanner 2
    (y-1124, -z-1, -x+24)  =>   (x, y, z)
    (y-1124-1172, -z-1+1211, -x+24-2375)  = (y-2296, -z+1210, -x-2351)


    ================  MATCHES  ==================================
    --- scanner 5 ---           --- scanner 26 ---         --- scanner 18 ---         Distance
    (-434, 670, -568)    -       (373, 734, -652)	   (618, 505, 501)            18381            
    (-354, 779, -558)    -       (293, 843, -662)          (608, 396, 421)

    (-354, 779, -558)    -       (293, 843, -662)	   (608, 396, 421)            1316834            
    (775, 706, -750)     -       (-836, 770, -470)         (800, 469, -708)
    
    TRANSFORMATION:
    scanner 5                   scanner 26                 scanner 18
    (-x-61, y-64, -z-1220)   =>   (x, y, z)
    (-y+64-1125, z+1220+2470, -x-61-1239) = (-y-1061, z+3690, -x-1300)
    
    (-z+67, 1175-y, 50-x)                              =>  (x,y,z)
    (y-1175-1125, x-50+2470, -z+67-1239)                 = (y-2300, x+2420, -z-1172)


    ================  MATCHES  ==================================
    --- scanner 4 ---           --- scanner 36 ---         Distance
    (753, -440, 773)    -       (-646, 637, -698) 	 34992           
    (893, -564, 777)    -       (-650, 777, -574)

    --- scanner 4 ---           --- scanner 36 ---         Distance
    (667, -628, 779)    -       (-652, 551, -510) 	 55176           
    (893, -564, 777)    -       (-650, 777, -574)
    
    TRANSFORMATION:
    scanner 4                   scanner 36
    (y+116, -z-1138, -x+127)  =>   (x, y, z)
        (x-127+152, -z-1138+57, y+116-3678)   =   (x+25, -z-1081, y-3562)


    ================  MATCHES  ==================================
    --- scanner 10 ---           --- scanner 6 ---         --- scanner 33 ---         Distance
    (-643, -714, 688)    -       (647, -653, -391)	   (-665, 545, -657)           5386            
    (-574, -738, 695)    -       (671, -584, -384)         (-689, 614, -664)

    (-643, -714, 688)    -       (647, -653, -391) 	   (-665, 545, -657)           19694            
    (-613, -577, 683)    -       (510, -623, -396)         (-528, 575, -652)
    
    TRANSFORMATION:
    scanner 10                   scanner 6                 scanner 33
    (y+10, -x-67, z+1079)   =>   (x, y, z)
    (y-1188, x-49,-z+31)                               =>  (x,y,z)
    

    ================  MATCHES  ==================================
    --- scanner 35 ---           --- scanner 5 ---         --- scanner 31 ---         Distance
    (-514, 590, 841)     -       (-610, 785, 546) 	   (-738, 713, 526)           4907            
    (-529, 559, 780)     -       (-625, 724, 577)          (-677, 682, 511)

    (-514, 590, 841)     -       (-610, 785, 546) 	   (-738, 713, 526)           14966            
    (-569, 536, 746)     -       (-665, 690, 600)          (-643, 659, 471)


    TRANSFORMATION:
    scanner 35                   scanner 5                 scanner 31
    (1x+96, -z+1136, y+56)  =>   (x, y, z)
    (1z-1040, 1y-123, -x+103)                         =>  (x,y,z) 


    ================  MATCHES  ==================================
    --- scanner 17 ---           --- scanner 4 ---         Distance
    (-770, -862, 650)    -       (620, 701, -794) 	   34433            
    (-832, -697, 592)    -       (678, 763, -629)

    --- scanner 17 ---           --- scanner 4 ---         Distance
    (-770, -862, 650)    -       (620, 701, -794)	   15662           
    (-816, -827, 539)    -       (731, 747, -759) 
    
    TRANSFORMATION:
    scanner 17                   scanner 4
    (-y-69, z-68,-x+1270)  =>   (x, y, z)


    ================  MATCHES  ==================================
    --- scanner 17 ---           --- scanner 10 ---             Distance
    (-724, -553, -509)    -     (540, 497, -624) 	        7221            
    (-716, -512, -583)    -     (614, 456, -632)
    
    (-724, -553, -509)    -     (540, 497, -624) 	        38610            
    (-729, -357, -496)    -     (527, 301, -619) 	 
    
    TRANSFORMATION:
    scanner 17                   scanner 10
    (-z-1348, -y-56, -x+31)  =>   (x, y, z)


    ================  MATCHES  ==================================
    --- scanner 15 ---           --- scanner 35 ---             Distance
    (-818, -639, 763)    -      (802, -531, -721)                40517
    (-627, -695, 793)    -      (858, -722, -751)
    	                      
    (-657, -719, 740)    -      (882, -692, -698)                4285
    (-627, -695, 793)    -      (858, -722, -751) 

    TRANSFORMATION:
    scanner 15                   scanner 35
    (-y-1349, -x+163, -z+42)  =>   (x, y, z)


    ================  MATCHES  ==================================
    --- scanner 38 ---           --- scanner 15 ---       --- scanner 17 ---           Distance
    (-849, -604, 850)    -      (679, 828, 654)           (682, 541, -408)             28257
    (-743, -474, 839)    -      (573, 817, 784)           (576, 411, -419)


    (449, -650, 639)     -      (-619, 617, 608)          (-616, 587, -619)             1491840
    (-743, -474, 839)    -      (573, 817, 784)           (576, 411, -419)

    	                      
    TRANSFORMATION:
    scanner 38                   scanner 15
    (-x-170, z-1258, y+22)  =>   (x, y, z)

    scanner 38                   scanner 17
    (-x-167, -y-63, z+1258)  =>   (x, y, z)
"""

            

######################
# Use --- scanner 0 --- as default orientation/coordinate space
######################
"""
The closest beacon has a squared distance value of 32061
(645, -448, -766) and (584, -612, -728) are 32061 apart
Find beacons that match that distacne from other scanners
"""

"""
    Scanner 38 also has 2 beacons with the same distance apart
    (-603, 498, -384) and (-767, 437, -422) are 32061 apart

    --- scanner 0 ---
    (645, -448, -766) and (584, -612, -728) are 32061
    --- scanner 38 ---
    (-603, 498, -384) and (-767, 437, -422) are 32061
    
    Also...
    --- scanner 0 ---
    (645, -448, -766) and (479, -471, -692) 	 33561

    --- scanner 38 ---
    (-603, 498, -384) and (-626, 332, -458) 	 33561


    ================  MATCHES  ==================================
    --- scanner 0 ---           --- scanner 38 ---         Distance
    (645, -448, -766)    -      (-603, 498, -384)          32061
    (584, -612, -728)    -      (-767, 437, -422)

    (645, -448, -766)    -      (-603, 498, -384)          33561
    (479, -471, -692)    -      (-626, 332, -458)

    TRANSFORMATION:
    scanner 0                           scanner 38
    (y + 147, x + 155, -1150 - z)  =>   (x, y, z)
"""


