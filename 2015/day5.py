# day5
def is_nice(x):
    """
    # part 1
    if not_vowels_and_doubles(x):
        return False
    if str_present(x):
        return False

    # passes all tests
    return True
    """

    # part 2
    if not repeated_pair(x):
        return False
    if not aba(x):
        return False

    # passes all tests
    return True

    
def repeated_pair(x):
    for i in range(len(x) - 3):
        if x[i:i+2] in x[i+2:]:
            return True        # passes test

    # fails test
    return False
        

def aba(x):
    for i in range(len(x) - 2):
        if x[i] == x[i+2]:
            return True
    return False

    
def not_vowels_and_doubles(x):
    vowels = 0
    doubles = False
    for i in range(len(x)):
        if x[i] in 'aeiou':
            vowels += 1
        if i < len(x) - 1:
            if x[i+1] == x[i]:
                doubles = True

    if doubles and vowels >= 3:     # both conditions met (passes test)
        return False

    return True     # fails test
        
    
def str_present(x):
    if 'ab' in x or 'cd' in x or 'pq' in x or 'xy' in x:
        return True     # fails test
    return False        # passes test


print(is_nice('qjhvhtzxzqqjkmpb'))
print(is_nice('xxyxx'))
print(is_nice('uurcxstgmygtbstg'))
print(is_nice('ieodomkazucvgmuy'))

count = 0
f = open('day5.txt', 'r')
for x in f:
    if is_nice(x):
        count += 1

print(count)
    


