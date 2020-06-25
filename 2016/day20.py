#day20

ips = {}

f = open('day20_input.txt','r')
for x in f:
    x = x.replace('-', ' ')
    x = x.split()
    ips[int(x[0])] = int(x[1])
    #break

ips[4294967295] = 4294967299

keys = sorted(ips)

for i in range(20):
    print(keys[i], '\t',ips[keys[i]])

ip = 0
max_no_ip = 0
count = 0

for k in keys:
    #current ip is in the range of next range set
    #print("IP = ", ip, count)
    if ip >= k:
        if ips[k] > max_no_ip:
            max_no_ip = ips[k]
            ip = ips[k]+1
    else:
        count += (k - ip)
        ip = ips[k] + 1
        """
        while ip < k:
            #print('******************* ', ip)
            count += 1
            ip += 1
        ip = ips[k] + 1
        """
        print(count)
    if ip >= 4294967295:
        break

print (count)
            
        



