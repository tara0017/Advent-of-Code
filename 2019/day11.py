#day9
def opcode(i):
    global data, output, relative_base, color_output, turn_output, color_grid, output_number
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

        #program will ask for an input representing what color robot is on
        value = get_color()

        index = data[i+1]
        data[index] = value
        return i+2
    elif data[i] == 4:
        index = data[i+1]
        output = data[index] 

        
        #handle 2 outputs, 1st is color to paint, 2nd is direction to turn
        if output_number == 1:  #1st output - color indicator
            #print("IN 4", location)
            color_output = output
            paint_square(color_output)
            output_number = 2   #switch to direction indicator
        elif output_number == 2:  #2nd output - direction indicator
            turn_output = output
            move(turn_output)
            output_number = 1   #switch back to color indicator
            #print("out_1 = ", color_output, "out_2 = ", turn_output)

            
        #print("The output is: ", output)
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
                #print("203 val_1 = ", ind)
                """
                ind = data[i+1] + relative_base
                #ensure data length is long enough
                if ind >= len(data):
                    increase_data_size(ind)

                val_1 = data[ind]
                """
            #value = int(input("Enter an input value: "))
            #program will ask for an input representing what color robot is on
            value = get_color()
        
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


            #handle 2 outputs, 1st is color to paint, 2nd is direction to turn
            if output_number == 1:  #1st output - color indicator
                color_output = output
                paint_square(color_output)
                output_number = 2   #switch to direction indicator
            elif output_number == 2:  #2nd output - direction indicator
                turn_output = output
                move(turn_output)
                output_number = 1   #switch back to color indicator
                #print("out_1 = ", color_output, "out_2 = ", turn_output)


            #print("The output is: ", output)
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
        
                

def get_color():
    global color_grid, location
    #check if location has been created yet
    #if it was created, return color
    if location in color_grid:
        if color_grid[location][0] == "black":
            return 0
        else:
            return 1
    #if it was not created, create a new one colored black and return color
    else:
        color_grid[location] = ("black", False)
        return 0
        

def increase_data_size(i):
    global data
    while len(data) < i+5:
        data.append(0)

f = open("day11_input.txt", "r") 
for i in f:
    data = i.strip().split(",")

for j in range(len(data)):
    data[j] = int(data[j])



def paint_square(color):
    global color_grid, location, num_painted_squares 
    #incriment count if it has not been painted already
    if color_grid[location][1] == False:
        #print("HERE")
        num_painted_squares += 1
        color_location()
    #paint square
    if color == 0:
        set_color("black")
    else:
        set_color("white")

def color_location():
    global color_grid, location
    t_list = list(color_grid[location])
    t_list[1] = True
    color_grid[location] = tuple(t_list)
    
def set_color(c):
    global color_grid, location
    t_list = list(color_grid[location])
    t_list[0] = c
    color_grid[location] = tuple(t_list)
    

def change_coord(x, y):
    global location, color_grid
    #print("X=", x, "    y= ", y)
    t_list = list(location)
    t_list[0] += x
    t_list[1] += y
    #print("x=", x, "y= ", y, location)
    location = tuple(t_list)
    if location not in color_grid:
        color_grid[location] = ("black", False)
    #print(t_list, location)
    

def move(turn_direction):
    global color_grid, location, facing
    if facing == "up":
        #print("UP", turn_direction)
        if turn_direction == 0:     #turn left
            #print("&&&&&&&&", location)
            change_coord(-1, 0)
            #print(location)
            facing = "left"
        elif turn_direction == 1:     #turn right
            change_coord(1, 0)
            facing = "right"
    elif facing == "down":
        #print("DOWN", turn_direction)
        if turn_direction == 0:     #turn left
            change_coord(1, 0)
            facing = "right"
        elif turn_direction == 1:     #turn right
            change_coord(-1, 0)
            facing = "left"
    elif facing == "right":
        #print("RIGHT", turn_direction)
        if turn_direction == 0:     #turn left
            change_coord(0, 1)
            facing = "up"
        elif turn_direction == 1:     #turn right
            change_coord(0, -1)
            facing = "down"            
    elif facing == "left":
        #print("LEFT", turn_direction)
        if turn_direction == 0:     #turn left
            change_coord(0, -1)
            facing = "down"
        elif turn_direction == 1:     #turn right
            change_coord(0, 1)
            facing = "up"
    


            

#practice input data
#data = 


#part 1
relative_base = 0
output = 0
output_number = 1
color_output = 0
turn_output = 0
#color_grid     coordinate point    :   (current color,     has it been colored)
#               (x, y)              :   ("black"/"white",   True/False
color_grid = {}
color_grid[(0,0)] = ("white", False)
location = (0,0)
num_painted_squares = 0
index = 0
facing = "up"

#print(len(data))
increase_data_size(2000)

while data[index] != 99:
    #print(location, num_painted_squares)
    #print(color_grid)
    #print("--------------------")
    index = opcode(index)

print("painted squares", num_painted_squares)
print(color_grid)


#draw result
import turtle
turtle.penup()
turtle.speed(0)

def draw_rect(x, y):
    turtle.setpos(x, y)
    turtle.color("green")
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(10)
        turtle.right(90)
    turtle.end_fill()
    

for point in color_grid:
    if color_grid[point][0] == "white":
        draw_rect(10*point[0], 10*point[1])
    
    




    
