#day15
def opcode(i):
    global data, output, relative_base, direction_to_move
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
        #value = int(input("Enter an input value: "))
        value = random.randrange(1,5,1)
        direction_to_move = value
        index = data[i+1]
        data[index] = value
        return i+2
    elif data[i] == 4:
        index = data[i+1]
        output = data[index] ############
        update_map(output)
        ###############print("The output is: ", output)
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
            value = random.randrange(1,5,1)            
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
            val_1 = data[index]    
            ##########print("The output is: ", val_1)
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

def update_map(output):
    global location, direction_to_move, droid_map, map_length
    #direction_to_move:     1=North, 2=South, 3=West, 4=East
    #output:                0=wall (don't move), 1=move, 2=found oxygen
    if output == 0:
        #update droid_map - place a wall in the direction of motion
        #do not change location
        if direction_to_move == 1: #NORTH
            new_location = [location[0], location[1]+1, output]
            if new_location not in droid_map:
                droid_map.append(new_location)
        elif direction_to_move == 2: #SOUTH
            new_location = [location[0], location[1]-1, output]
            if new_location not in droid_map:
                droid_map.append(new_location)
        elif direction_to_move == 3: #WEST
            new_location = [location[0]-1, location[1], output]
            if new_location not in droid_map:
                droid_map.append(new_location)
        elif direction_to_move == 4: #EAST
            new_location = [location[0]+1, location[1], output]
            if new_location not in droid_map:
                droid_map.append(new_location)
               
    elif output == 1:
        #update location
        #update droid_map
        if direction_to_move == 1: #NORTH
            new_location = [location[0], location[1]+1, output]
            location = (new_location[0], new_location[1])
            if new_location not in droid_map:
                droid_map.append(new_location)
        elif direction_to_move == 2: #SOUTH
            new_location = [location[0], location[1]-1, output]
            location = (new_location[0], new_location[1])
            if new_location not in droid_map:
                droid_map.append(new_location)
        elif direction_to_move == 3: #WEST
            new_location = [location[0]-1, location[1], output]
            location = (new_location[0], new_location[1])
            if new_location not in droid_map:
                droid_map.append(new_location)
        elif direction_to_move == 4: #EAST
            new_location = [location[0]+1, location[1], output]
            location = (new_location[0], new_location[1])
            if new_location not in droid_map:
                droid_map.append(new_location)

    elif output == 2:
        #update location
        #update droid map
        #print location of oxygen
        #print shortest distance
        if direction_to_move == 1: #NORTH
            new_location = [location[0], location[1]+1, output]
            location = (new_location[0], new_location[1])
            if new_location not in droid_map:
                droid_map.append(new_location)
        elif direction_to_move == 2: #SOUTH
            new_location = [location[0], location[1]-1, output]
            location = (new_location[0], new_location[1])
            if new_location not in droid_map:
                droid_map.append(new_location)
        elif direction_to_move == 3: #WEST
            new_location = [location[0]-1, location[1], output]
            location = (new_location[0], new_location[1])
            if new_location not in droid_map:
                droid_map.append(new_location)
        elif direction_to_move == 4: #EAST
            new_location = [location[0]+1, location[1], output]
            location = (new_location[0], new_location[1])
            if new_location not in droid_map:
                droid_map.append(new_location)
        #print("OXYGEN FOUND!!!! It was hiding at ", location)
        print(droid_map)

    if len(droid_map) != map_length:    #map was updated w new point
        map_length = len(droid_map)
        draw_new_square(droid_map[-1])
        
    #print("--------------------------------")
    #print(droid_map)


def draw_new_square(coordinate):
    x = 10*coordinate[0]
    y = 10*coordinate[1]
    point_id = coordinate[2]
    turtle.setpos(x,y)
    if point_id == 0:   #wall
        turtle.color("black")
    elif point_id == 1: #open
        turtle.color("yellow")
    else:               #oxygen
        turtle.color("blue")
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(10)
        turtle.left(90)
    turtle.end_fill()
    

    
f = open("day15_input.txt", "r") 
for i in f:
    data = i.strip().split(",")
for j in range(len(data)):
    data[j] = int(data[j])

import turtle, random
turtle.penup()
turtle.speed(0)

turtle.color("green")
turtle.begin_fill()
for i in range(4):
    turtle.fd(10)
    turtle.left(90)
turtle.end_fill()

    
#part 1
relative_base = 0
output = 0
index = 0
droid_map = []  #[x, y, location_id]
droid_map.append([0,0,1])
location = (0,0)
direction_to_move = 0
map_length = 1

increase_data_size(1000)

while data[index] != 99:
    index = opcode(index)


 
