import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw            

def logo_place(image, side):
    image_width, image_height = image.size
    logo.resize(image_width * .125, image_height *.125)
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
    image.paste(logo, (logo_x, logo_y))
    return image 
            
    