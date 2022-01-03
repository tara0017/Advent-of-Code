# day 20
def convert_to_dict():
    global image, image_length, image_height

    image_length = len(image[0])
    image_height = len(image)

    d = dict()
    
    for y in range(len(image)):
        for x in range(len(image[0])):
            if image[y][x] == '.':
                d[(y,x)] = 0
            else:
                d[(y,x)] = 1
    return d


def get_bin_value(y,x, itteration):
    global image
    bin_num = '0b'
    
    for j in range(y-1, y+2):
        for i in range(x-1, x+2):
            if (j,i) not in image:
                """
                ###################
                # for test case
                bin_num += str(0)
                ###################
                """

                ###################
                # for actual input
                if itteration % 2 == 0:
                    bin_num += str(0)
                else:
                    bin_num += str(1)
                ###################
            else:
                bin_num += str(image[(j,i)])
    return int(bin_num, 2)


def get_pixel(v):
    global iea
    if iea[v] == '#':
        return 1
    else:
        return 0
    

# global variables
iea   = ''
image = []
image_length = 0
image_height = 0


# read input 
is_image = False
f= open('day20.txt', 'r')
for x in f:
    if x == '\n':
        continue
    x = x.strip()
    if is_image == True:
        image.append(x)
    else:
        iea = x
        is_image = True

image = convert_to_dict()


min_coord = 0
repetitions = 50
count = 0

for i in range(repetitions):
    enhanced_image = dict()
    for y in range(min_coord - 1, image_height + 1):
        for x in range(min_coord - 1, image_length + 1):
            v = get_bin_value(y,x, i)
            pixel = get_pixel(v)
            enhanced_image[(y,x)] = pixel

            # count lit pixels on final repetition
            if (i == repetitions - 1) and (pixel == 1):
                count += 1

    # expand image search area
    min_coord    -= 1
    image_height += 1
    image_length += 1

    # update image
    image = enhanced_image
    

print(count)
            

            
            
    

