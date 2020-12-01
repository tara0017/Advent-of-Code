# day20

def assign_factors(n):
    global factors, primes

    # initialize factor set with 1 and number
    fact = {1,n}   
    
    for p in primes:
        if n%p == 0:
            for f in factors[n / p]:
                fact.add(p * f)
                fact.add(f)
            break

    factors[n] = fact

def collect_presents(n):
    global factors

    presents = set()
    for f in factors[n]:
        if (50 * f) >= n:
            presents.add(f)

    return (11* sum(presents), presents)


num_presents   = 29000000
primes = set()

f = open('primes.txt', 'r')
for x in f:
    x = x.split()
    for n in x:
        primes.add(int(n))

          

factors = dict()    # {number: set(factors) }
for p in primes:
    f = {1, p}
    factors[p] = f

total = 0
n = 4
while True:
    if n not in factors:
        assign_factors(n)
        # part 1
        # total = sum(factors[n])

        # part 2
        total = collect_presents(n)

        """
        # part 1
        if 10 * total >= num_presents:
            print(n, total, factors[n])
            break
        """
        
        # part 2
        if total[0] >= num_presents:
            print(n, total)
            break
    n += 1





    
