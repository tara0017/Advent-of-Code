# day 16
class packet:
    def __init__(self, version, type_id, starting_index, literal_value = 0, sub_packets = set()):
        self.version = version
        self.type_id = type_id
        self.starting_index = starting_index
        self.literal_value = literal_value
        self.sub_packets   = sub_packets

    def print_packet(self):
        print('ver:', self.version, 'type:', self.type_id, 'starting_index:', self.starting_index, 'value:', self.literal_value, 'num subpacks:', len(self.sub_packets))
    
    def get_value(self):
        if self.type_id == 4:
            return self.literal_value
        elif self.type_id == 0:
            return self.sum_sub_packets(self.sub_packets)
        elif self.type_id == 1:
            return self.product_sub_packets(self.sub_packets)
        elif self.type_id == 2:
            return self.min_sub_packets(self.sub_packets)
        elif self.type_id == 3:
            return self.max_sub_packets(self.sub_packets)
        elif self.type_id == 5:
            return self.greater_than_sub_packets(self.sub_packets)
        elif self.type_id == 6:
            return self.less_than_sub_packets(self.sub_packets)
        elif self.type_id == 7:
            return self.equal_to_sub_packets(self.sub_packets)


    def equal_to_sub_packets(self, subs):
        packs = []
        for p in subs:
            packs.append(p)
            
        if packs[0].get_value() == packs[1].get_value():
            return 1
        else:
            return 0


    def less_than_sub_packets(self, subs):
        packs = []
        for p in subs:
            packs.append(p)

        if packs[0].starting_index > packs[1].starting_index:
            packs[0],packs[1] = packs[1],packs[0]
            
        if packs[0].get_value() < packs[1].get_value():
            return 1
        else:
            return 0

        
    def greater_than_sub_packets(self, subs):
        packs = []
        for p in subs:
            packs.append(p)

        if packs[0].starting_index > packs[1].starting_index:
            packs[0],packs[1] = packs[1],packs[0]
            
        if packs[0].get_value() > packs[1].get_value():
            return 1
        else:
            return 0

    
    def max_sub_packets(self, subs):
        highest = float('-inf')
        for p in subs:
            v = p.get_value()
            if v > highest:
                highest = v
        return highest

    
    def min_sub_packets(self, subs):
        lowest = float('inf')
        for p in subs:
            v = p.get_value()
            if v < lowest:
                lowest = v
        return lowest

    
    def product_sub_packets(self, subs):
        total = 1
        for p in subs:
            total *= p.get_value()
        return total
    
    def sum_sub_packets(self, subs):
        total = 0
        for p in subs:
            total += p.get_value()
        return total
        


        
def convert_to_bin(s):
    d = dict()
    d['0'] = '0000'
    d['1'] = '0001'
    d['2'] = '0010'
    d['3'] = '0011'
    d['4'] = '0100'
    d['5'] = '0101'
    d['6'] = '0110'
    d['7'] = '0111'
    d['8'] = '1000'
    d['9'] = '1001'
    d['A'] = '1010'
    d['B'] = '1011'
    d['C'] = '1100'
    d['D'] = '1101'
    d['E'] = '1110'
    d['F'] = '1111'

    b = ''
    for c in s:
        b += d[c]
    return b
        

    
def get_packet(current_index):
    global g_pack, total_version_values, packets

    start_ind = current_index
    ver = g_pack[current_index : current_index + 3]
    ver = int('0b' + ver, 2)
    total_version_values += ver     # part 1 
    ty_id = g_pack[current_index + 3 : current_index + 6]
    ty_id = int('0b' + ty_id, 2)

    # current_index increased by 6
    current_index += 6


    if ty_id == 4:  # literal value
        v = get_literal_value(current_index) #returns value and amount to increase index
        current_index = v[0]
        new_p = packet(ver, ty_id, start_ind, v[1])
        packets.add(new_p)
        return [current_index, new_p]
    
    
    else:           # operator
        length_type_id = g_pack[current_index]
        current_index += 1
        if length_type_id == '0':     # next 15 bits = total length
            sub_packet_length = g_pack[current_index : current_index + 15]
            sub_packet_length = int('0b' + sub_packet_length, 2)
            current_index += 15

            sub_packs = get_indefinite_packets(sub_packet_length, current_index)

            #create new packet/s
            new_p = packet(ver, ty_id, start_ind, 0, sub_packs[1])
            packets.add(new_p)

            #update index after all subpacks found            
            current_index = sub_packs[0]
            
            return [current_index, new_p]

        elif length_type_id == '1':   # next 11 bits = number of sub packets
            num_sub_packets = g_pack[current_index : current_index + 11]
            num_sub_packets = int('0b' + num_sub_packets, 2)
            current_index += 11

            sub_packs = get_multiple_subpackets(num_sub_packets, current_index)

            #create new packet
            new_p = packet(ver, ty_id, start_ind, 0, sub_packs[1])
            packets.add(new_p)

            #update index after all subpacks found
            current_index = sub_packs[0]
            
            return [current_index, new_p]


            
# returns [new index, set of sub packets]
def get_indefinite_packets(length, ind):
    sub_packs = set()
    ending_index = ind + length

    while ending_index - ind > 6: # not just trailing zeros left
        p = get_packet(ind)
        sub_packs.add(p[1])
        ind = p[0]

    ind = ending_index  # account for potential trailing zeros
    return [ind, sub_packs]


# returns [new index, set of sub packets]
def get_multiple_subpackets(num_packets, ind):
    sub_packs = set()
    
    for i in range(num_packets):
        p = get_packet(ind)
        sub_packs.add(p[1])
        ind = p[0]
             
    return [ind, sub_packs]




#return [new index, the literal value for type ID 4]
def get_literal_value(ind):
    global g_pack
    value = '0b'
    # continue looking at next 5 bits until one starts with a zero
    while True:
        five_bit = g_pack[ind : ind + 5]
        value += five_bit[1:]
        ind += 5
        if five_bit[0] == '0':
            break
        
    value = int(value, 2)   # convert value to decimal
    return [ind, value] 



# convert to binary
f = open('day16.txt','r')
for x in f:
    s = x.strip()
g_pack = convert_to_bin(s)

# global variables
current_index = 0
total_version_values = 0
packets = set()

# part 1
get_packet(current_index)
print('TOTAL VERSION VALUES:', total_version_values)

# part 2
for p in packets:
    if p.starting_index == 0:
        print('Packet value:', p.get_value())
        break


