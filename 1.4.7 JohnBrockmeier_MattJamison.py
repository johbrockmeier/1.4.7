import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw            

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
        new_image_filename = os.path.join(new_directory,filename + '.png')
        new_image.save(new_image_filename)
        
def test():
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
         