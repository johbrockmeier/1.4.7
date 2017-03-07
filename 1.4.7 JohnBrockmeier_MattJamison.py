import PIL
import os.path  
import PIL.ImageDraw 
import matplotlib.pyplot as plt      

logo_raw = PIL.Image.open('MartianPicture.jpg')
logo_large = PIL.Image.new('RGBA', logo_raw.size, (0,0,0,0))
def round_logo():
    """ 
    creates a rounded logo
    """
    width, height = logo_raw.size
    radius = int(min(width/2, height/2)) 
    round_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(round_mask)
    drawing_layer.ellipse((width/2-radius,0,radius+width/2, 2*radius), 
                          fill=(0,127,127,255)) 
    #plt.imshow(round_mask)
    logo_large.paste(logo_raw, (0,0), mask=round_mask)
    #return logo_large
    
def frame_image(image, wide = 50):

    width, height = image.size
    frame_width = width + 2*wide
    frame_height = height + 2*wide 
    frame_large = PIL.Image.open('background.jpg')
    frame_mask = frame_large.resize((frame_width,frame_height))
    frame_mask.paste(image, ((frame_width-width)/2,(frame_height-height)/2))
    return frame_mask 

def logo_place(image, side):
    ''' 
    This function will place a predetermined logo in a specified corner of the image, or in the middle.
    Use middle or upper/lower then left/right to set location of logo on the image.
    '''
    image_width, image_height = image.size
    logo_size = int(min(image_height,image_width)*.2)
    logo = logo_large.resize((logo_size,logo_size))
    border_spacing = .2
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
    image.paste(logo, (int(logo_x), int(logo_y)), mask = logo)
    return image 
    
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
    '''
    calls on all images in a directory to place a logo and border on them
    '''
    if directory == None:
        directory = os.getcwd() 
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed 
    round_logo()
    image_list, file_list = get_images(directory) 
    for n in range(len(image_list)):
        filename, filetype = os.path.splitext(file_list[n])
        new_image = logo_place(image_list[n], side)
        final_image = frame_image(new_image)
        final_image_filename = os.path.join(new_directory,filename + '.png')
        final_image.save(final_image_filename)
        
def test():
    ''' 
    Will test the program in order to see if using proper directories and
    image control. If test passes: directory has been created and image has been
    saved as a .png
    '''
    round_logo()
    for a in range(1):
        if a == 'background.jpg':
            pass
        else:
            
            directory = os.getcwd()
            #set_logo('left')

            directory = os.getcwd()
            set_logo('lower right')
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