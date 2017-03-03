import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw            

def get_images(directory=None):
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
    # create 2 new lists for images and files
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
        new_image_filename = os.path.join(new_directory,filename + '.png')
        new_image.save(new_image_filename)
        
def test():
    ''' 
    Will test the program in order to see if using proper directories and
    image control. If test passes: directory has been created and image has been
    saved as a .png
    '''
    for a in range(1):
        directory = os.getcwd()
        #set_logo('left')
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
         
def logo_place(image, side): #Places the logo onto specified corner of an image
    ''' 
    This function will place a predetermined logo in a specified corner of the image, or in the middle.
    Use middle or upper/lower then left/right to set location of logo on the image.
    ''' 
    image_width, image_height = image.size
    logo.resize(image_width * .125, image_height *.125)
    border_spacing = 0.1
    if side == 'upper right' or 'upper left': # check to see where user wants logo
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
    # paste image according to conditions inputed by user and computed by program
    image.paste(logo, (logo_x, logo_y))
    return image 
