import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw    
import numpy as np        

logo = PIL.Image.open('test_image.jpg')
def frame_image(original_image, wide = 50):
    width, height = original_image.size
    frame_width = width + 2*wide
    frame_height = height + 2*wide 
    frame_mask = PIL.Image.new('RGBA', (frame_width, frame_height))
    image = np.array(frame_mask)
    for frame_width in range(frame_width):
        for frame_heigth in range(frame_height):
            if (frame_width+frame_height)/5 % 2 == 0: 
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                image[frame_width][frame_height] = [127, 255, 127, 255] # pale red, alpha=0
            elif (frame_width-frame_height)/5 %2 ==0:
                image[frame_width][frame_height] = [15, 255, 255, 255]
            else:
                # Odd stripe
                image[frame_width][frame_height] = [0, 255, 255, 0] # magenta, alpha=255
    frame_mask.paste(original_image, ((frame_width-width)/2,(frame_height-height)/2))
    return frame_mask 

def logo_place(image, side):
    image_width, image_height = image.size
    logo.resize((int(image_width * .125), int(image_height *.125)))
    border_spacing = 0.1
    if side == 'upper right' or 'upper left':
        logo_y = (image_height - (image_height * border_spacing))
        if side == 'upper right':
            logo_x = (image_width - (image_width * border_spacing))
        else:
            logo_x = image_width * border_spacing
    else:
        logo_y = image_height * border_spacing
        if side == 'lower right':
            logo_x = (image_width - (image_width * border_spacing))
        else:
            logo_x = image_width * border_spacing
    image.paste(logo, (int(logo_x), int(logo_y)))
    return image 
    
def get_images(directory=None):
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
    image_list=[] 
    file_list = []
    directory_list = os.listdir(directory) 
    for entry in directory_list:
         absolute_filename = os.path.join(directory, entry)
         try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
         except IOError:
             pass 
    return image_list, file_list
        

def set_logo(side, directory=None):
    if directory == None:
        directory = os.getcwd() 
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed 
    image_list, file_list = get_images(directory) 
    for n in range(len(image_list)):
        filename, filetype = os.path.splitext(file_list[n])
        new_image = logo_place(image_list[n], side)
        final_image = frame_image(new_image)
        final_image_filename = os.path.join(new_directory,filename + '.png')
        final_image.save(final_image_filename)
        
def test():
    directory = os.getcwd()
    set_logo('left')
    image_directory = os.path.join(directory, 'modified')
    if os.path.exists(os.path.join(directory, 'modified')) == True:
        print 'Directory exists, No images created'
        image_directory = os.path.join(directory, 'modified')
    elif os.path.exists(os.path.join(image_directory, 'test_image.png')) == True:
        print 'Image created, Test Passed'
    else:
        print 'Test Failed'
    try:
        os.remove(image_directory)
    except OSError:
        pass
         