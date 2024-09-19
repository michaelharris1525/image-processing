from byuimage import Image
import sys
# import os

# used to flip images vertically
def flipped(filename, output_filename) :
    image_from_file = filename
    height = image_from_file.height
    width = image_from_file.width
    new_blank_image = Image.blank(width, height)
    for y in range(0, height) :
       for x in range(0, width) :
           og_pixel = image_from_file.get_pixel(x, y)
           opposite_pixel = new_blank_image.get_pixel(x, height - y - 1)
           opposite_pixel.red = og_pixel.red
           opposite_pixel.green = og_pixel.green 
           opposite_pixel.blue = og_pixel.blue
    new_blank_image.save(output_filename)
    return new_blank_image
    # new_blank_image.show()

def mirror(filename, output_filename) :
    image_from_file = filename

    height = image_from_file.height
    width = image_from_file.width
   
    new_blank_image = Image.blank(width, height)
    for y in range(0, height) :
       for x in range(0, width) :
           og_pixel = image_from_file.get_pixel(x, y)
           opposite_pixel = new_blank_image.get_pixel(width - x - 1, y)
           opposite_pixel.red = og_pixel.red
           opposite_pixel.green = og_pixel.green 
           opposite_pixel.blue = og_pixel.blue
    # new_blank_image.show()
    new_blank_image.save(output_filename)
    return new_blank_image
    


def make_borders(filename, thickness, red, green, blue, output_file_name) :
    image_from_file = filename
    height = image_from_file.height
    width = image_from_file.width
    real_thickness = int (thickness)
    new_blank_image = Image.blank(width + (2 * real_thickness), height + (2 * real_thickness))
    new_height = new_blank_image.height
    new_width = new_blank_image.width

    # top thickness border
    for y in range(0, real_thickness) :
       for x in range(0, new_width) :
           pixel_new = new_blank_image.get_pixel(x, y)
           pixel_new.red = red
           pixel_new.green = green
           pixel_new.blue = blue
           
    # bottom border
    for y in range((new_height - real_thickness), new_height) :
        for x in range(new_width) :
            pixel_new = new_blank_image.get_pixel(x, y)
            pixel_new.red = red
            pixel_new.green = green
            pixel_new.blue = blue

    # left and right border
    for y in range(real_thickness, (new_height - real_thickness)) :
        # left border
        for x in range(real_thickness) :
            pixel_new = new_blank_image.get_pixel(x, y)
            pixel_new.red = red
            pixel_new.green = green
            pixel_new.blue = blue
        # right border
        for x in range((new_width - real_thickness), new_width) :
            pixel_new = new_blank_image.get_pixel(x, y)
            pixel_new.red = red
            pixel_new.green = green
            pixel_new.blue = blue

    # Copying image intor new image with thickness
    for y in range(height) :
        for x in range(width) :
            og_pixel = image_from_file.get_pixel(x, y)
            pixel_new = new_blank_image.get_pixel(x + real_thickness, y + real_thickness)
            pixel_new.red = og_pixel.red
            pixel_new.green = og_pixel.green
            pixel_new.blue = og_pixel.blue
    # print(thickness)
    # new_blank_image.show()
    new_blank_image.save(output_file_name)
    return new_blank_image

# works but need to figure out how to use command line with images
def darken(image_file, percentage, output_file_name) :

    height = image_file.height
    width = image_file.width
    for y in range(height) :
        for x in range (width) :
            pixel = image_file.get_pixel(x, y)
            pixel.red = pixel.red * (1 - percentage)
            pixel.green = pixel.green * (1 - percentage)
            pixel.blue = pixel.blue * (1 - percentage)
    # image_file.show()
    image_file.save(output_file_name)
    return True


def sepia(filename, output_file_name):
    """Write your code here"""
    image_file = filename
    height = image_file.height
    width = image_file.width
    for y in range(height) :
        for x in range (width) :
            pixel = image_file.get_pixel(x, y)
            red_filter = (pixel.red * 0.393) + (0.769 * pixel.green) + (0.189 * pixel.blue)
            green_filter = 0.349*pixel.red + 0.686*pixel.green + 0.168*pixel.blue
            blue_filter = 0.272 * pixel.red + 0.534*pixel.green + 0.131*pixel.blue
            pixel.red = red_filter
            pixel.green = green_filter
            pixel.blue = blue_filter

            # change these to if statements
            if pixel.red > 255 :
                pixel.red = 255
            elif pixel.green > 255 :
                pixel.green = 255
            elif pixel.blue > 255 :
                pixel.blue = 255
    image_file.save(output_file_name)
    # image_file.show()

