# day1

f = open('day1.txt', 'r')

increasing = -1     # do not count 1st value
last_value = 0

increasing_window = 0   # conditional in loop ensures 1st window isn't counted
window = []

for x in f:
    x = int(x)
    
    # part 1
    if x > last_value:
        increasing += 1
    last_value = x

    # part 2
    # make sure initial window has 3 values
    if len(window) < 3:
        window.append(x)
    else:   # window has 3 values
        if x > window[0]:
            increasing_window += 1
            
        # remove oldest value from window and add x at end as newest value
        window[0] = window[1]
        window[1] = window[2]
        window[2] = x

    
print(increasing)
print(increasing_window)
