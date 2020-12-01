# day1
import itertools

values = []

f = open('day1.txt','r')
for x in f:
    values.append(int(x))

# part 2
lst = itertools.combinations(values, 3)
for x in list(lst):
    if sum(x) == 2020:
        print(x, x[0] * x[1] * x[2])
        
# part 1
lst = itertools.combinations(values, 2)
for x in list(lst):
    if sum(x) == 2020:
        print(x, x[0] * x[1])

