#day22
def new_stack():
    global deck
    deck.reverse()

def cut(n):
    global deck
    deck = deck[n:] + deck[:n]

def increment(n):
    global deck
    new_deck = [0]* len(deck)
    for i in range(len(deck)):
        new_deck[i*n % len(deck)] = deck[i]
    deck = new_deck[:]
        

deck_size = 10007
deck = []
for i in range(deck_size):
    deck.append(i)


f = open("day22_input.txt", "r")
for x in f:
    #print(x)
    s = x.split()
    if s[-2] == 'new':
        new_stack()
    if s[-2] == 'increment':
        increment(int(s[-1]))
    if s[-2] == 'cut':
        cut(int(s[-1]))



print (deck.index(9492))
