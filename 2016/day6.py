#day6
def seperate_letters(s):
    global letter_distribution
    s = s.strip()
    #print(len(s))
    for i in range(len(s)):
        letter = s[i]
        if letter in letter_distribution[i]:
            letter_distribution[i][letter] += 1
        else:
            letter_distribution[i][letter] = 1

def find_most_common(d):
    m = max(d, key=d.get)
    return m

def find_least_common(d):
    m = min(d, key=d.get)
    return m

first = {}
second = {}
third = {}
fourth = {}
fifth = {}
sixth = {}

letter_distribution = [{},{},{},{},{},{},{},{}]

f = open('day6_input.txt','r')
for x in f:
    seperate_letters(x)
    #break

print(letter_distribution)

for i in range(len(letter_distribution)):
    print(find_most_common(letter_distribution[i]), end = '')
print()    
for i in range(len(letter_distribution)):
    print(find_least_common(letter_distribution[i]), end = '')

        
    
