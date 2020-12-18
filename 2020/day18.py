# day18




def evaluate(x):
    # evaluate each parentheses
    while '(' in x:
        start_ind = x.index('(')
        end_ind   = get_closing_paran(x, start_ind)


        simplified_x = []
        y = evaluate(x[start_ind + 1: end_ind])

        simplified_x += x[:start_ind] + [y] + x[end_ind + 1:]

        return(evaluate(simplified_x))


    # no parentheses left
    # evaluate each '+'
    while '+' in x:
        ind = x.index('+')

        simplified_x = []
        y = int(x[ind-1]) + int(x[ind+1])

        simplified_x += x[:ind-1] + [str(y)] + x[ind+2:]
        return(evaluate(simplified_x))


    # only '*' left
    value = int(x[0])
    ind = 1
    while ind < len(x):
        if x[ind] == '*':
            value *= int(x[ind + 1])

        ind += 2

    return str(value)



def get_closing_paran(x, i):
    num_open   = 1
    num_closed = 0
    
    while num_open > num_closed:
        open_i  = len(x) + 1
        close_i = len(x) + 1

        # check for inner parentheses
        if '(' in x[i+1:]:
            open_i  = x.index('(', i+1)
        close_i =  x.index(')', i+1)

        if open_i < close_i:
            num_open   += 1
            i = open_i
        else:
            num_closed += 1
            i = close_i

    return close_i


        
total = 0

f = open('day18.txt', 'r')
for x in f:
    x = x.replace('(', ' ( ')
    x = x.replace(')', ' ) ')
    x = x.split()

    total += int(evaluate(x))

print(total)
