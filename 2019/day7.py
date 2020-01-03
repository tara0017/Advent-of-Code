#day7
def opcode(i, in_1, in_2):
    global data, output, is_first_input, largest_output
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
        #value = int(input("Enter an input value: "))
        if is_first_input:
            value = in_1
        else:
            value = in_2
        is_first_input = not is_first_input     #alternate True/False 
        
        index = data[i+1]
        data[index] = value
        return i+2
    elif data[i] == 4:
        index = data[i+1]
        output = data[index] ############
        if output > largest_output:
            print("The largest_output is: ", output)
            largest_output = output
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
                
            #value = int(input("Enter an input value: "))
            if is_first_input:
                value = in_1
            else:
                value = in_2
            is_first_input = not is_first_input     #alternate True/False
            
            index = data[val_1]
            data[index] = value
            return i+2
                
        elif s[-2:] == "04":
            if s[-3] == "0":
                val_1 = data[data[i+1]]
            elif s[-3] == "1":
                val_1 = i+1

            index = val_1
            output = data[index] ############
            if output > largest_output:
                print("The largest_output is: ", output)
                largest_output = output
            
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

def find_signal_strength(signal):   
    for i in range(5):
        data = original_data[:]     #reset data to original input data
        input_value = int(signal[i])    #set starting input from signal   
        
        index = 0
        while data[index] != 99:
            index = opcode(index, input_value, output)

                

f = open("day7_input.txt", "r") 

for i in f:
    original_data = i.strip().split(",")

for j in range(len(original_data)):
    original_data[j] = int(original_data[j])

#print(data)

#practice input data
#original_data = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
#original_data = [3,23,3,24,1002,24,10,24,1002,23,-1,23, 101,5,23,23,1,24,23,23,4,23,99,0,0]
#original_data = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33, 1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

data = original_data[:]

#part 1
output = 0
is_first_input = True
largest_output = 0
#signal = '10432' #'01234' #'43210'

#generate every combination of digits 0, 1, 2, 3, 4 and set it to signal
#generate_signal_seq():
for a in range(5):
    for b in range(5):
        if b == a:
            continue
        for c in range(5):
            if c == a or c == b:
                continue
            for d in range(5):
                if d == a or d == b or d == c:
                    continue
                for e in range(5):
                    if e == a or e == b or e == c or e == d:
                        continue
                    output = 0
                    signal = str(a) + str(b) + str(c) + str(d) + str(e)
                    #print(signal)
                    find_signal_strength(signal)


 
        











