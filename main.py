import cv2
import numpy
import numpy as np
from PIL import Image
import math

if __name__ == "__main__":
    img = cv2.imread(r'512-by-512.jpg', 0)

    window = 2
    img_width = img.shape[0]
    img_height = img.shape[1]

    new_img = []
    if img_width % 4 == 0 & img_height % 4 == 0:
        original_img = img
        y_axis = 0

        for row in range(0, img_width, window):
            # for row in range(0, 1, window):
            new_img_row = []
            for col in range(0, img_height, window):
                # | img(col, row)   |  img(col+1, row)  |
                # | img(col, row+1) | img(col+1, row+1) |
                # avg_pixel = ((int(img[col, row]) + int(img[col + 1, row]) + int(img[col, row + 1]) + int(
                #     img[col + 1, row + 1])) / 4)
                avg_pixel = ((int(img[row, col]) + int(img[row + 1, col]) + int(img[row, col + 1]) + int(
                    img[row + 1, col + 1])) / 4)

                new_img_row.append(avg_pixel)

            new_img.append(new_img_row)
        ar = numpy.array(new_img)
        #
        im = Image.fromarray(ar)

        # This is to solve technical problem of Python, not about the idea.
        if im.mode != 'RGB':
            im = im.convert('RGB')
        im.save("512-by-512-shrink.jpg")
    else:
        pass