def grayscale(filename, output_file_name):
    """Write your code here"""
    image_file = filename
    height = image_file.height
    width = image_file.width
    for y in range(height) :
        for x in range (width) :
            pixel = image_file.get_pixel(x, y)
            average = (pixel.red + pixel.green + pixel.blue) / 3
            pixel.red = average
            pixel.green = average
            pixel.blue = average 
    image_file.save(output_file_name)
    # image_file.show()

# def detect_green(pixel, threshold, factor) :
#     f = float(factor)
#     red = int(pixel.red)
#     blue = int(pixel.blue)
#     green = int(pixel.green)
#     average = red + blue + green / 3
#     threshold_int = int(threshold)

#     # if green > blue + threshold_int and green > red + threshold_int :
#     if green >= f * average and green > threshold_int :
#         return True
#     else :
#         return False
    

# def ignore_green_and_copy_images(filename1, filename2, threshold, output_file_name, factor) :
#     foreground = filename1
#     background =  filename2

#     height = foreground.height
#     width = foreground.width
#     new_blank_file_image = Image.blank(width, height)

#     for y in range(height) :
#         for x in range(width) :
#             foreground_pixels = foreground.get_pixel(x, y)
#             background_pixels = background.get_pixel(x, y)


#             pixels_new_transferred = new_blank_file_image.get_pixel(x, y)

#             if detect_green(foreground_pixels, threshold, factor) == False :
#                 pixels_new_transferred.red = foreground_pixels.red
#                 pixels_new_transferred.green = foreground_pixels.green
#                 pixels_new_transferred.blue = foreground_pixels.blue
#             else :
#                 pixels_new_transferred.red = background_pixels.red
#                 pixels_new_transferred.green = background_pixels.green
#                 pixels_new_transferred.blue = background_pixels.blue
#     new_blank_file_image.save(output_file_name)
    # new_blank_file_image.show()
    
def detect_green(pixel, threshold, factor):
    f = float(factor)
    t = int(threshold)
    average = (pixel.red + pixel.green + pixel.blue) / 3
    if pixel.green >= f * average and pixel.green > t :
        return True
    else:
        return False           

def green_screen(foreground, background, threshold, outputfilename, factor):
    final = Image.blank(background.width,background.height)
    for y in range(background.height):
        for x in range(background.width):
            fp = final.get_pixel(x,y)
            bp = background.get_pixel(x,y)
            fp.red = bp.red
            fp.green = bp.green
            fp.blue = bp.blue

    for y in range(foreground.height):
        for x in range(foreground.width):
            fp = foreground.get_pixel(x, y)
            if not detect_green(fp, threshold, factor):
                np = final.get_pixel(x,y)
                np.red = fp.red
                np.green = fp.green
                np.blue =fp.blue
    final.save(outputfilename)
    return final




# to make 4 images into a collage
def collage(filename1, filename2, filename3, filename4, output_file_name, border_thickness) :
    # image_from_file = Image(filename1)
    # image2_rc = Image(filename2)
    # image3_blc = Image(filename3)
    # image4_brc = Image(filename4)
    image_from_file = filename1
    image2_rc = filename2
    image3_blc = filename3
    image4_brc = filename4

    height = image_from_file.height
    height2 = image2_rc.height

    width = image_from_file.width
    width2= image2_rc.width
   
    thickness = int(border_thickness)
    # thickness = border_thickness
    # collage_height = image_from_file.height + image2_rc.height + image3_blc.height + image4_brc.height
    collage_height = height + height2 
    collage_width = width + width2 
    # collage_width = image_from_file.width + image2_rc.width + image3_blc.width + image4_brc.width
    new_blank_image = Image.blank(collage_width + (3 * thickness), collage_height + (3 * thickness)) 
    for y in range(collage_height + (3 * thickness)) :
        for x in range(collage_width + (3 * thickness)) :
            get_pixels = new_blank_image.get_pixel(x, y)
            get_pixels.red = 0
            get_pixels.green = 0
            get_pixels.blue = 0
    


    for y in range(height) :
        for x in range(width) :
            get_pixels = image_from_file.get_pixel(x, y)
            get_pixels2 = image2_rc.get_pixel(x, y)
            get_pixels3 = image3_blc.get_pixel(x, y)
            get_pixels4 = image4_brc.get_pixel(x, y)


            pixel_new_1 = new_blank_image.get_pixel(x + thickness, y + thickness)
            pixel_new_2 = new_blank_image.get_pixel(x + (2 * thickness) + width, y + thickness)
            pixel_new_3 = new_blank_image.get_pixel(x + thickness, y + (2 * thickness) + height)
            pixel_new_4 = new_blank_image.get_pixel(x + (2 * thickness) + width, y + (2 * thickness) + height)

            pixel_new_1.red = get_pixels.red
            pixel_new_1.green = get_pixels.green
            pixel_new_1.blue = get_pixels.blue

            pixel_new_2.red = get_pixels2.red
            pixel_new_2.green = get_pixels2.green
            pixel_new_2.blue = get_pixels2.blue

            pixel_new_3.red = get_pixels3.red
            pixel_new_3.green = get_pixels3.green
            pixel_new_3.blue = get_pixels3.blue

            pixel_new_4.red = get_pixels4.red
            pixel_new_4.green = get_pixels4.green
            pixel_new_4.blue = get_pixels4.blue
    # new_blank_image.show()
    new_blank_image.save(output_file_name)
    return new_blank_image


