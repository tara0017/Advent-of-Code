#day 5


f = open('day5.txt','r')

seeds = []

seed_to_soil = dict()
soil_to_fert = dict()
fert_to_water = dict()
water_to_light = dict()
light_to_temp = dict()
temp_to_humid = dict()
humid_to_loc = dict()

current_map = None

for x in f:
    x = x.strip()
    #blank space
    if x == '':     
        continue  
    
    x = x.split()    

    match x[0]:
        case 'seeds:':          #seeds
            for i in range(1, len(x)):
                seeds.append(int(x[i]))    
        case 'seed-to-soil':
            current_map = seed_to_soil
        case 'soil-to-fertilizer':
            current_map = soil_to_fert
        case 'fertilizer-to-water':
            current_map = fert_to_water
        case 'water-to-light':
            current_map = water_to_light
        case 'light-to-temperature':
            current_map = light_to_temp
        case 'temperature-to-humidity':
            current_map = temp_to_humid
        case 'humidity-to-location':
            current_map = humid_to_loc
        case _:
            current_map[(int(x[1]), int(x[2]))] = int(x[0])  #(source, range) -> destination


def get_destination(source, convert_map):
    for k,v in convert_map.items():
        if source >= k[0] and source < k[0] + k[1]:
            value =  (source - k[0] + v)
            return value
    return source


locations = set()

for s in seeds:
    soil = get_destination(s, seed_to_soil)
    fert = get_destination(soil, soil_to_fert)
    water = get_destination(fert, fert_to_water)
    light = get_destination(water, water_to_light)
    temp = get_destination(light, light_to_temp)
    humid = get_destination(temp, temp_to_humid)
    loc = get_destination(humid, humid_to_loc)
    locations.add(loc)


print('Part 1: ', min(locations))


######### Part 2 ############
import math


# returns [[min, range], [min, range], ...] list of lists
def get_ranges(r, convert_map):
    #r                  =       [min, range]
    #convert_map        =       (source, range) -> destination

    #remove ranges that won't affect current r
    ordered_ranges = []     #list of (source, range) values whose intersection with r not None
    for k in convert_map:
        if r[0] > k[0] + k[1] - 1:  #current range is too big for this map
            continue
        if r[0] + r[1] - 1 < k[0]:  #current range is too small for this map
            continue
        ordered_ranges.append(k)

    # range is not affected by convert_map
    if len(ordered_ranges) == 0:
        return [r]
    
    #sort by min value in range
    ordered_ranges.sort()

    new_ranges = []
    for o_r in ordered_ranges:
        #r min starts below o_r minimum
        if r[0] < o_r[0]:
            #r ends within o_r range
            if r[0] + r[1] - 1 <= o_r[0] + o_r[1] - 1:
                new_ranges.append([r[0], o_r[0] - r[0]])     #add portion below range to new ranges
                new_ranges.append([convert_map[o_r], r[0] + r[1] - o_r[0]])     #add portion within o_r
                r = None
                
            #r ends after o_r range
            else:
                new_ranges.append([r[0], o_r[0] - r[0]])     #add portion below range to new ranges
                new_ranges.append(list(o_r))                 #add all of o_r range
                r = [o_r[0] + o_r[1], r[0] + r[1] - o_r[0] - o_r[1]]    #add portion above o_r
                
        #r min starts within range of o_r
        else:
            #r ends within o_r range
            if r[0] + r[1] - 1 <= o_r[0] + o_r[1] - 1:
                new_ranges.append([r[0] - o_r[0] + convert_map[o_r], r[1]])     #add entire range of r after map conversion
                r = None
                      
            #r ends after o_r range
            else:
                new_ranges.append([r[0] - o_r[0] + convert_map[o_r], o_r[0] + o_r[1] - r[0]])   #add portion within o_r
                #new_ranges.append([o_r[0] + o_r[1], r[0] + r[1] - o_r[0] - o_r[1]])             #add portion beyond o_r
                r = [o_r[0] + o_r[1], r[0] + r[1] - o_r[0] - o_r[1]]             #add portion beyond o_r

    if r != None:
        new_ranges.append(r)
    
    return new_ranges


ranges = []
#get seed range [[min, range]] list of lists
for i in range(0, len(seeds), 2):
    r = [seeds[i], seeds[i+1]]
    ranges.append(r)

min_loc = math.inf


soil = []
#for each range update to next level's range
for r in ranges:
    soil += get_ranges(r, seed_to_soil)

fert = []
for s in soil:
    fert += get_ranges(s, soil_to_fert)

water = []
for f in fert:
    water += get_ranges(f, fert_to_water)

light = []
for w in water:
    light += get_ranges(w, water_to_light)

temp = []
for l in light:
    temp += get_ranges(l, light_to_temp)

humid = []
for t in temp:
    humid += get_ranges(t, temp_to_humid)

loc = []
for h in humid:
    loc += get_ranges(h, humid_to_loc)


#get minimum from loc
for l in loc:
    min_loc = min(min_loc, l[0])

print('Part 2: ', min_loc)

