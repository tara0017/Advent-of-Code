#day19
def opcode(i):
    global data, output, relative_base, x, y, grid_map, is_first_coord, count, in_beam
    #print("--------", "i= ", i, "RB= ", relative_base)
    if i > len(data):
        increase_data_size(i)
    #print(data)
    if data[i] == 1:
        data[data[i+3]] = data[data[i+1]] + data[data[i+2]] 
        return i+4
    elif data[i] == 2:
        data[data[i+3]] = data[data[i+1]] * data[data[i+2]] 
        return i+4
    elif data[i] == 3:
        if is_first_coord:
            value = x
            is_first_coord = False
        else:
            value = y
            is_first_coord = True
        #value = int(input("Enter an input value: "))
        index = data[i+1]
        data[index] = value
        return i+2
    elif data[i] == 4:
        index = data[i+1]
        output = data[index] ############
        grid_map.append([x, y, output])
        if output == 1:
            in_beam.append([x,y,output])
            count += 1
        return i+2
    elif data[i] == 5:
        if data[data[i+1]] == 0:
            return i+3 
        else:
            i = data[data[i+2]]
            return i
    elif data[i] == 6:
        if data[data[i+1]] == 0:
            i = data[data[i+2]]
            return i
        else:
            return i+3 
    elif data[i] == 7:
        if data[data[i+1]] < data[data[i+2]]:
            data[data[i+3]] = 1    
        else:
            data[data[i+3]] = 0
        return i+4
    elif data[i] == 8:
        if data[data[i+1]] == data[data[i+2]]:
            data[data[i+3]] = 1
        else:
            data[data[i+3]] = 0
        return i+4
    elif data[i] == 9:
        #print("IN 9", i, data[i+1], relative_base)
        relative_base += data[data[i+1]]
        #print("OUT 9", i, data[i+1], relative_base)
        return i+2

    #------------------------------------------------------------------#
    else:
        #entries of the form:   1002, 4, 3, 4, 33
        s = "000" +str(data[i])     #in case of missing leading 0's
        #if "2" in s:
        #    print (s)
        
        if s[-2:] == "01" or s[-2:] == "02":
            #values for each of the three parameters
            if s[-3] == "0":
                #ensure data length is long enough
                if data[i+1] >= len(data):
                    increase_data_size(data[i+1])
                    
                val_1 = data[data[i+1]]
            elif s[-3] == "1":
                val_1 = data[i+1]
            elif s[-3] == "2":
                val_1 = data[data[i+1] + relative_base]
            if s[-4] == "0":
                val_2 = data[data[i+2]]
            elif s[-4] == "1":
                val_2 = data[i+2]
            elif s[-4] == "2":
                val_2 = data[data[i+2] + relative_base]
            if s[-5] == "0":
                ind = data[i+3]
                #ensure data length is long enough
                if ind >= len(data):
                    increase_data_size(ind)
                #print("IND", ind, len(data))
            elif s[-5] == "2":
                ind = data[i+3] + relative_base
                #ensure data length is long enough
                if ind >= len(data):
                    increase_data_size(ind)
            
            if s[-2:] == "01":
                data[ind] = val_1 + val_2
            elif s[-2:] == "02":
                #print(val_1, val_2, ind)
                data[ind] = val_1 * val_2
            return i+4
        
        elif s[-2:] == "03":
            #values for each of the three parameters
            if s[-3] == "1":
                ind = data[i+1]
            elif s[-3] == "2":
                ind = data[i+1] + relative_base

            #value = int(input("Enter an input value: "))
            if is_first_coord == True:
                value = x
                is_first_coord = False
            else:
                value = y
                is_first_coord = True
            #ensure data length is long enough
            if ind >= len(data):
                increase_data_size(ind)

            data[ind] = value
            return i+2
                
        elif s[-2:] == "04":
            if s[-3] == "0":
                index = data[i+1]
            elif s[-3] == "1":
                index = i+1
            elif s[-3] == "2":
                index = data[i+1] + relative_base

            #ensure data length is long enough
            if index >= len(data):
                increase_data_size(index)
            output = data[index]    
            #print("The output is: ", val_1)
            point = [x, y, output]
            grid_map.append(point)
            if output == 1:
                count += 1
                in_beam.append([x,y,output])                
            return i+2
        
        elif s[-2:] == "05":
            #print("In 05 DATA @ 63 = ", data[63])
            if s[-3] == "0": #position mode for 1st parameter
                ind = data[i+1]
                #ensure data length is long enough
                if ind >= len(data):
                    increase_data_size(ind)
                    
                if data[ind] == 0: #1st param is zero - do nothing
                    return i+3 ######if it does nothing how many spots to advance?
                else:   #set pointer to value from 2nd param
                    #is 2nd parameter in position/immediate mode?
                    if s[-4] == "0": #position mode for 2nd param
                        ind = data[i+2]
                        i = data[ind]
                        return i
                    elif s[-4] == "1":   #immediate mode for 2nd param
                        i = data[i+2]
                        return i
                    elif s[-4] == "2": #relative position mode for 2nd param
                        ind = data[i+2] + relative_base
                        i = data[ind]
                        return i
            elif s[-3] == "1":   #immediate mode for 1st param
                if data[i+1] == 0:  #1st param is zero
                    return i+3
                else: #1st param is not zero
                    #set pointer to value from 2nd param
                    #is 2nd param in position or immediate mode?
                    if s[-4] == "0": #position mode for 2nd param
                        ind = data[i+2]
                        #ensure data length is long enough
                        if ind >= len(data):
                            increase_data_size(ind)
                            
                        i = data[ind]
                        return i
                    elif s[-4] == "1":   #immediate mode for 2nd param
                        i = data[i+2]
                        return i
                    elif s[-4] == "2":   #relative poition mode for 2nd param
                        #print("THE RELATIVE BASE is: ", relative_base)
                        ind = data[i+2] + relative_base
                        #print("THE ind is: ", ind, "data{ind] = ", data[ind])
                        #ensure data length is long enough
                        if ind >= len(data):
                            increase_data_size(ind)
                            
                        i = data[ind]
                        return i



            elif s[-3] == "2": #relative position mode for 1st parameter
                ind = data[i+1] + relative_base
                #ensure data length is long enough
                if ind >= len(data):
                    increase_data_size(ind)
                    
                if data[ind] == 0: #1st param is zero - do nothing
                    return i+3 ######if it does nothing how many spots to advance?
                else:   #set pointer to value from 2nd param
                    #is 2nd parameter in position/immediate mode?
                    if s[-4] == "0": #position mode for 2nd param
                        ind = data[i+2]
                        i = data[ind]
                        return i
                    elif s[-4] == "1":   #immediate mode for 2nd param
                        i = data[i+2]
                        return i
                    elif s[-4] == "2": #relative position mode for 2nd param
                        ind = data[i+2] + relative_base
                        i = data[ind]
                        return i


                    
                
        elif s[-2:] == "06":
            if s[-3] == "0": #position mode for 1st parameter
                ind = data[i+1]
                #ensure data length is long enough
                if ind >= len(data):
                    increase_data_size(ind)
                    
                if data[ind] == 0: #1st parameter is zero
                    #set pointer to value from 2nd param
                    if s[-4] == "0": #position mode for 2nd param
                        ind = data[i+2]
                        i = data[ind]
                        return i
                    elif s[-4] == "1":   #immediate mode for 2nd param
                        i = data[i+2]
                        return i
                    elif s[-4] == "2": #relative position mode for 2nd param
                        ind = data[i+2] + relative_base
                        i = data[ind]
                        return i
                else: #1st param is not zero - do nothing
                    return i+3
            elif s[-3] == "1": #immediate mode for 1st param
                if data[i+1] == 0: #1st param is zero
                    #is 2nd param in position or immediate mode
                    if s[-4] == "0": #position mode for 2nd param
                        ind = data[i+2]
                        #ensure data length is long enough
                        if ind >= len(data):
                            increase_data_size(ind)
                            
                        i = data[ind]
                        return i
                    elif s[-4] == "1":   #immediate mode for 2nd param
                        i = data[i+2]
                        return i
                    elif s[-4] == "2": #position mode for 2nd param
                        ind = data[i+2] + relative_base
                        #ensure data length is long enough
                        if ind >= len(data):
                            increase_data_size(ind)
                            
                        i = data[ind]
                        return i
                else:
                    i = i+3
                    return i

            elif s[-3] == "2": #relative position mode for 1st parameter
                ind = data[i+1] + relative_base
                #ensure data length is long enough
                if ind >= len(data):
                    increase_data_size(ind)
                    
                if data[ind] == 0: #1st parameter is zero
                    #set pointer to value from 2nd param
                    if s[-4] == "0": #position mode for 2nd param
                        ind = data[i+2]
                        i = data[ind]
                        return i
                    elif s[-4] == "1":   #immediate mode for 2nd param
                        i = data[i+2]
                        return i
                    elif s[-4] == "2": #relative position mode for 2nd param
                        ind = data[i+2] + relative_base
                        i = data[ind]
                        return i
                else: #1st param is not zero - do nothing
                    return i+3

        elif s[-2:] == "07":
            #1st param value
            if s[-3] == "0":  #position mode for 1st param
                ind = data[i+1]
                #ensure data length is long enough
                if ind >= len(data):
                    increase_data_size(ind)
                            
                param_1 = data[ind]
            elif s[-3] == "1":   #immediate mode for 1st param
                param_1 = data[i+1]
            elif s[-3] == "2":  #relative position mode for 1st param
                ind = data[i+1] + relative_base
                #ensure data length is long enough
                if ind >= len(data):
                    increase_data_size(ind)        
                param_1 = data[ind]
                #print("param_1 = ", param_1, "ind = ", ind)
            if s[-4] == "0":  #position mode for 2nd param
                ind = data[i+2]
                #ensure data length is long enough
                if ind >= len(data):
                    increase_data_size(ind)
                    
                param_2 = data[ind]
            elif s[-4] == "1":   #immediate mode for 2nd param
                param_2 = data[i+2]
            elif s[-4] == "2":  #relative position mode for 2nd param
                ind = data[i+2] + relative_base
                #ensure data length is long enough
                if ind >= len(data):
                    increase_data_size(ind)
                    
                param_2 = data[ind]
                
            if s[-5] == "0":  #position mode for 3rd param
                param_3 = data[i+3]
                #param_3 = data[ind]
            elif s[-5] == "1":   #immediate mode for 3rd param 
                param_3 = data[i+3]     #IS IT ALLOWED TO BE IN IMMEDIAT MODE?????
            elif s[-5] == "2":   #relative position mode for 3rd param 
                param_3 = data[i+3] + relative_base
                
            #ensure data length is long enough
            if param_3 >= len(data):
                increase_data_size(param_3)
                    
            if param_1 < param_2:
                data[param_3] = 1
            else:
                data[param_3] = 0
            
            return i+4

        elif s[-2:] == "08":
            #1st param value
            if s[-3] == "0":  #position mode for 1st param
                ind = data[i+1]
                #ensure data length is long enough
                if ind >= len(data):
                    increase_data_size(ind)
                #print("IN 008 - data[1000] = ", data[1000])     
                param_1 = data[ind]
            elif s[-3] == "1":   #immediate mode for 1st param
                param_1 = data[i+1]
            elif s[-3] == "2":  #relative position mode for 1st param
                ind = data[i+1] + relative_base
                #ensure data length is long enough
                if ind >= len(data):
                    increase_data_size(ind)     
                param_1 = data[ind]
                
            if s[-4] == "0":  #position mode for 2nd param
                ind = data[i+2]
                #ensure data length is long enough
                if ind >= len(data):
                    increase_data_size(ind)
                    
                param_2 = data[ind]
            elif s[-4] == "1":   #immediate mode for 2nd param
                param_2 = data[i+2]
            elif s[-4] == "2":  #relative position mode for 2nd param
                ind = data[i+2] + relative_base
                #ensure data length is long enough
                if ind >= len(data):
                    increase_data_size(ind)
                    
                param_2 = data[ind]
                
            if s[-5] == "0":  #position mode for 3rd param
                ind = data[i+3]
                #ensure data length is long enough
                if ind >= len(data):
                    increase_data_size(ind)
                    
                param_3 = ind
            elif s[-5] == "1":   #immediate mode for 3rd param
                param_3 = data[i+3]
            elif s[-5] == "2":  #relative position mode for 3rd param
                ind = data[i+3] + relative_base
                #ensure data length is long enough
                if ind >= len(data):
                    increase_data_size(ind)
                    
                param_3 = ind
                
            #ensure data length is long enough
            if param_3 >= len(data):
                increase_data_size(param_3)
                    
            if param_1 == param_2:
                data[param_3] = 1
            else:
                #ensure data length is long enough
                if param_3 >= len(data):
                    increase_data_size(param_3)
                data[param_3] = 0
            return i+4
        elif s[-2:] == "09":
            #print("@@@@@@@@@@@@@@@", i, data[i+1], relative_base)
            #is 009 a possible entry??????
            if s[-3] == "1":
                relative_base += data[i+1]
            if s[-3] == "2":
                relative_base += data[(relative_base + data[i+1])]

            #print("****************", i, data[i+1], relative_base)
            return i+2
        
                


def increase_data_size(i):
    global data
    while len(data) < i+5:
        data.append(0)

f = open("day19_input.txt", "r") 
for i in f:
    data = i.strip().split(",")
for j in range(len(data)):
    data[j] = int(data[j])


#part 1
relative_base = 0
output = 0
index = 0
grid_map = []

increase_data_size(1000)
is_first_coord = True
original_data = data[:]
in_beam = []

count = 0

#1035 - 1134:   [1035, 838, 1]  [1134, 737, 1]
#x = 1030 - 1129:   [1030, 834, 1]  [1129, 734, 1]
"""
for x in range(1020, 1138): 
    for y in range(700, 850):

        while data[index] != 99:
            index = opcode(index)
        data = original_data[:]
        index = 0
"""
x = 1018 +99       #10180726
y = 726 # +99    

while data[index] != 99:
    index = opcode(index)
            
#print(grid_map)
print(in_beam)
#print("---------------", len(in_beam))

#print(count)
 