args = sys.argv
def validate_commands() :
    # display
    if args[1] == "-d" and len(args) > 1:
        print("its true/it works")
        image_from_file = Image(args[2])
        # print(os.getcwd())
        image_from_file.show()
        return True
    
    # darken_filter: -k, input_file, outputfile Name, percent float
    elif args[1] == "-k" and len(args) >= 3 :
        image_from_file = Image(args[2])
        output_file = args[3]
        percent = float(args[4])
        darken(image_from_file, percent, output_file)
        # image_from_file.save(output_file)
        return True
    
    # sepia filter: -s <input file> <output file>
    elif args[1] == "-s" and len(args) > 1 :
        image_from_file = Image(args[2])
        output_file = args[3]
        sepia(image_from_file, output_file)
        return True
    # Grayscale: -g <input file> <output file>
    elif args[1] == "-g" and len(args) > 1 :
        image_from_file = Image(args[2])
        output_file = args[3]
        grayscale(image_from_file, output_file)
        return True
    
    # Borders: -b <input file> <output file> <thickness> <red> <green> <blue>
    elif args[1] == "-b" and len(args) > 6 :
        image_from_file = Image(args[2])
        output_file = args[3] 
        thickness = args[4] 
        red = args[5]
        green = args[6]
        blue = args[7]
        make_borders(image_from_file, thickness, red, green, blue, output_file)
        # image_from_file.save(output_file)
        return True
    
    # flipped: -f <input file> <output file>
    elif args[1] == "-f" and len(args) > 1 :
        image_from_file = Image(args[2])
        output_file = args[3] 
        flipped(image_from_file, output_file)
        return True
    
    # mirror: -m <input file> <output file>
    elif args[1] == "-m" and len(args) > 1 :
        image_from_file = Image(args[2])
        output_file = args[3] 
        mirror(image_from_file, output_file)
        return True
    
# Collage: -c, <image 1>, <image 2>, <image 3>, <image 4>, <output image>, <border thickness>
# 7 inputs
    elif args[1] == "-c" :
        image_from_file = Image(args[2])
        image2 = Image(args[3])
        image3 = Image(args[4])
        image4 = Image(args[5])
        output_file = args[6] 
        b_thickness = args[7]
        collage(image_from_file, image2, image3, image4, output_file, b_thickness)
        return True
    
    # -y, <foreground image>, <background image>, <output file>, <threshold>, <factor>
    elif args[1] == "-y" :
        image_from_file = Image(args[2])
        image2 = Image(args[3])
        output_file_name_ = args[4] 
        threshold = args[5]
        factor = args[6]
        # ignore_green_and_copy_images(image_from_file, image2, threshold, output_file_name_, factor)
        green_screen(image_from_file, image2, threshold, output_file_name_, factor)
        return True

    else :
        print("you did something wrong")
        return False
    
# user_input_list = []
# user_input_list = input("Give me your list of inputs\n")
# validate_commands()


if __name__ == "__main__":
#    ignore_green_and_copy_images("man.input.jpg", "explosion.input.jpg", 30)
   validate_commands()
   pass