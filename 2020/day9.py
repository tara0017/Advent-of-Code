# day9
def is_a_sum(i):
    global data

    pre = data[i-26:i]
    val = data[i]

    for n in pre:
        if val == 2*n:
            continue
        else:
            if (val - n) in pre:
                return True
    return False

def end_i_to_invalid(i):
    global data, invalid
    s = 0
    while s < invalid:
        s += data[i]
        if s == invalid:
            return i
        i += 1
    return -1


# read data
data = []
f = open('day9.txt','r')
for x in f:
    data.append(int(x))

# part 1
for i in range(26, len(data)):
    if not is_a_sum(i):
        print(i, data[i])
        invalid = data[i]
        break

# part 2
# invalid = 70639851

for start_i in range (len(data)):
    end_i = end_i_to_invalid(start_i)
    if  end_i > 0:
        # get min value
        m = min(data[start_i: end_i + 1])
        
        # get max value
        n = max(data[start_i: end_i + 1])        
        
        print(m, n, m + n)
        break
    
