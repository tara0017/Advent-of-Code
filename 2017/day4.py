#day4
def split(word):
    return [char for char in word]
    
def contains_duplicates(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return True
    return False    

count = 0

f= open("day4_input.txt", "r")
for x in f:
    x = x.split()
    for i in range(len(x)):
        x[i] = sorted(split(x[i]))
        
        
    if not contains_duplicates(x):
        count += 1

print(count)

