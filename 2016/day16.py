#day16

a = '10001110011110000'
#a = '111100001010'

length = 35651584 #272

while len(a) < length:
    b = '0'
    for i in range(len(a)):
        if a[len(a)-1 -i] == '0':
            b += '1'
        else:
            b += '0'
    a += b
    #break

print('=============')        
#print(a)
#print('=============')
a = a[:length]

while len(a) % 2 == 0:
    c = ''
    for i in range(int(len(a) / 2)):
        if a[2*i] == a[2*i + 1]:
            c += '1'
        else:
            c += '0'
    a = c

print(a)





