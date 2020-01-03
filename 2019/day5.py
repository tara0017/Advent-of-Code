#day5
def opcode(i):
    global data
    #print("--------", data[i])
    if data[i] == 99:
        return 99
    elif data[i] == 1:
        data[data[i+3]] = data[data[i+1]] + data[data[i+2]] 
        return i+4
    elif data[i] == 2:
        data[data[i+3]] = data[data[i+1]] * data[data[i+2]] 
        return i+4
    elif data[i] == 3:
        value = int(input("Enter an input value: "))
        index = data[i+1]
        data[index] = value
        return i+2
    elif data[i] == 4:
        index = data[i+1]
        print("The output is: ", data[index])
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
            return i+4
        else:
            data[data[i+3]] = 0
            return i+4
    elif data[i] == 8:
        if data[data[i+1]] == data[data[i+2]]:
            data[data[i+3]] = 1
            return i+4
        else:
            data[data[i+3]] = 0
            return i+4

    #------------------------------------------------------------------#
    else:
        #entries of the form:   1002, 4, 3, 4, 33
        s = "000" +str(data[i])     #in case of missing leading 0's

        if s[-2:] == "01" or s[-2:] == "02":
            #values for each of the three parameters
            if s[-3] == "0":
                val_1 = data[data[i+1]]
            elif s[-3] == "1":
                val_1 = data[i+1]
            if s[-4] == "0":
                val_2 = data[data[i+2]]
            elif s[-4] == "1":
                val_2 = data[i+2]
            if s[-5] == "0":
                ind = data[i+3]
            
            if s[-2:] == "01":
                data[ind] = val_1 + val_2
            elif s[-2:] == "02":
                data[ind] = val_1 * val_2
            return i+4
        
        elif s[-2:] == "03":
            #values for each of the three parameters
            if s[-3] == "0":
                val_1 = data[data[i+1]]
            elif s[-3] == "1":
                val_1 = data[i+1]
                
            value = int(input("Enter an input value: "))
            index = data[val_1]
            data[index] = value
            return i+2
                
        elif s[-2:] == "04":
            if s[-3] == "0":
                val_1 = data[data[i+1]]
            elif s[-3] == "1":
                val_1 = i+1

            index = val_1
            print("The output is: ", data[index])
            return i+2
        
        elif s[-2:] == "05":
            if s[-3] == "0": #position mode for 1st parameter
                ind = data[i+1]
                if data[ind] == 0: #1st param is zero - do nothing
                    return i+3 ######if it does nothing how many spots to advance?
                else:   #set pointer to value from 2nd param
                    #is 2nd parameter in position/immediate mode?
                    if s[-4] == "0": #position mode for 2nd param
                        ind = data[i+2]
                        i = data[ind]
                        return i
                    else:   #immediate mode for 2nd param
                        i = data[i+2]
                        return i
            else:   #immediate mode for 1st param
                if data[i+1] == 0:  #1st param is zero
                    return i+3
                else: #1st param is not zero
                    #set pointer to value from 2nd param
                    #is 2nd param in position or immediate mode?
                    if s[-4] == "0": #position mode for 2nd param
                        ind = data[i+2]
                        i = data[ind]
                        return i
                    else:   #immediate mode for 2nd param
                        i = data[i+2]
                        return i
                
        elif s[-2:] == "06":
            if s[-3] == "0": #position mode for 1st parameter
                ind = data[i+1]
                if data[ind] == 0: #1st parameter is zero
                    #set pointer to value from 2nd param
                    if s[-4] == "0": #position mode for 2nd param
                        ind = data[i+2]
                        i = data[ind]
                        return i
                    else:   #immediate mode for 2nd param
                        i = data[i+2]
                        return i
                else: #1st param is not zero - do nothing
                    return i+3
            else: #immediate mode for 1st param
                if data[i+1] == 0: #1st param is zero
                    #is 2nd param in position or immediate mode
                    if s[-4] == "0": #position mode for 2nd param
                        ind = data[i+2]
                        i = data[ind]
                        return i
                    else:   #immediate mode for 2nd param
                        i = data[i+2]
                        return i
                else:
                    i = i+3
                    return i

        elif s[-2:] == "07":
            #1st param value
            if s[-3] == "0":  #position mode for 1st param
                ind = data[i+1]
                param_1 = data[ind]
            else:   #immediate mode for 1st param
                param_1 = data[i+1]
            if s[-4] == "0":  #position mode for 2nd param
                ind = data[i+2]
                param_2 = data[ind]
            else:   #immediate mode for 2nd param
                param_2 = data[i+2]
            if s[-5] == "0":  #position mode for 3rd param
                param_3 = data[i+3]
                #param_3 = data[ind]
            else:   #immediate mode for 3rd param 
                param_3 = data[i+3]     #IS IT ALLOWED TO BE IN IMMEDIAT MODE?????

            if param_1 < param_2:
                data[param_3] = 1
                return i+4
            else:
                data[param_3] = 0
                return i+4

        elif s[-2:] == "08":
            #1st param value
            if s[-3] == "0":  #position mode for 1st param
                ind = data[i+1]
                param_1 = data[ind]
            else:   #immediate mode for 1st param
                param_1 = data[i+1]
            if s[-4] == "0":  #position mode for 2nd param
                ind = data[i+2]
                param_2 = data[ind]
            else:   #immediate mode for 2nd param
                param_2 = data[i+2]
            if s[-5] == "0":  #position mode for 3rd param
                ind = data[i+3]
                param_3 = ind
            else:   #immediate mode for 3rd param
                param_3 = data[i+3]

            if param_1 == param_2:
                data[param_3] = 1
                return i+4
            else:
                data[param_3] = 0
                return i+4

                

f = open("day5_input.txt", "r") 

for i in f:
    data = i.strip().split(",")

for j in range(len(data)):
    data[j] = int(data[j])

#print(data)

#practice input data
#data = [1002,4,3,4,33]
#data = [3,9,8,9,10,9,4,9,99,-1,8]
#data = [3,9,7,9,10,9,4,9,99,-1,8]
#data = [3,3,1108,-1,8,3,4,3,99]
#data = [3,3,1107,-1,8,3,4,3,99]
#data = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
#data = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
#data = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]


#part 1
index = 0
while data[index] != 99:
    index = opcode(index)
#print (data)
 
        











