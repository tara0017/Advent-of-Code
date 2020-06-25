#day2
#part2
def have_one_diff(b1, b2):
    num_diff = 0
    for i in range(len(b1)):
        if b1[i] != b2[i]:
            num_diff += 1
            if num_diff > 1:
                return False
    if num_diff == 1:
        return True

def find_almost_match(box):
    for i in range(len(box)):
        box1 = box[i]
        for j in range(i+1, len(box)):
            box2 = box[j]
            if have_one_diff(box1, box2):
                return (box1, box2)


def print_similarities(match):
    a = match[0]
    b = match[1]
    answer = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            answer += a[i]
    print(answer)

    
box_ids = []
f = open("day2_input.txt", "r")
for x in f:
    box_ids.append(x)

#find matches
matches = find_almost_match(box_ids)
#print the matches minus the single difference
print_similarities(matches)

"""
#part1
def analyze_text(x):
    global num_doubles, num_triples
    d = {}
    for letter in x:
        if letter in d:     #letter has already been found
            d[letter] += 1
        else:               #first occurance of this letter
            d[letter] = 1
    #search for doubles
    if is_double_in_set(d):
        num_doubles += 1
    #search for triples
    if is_triple_in_set(d):
        num_triples += 1

def is_double_in_set(d):
    for k,v in d.items():
        if v == 2:
            return True
    return False


def is_triple_in_set(d):
    for k,v in d.items():
        if v == 3:
            return True
    return False


num_doubles = 0
num_triples = 0

f = open("day2_input.txt", "r")
for x in f:
    analyze_text(x)

print(num_doubles * num_triples)
"""
