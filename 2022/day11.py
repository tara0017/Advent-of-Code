#day11

class monkey:
    def __init__(self, name, items, operation, test, num_items_inspected = 0):
        self.name = name            # 'Monkey0'
        self.items = items          # [79, 98]
        self.operation = operation  # ['*', '19']
        self.test = test            # [23, ('2', '3')]  =>  if div by 23 go to 2 else go to 3
        self.num_items_inspected = num_items_inspected
        
    def print_detail(self):
        print(self.name)
        print(self.items)
        print(self.operation)
        print(self.test)
        print(self.num_items_inspected)
        print('----------------------------')


def complete_test(n, test):
    global monkeys

    v = test[0]
    
    if n % v == 0:
        m_num = int(test[1][0])
        monkeys[m_num].items.append(n)
    else:
        m_num = int(test[1][1])
        monkeys[m_num].items.append(n)
        
        

        
def complete_operation(n,op):
    if op[1] == 'old':
        value = n
    else:
        value = int(op[1])

    if op[0] == '+':
        value += n
    else:
        value *= n

    return (value % (17*7*13*2*19*3*5*11))



def run_one_round():
    global monkeys

    for m in monkeys:                   #for each monkey
        for i in m.items:               #for each item that monkey has
            i = complete_operation(i,m.operation) #complete operation
            #########i = int(i / 3)     #divide by 3 and round down (part 1)
            complete_test(i, m.test)    #test and assign item
            m.num_items_inspected += 1
        m.items.clear()                 #clear that monkey's items
            


def create_monkey(m):
    global monkeys

    name = m[0][0] + m[0][1]
    items = []
    for i in m[1][2:]:
        items.append(int(i))
    #operations + or * (could be + or * 'old')
    op = m[2][4:]
    check = int(m[3][3])
    options = (m[4][5], m[5][5])
    test = [check, options]
    
    mnky = monkey(name, items, op, test, 0)
    monkeys.append(mnky)
    

#gloabal variables
monkeys = []

#read data
f = open('day11.txt','r')
monkey_info = []
for x in f:
    if x == '\n':
        create_monkey(monkey_info)
        monkey_info.clear()
    else:
        x = x.strip()
        x = x.replace(':', '')
        x = x.replace(',', '')
        x = x.split()
        monkey_info.append(x)

    
num_rounds = 10000 #20 rounds for part 1
for i in range(num_rounds):
    run_one_round()

for m in monkeys:
    m.print_detail()
    

#find the 2 most active monkeys and multiply the # of items they inspected
most_active = [0,0]
for m in monkeys:
    most_active.append(m.num_items_inspected)
    most_active.remove(min(most_active))

print(most_active)
print(most_active[0] * most_active[1])





