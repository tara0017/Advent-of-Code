#day21
def evaluate(k):
    global monkeys

    if type(monkeys[k]) is int:
        return monkeys[k]
    else: #list with operation
        if monkeys[k][1] == '+':
            return evaluate(monkeys[k][0]) + evaluate(monkeys[k][2])
        elif monkeys[k][1] == '-':
            return evaluate(monkeys[k][0]) - evaluate(monkeys[k][2])
        elif monkeys[k][1] == '*':
            return evaluate(monkeys[k][0]) * evaluate(monkeys[k][2])
        elif monkeys[k][1] == '/':
            return int(evaluate(monkeys[k][0]) / evaluate(monkeys[k][2]))
        
    
monkeys = dict()

f = open('day21.txt','r')
for x in f:
    x = x.replace(':', '')
    x = x.split()
    
    #equation
    if len(x) > 2:
        monkeys[x[0]] = x[1:]

    else: #value
        monkeys[x[0]] = int(x[1])

#part 1
print('Part 1:', evaluate('root'))


#part2
#root: brrs + fcjl
print(evaluate('fcjl')) # = 2407903937671

monkeys['humn'] = 3099532691300 
result = evaluate('brrs')

print(result)

