import PIL
import os.path  
import PIL.ImageDraw 
import matplotlib.pyplot as plt      

logo_raw = PIL.Image.open('test_image.jpg')
def round_corners():
    """ Rounds the corner of a PIL.Image

    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1 is the corner radius as 
    portion of shorter dimension of original_image
    """
    #set the radius of the rounded corners
    width, height = logo_raw.size
    radius = int(min(width/2, height/2)) #radius in pixels

    ###
    #create a mask
    ###

    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)

    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask

    # Draw two rectangles to fill interior with opaqueness 


    #Draw four filled circles of opaqueness
    drawing_layer.ellipse((250,500, 1000, 1000), 
                          fill=(0,127,127,255)) #top left


    # Uncomment the following line to show the mask
    plt.imshow(rounded_mask)

    # Make the new image, starting with all transparent
    logo_large = PIL.Image.new('RGBA', logo_raw.size, (0,0,0,0))
    logo_large.paste(logo_raw, (0,0), mask=rounded_mask)
    return logo_large
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
    logo = logo_large.resize((int(image_width * .125), int(image_height *.125)))
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
        final_image = frame_image(new_image)
        final_image_filename = os.path.join(new_directory,filename + '.png')
        final_image.save(final_image_filename)
        
def test():
    ''' 
    Will test the program in order to see if using proper directories and
    image control. If test passes: directory has been created and image has been
    saved as a .png
    '''
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