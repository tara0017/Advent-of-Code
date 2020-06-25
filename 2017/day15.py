#day15
a = 783
b = 325

#practice
#a = 65
#b = 8921

a_factor = 16807
b_factor = 48271
count = 0
a_values = []
b_values = []

while min(len(a_values), len(b_values)) < 5*(10**6):
    a = (a*a_factor) % 2147483647
    b = (b*b_factor) % 2147483647

    if a % 4 == 0:
        a_values.append(a)
    if b % 8 == 0:
        b_values.append(b)
        
for i in range(5*(10**6)):
    a = a_values[i]
    b = b_values[i]
    
    bin_a = bin(a)
    bin_b = bin(b)
    
    if len(str(bin_a)) > len(bin(2**15)):
        bin_a = str(bin_a)[-16:]
    else:
        bin_a = str(bin_a)
        bin_a = bin_a.replace('0b', '00000000000000000000')
        bin_a = bin_a[-16:]
        
    if len(str(bin_b)) > len(bin(2**15)):
        bin_b = str(bin_b)[-16:]
    else:
        bin_b = str(bin_b)
        bin_b = bin_b.replace('0b', '00000000000000000000')
        bin_b = bin_b[-16:]
    
    if bin_a == bin_b:
        count += 1

print(count)
