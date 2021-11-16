import os

import cv2
import numpy as np

# -d configure which camera device to use
# -r Size of foto
# -S visibility range 1 - 10 if parameter not set or set to 0 foto will be black
# if path not specified /home/pi is the default
# EXAMPLE: "fswebcam -d /dev/video0 --no-banner -r 320x240 -S 10 /home/pi/foto.jpg

'''
-------------
| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |
-------------

maybe a model like this would be okay?
-------------
| 0 | 1 | 2 |
-------------
'''
# once it finds the ball this will be set with codes 0 - 8 found above
ballSegment = None

def main():
    dirFoto = "/home/pi/"
    imageName = "camView.jpg"
    commandToTakeFoto = "fswebcam -d /dev/video0 --no-banner -r 320x240 -S 10 " + dirFoto + imageName
    print("openCV version: " + cv2.__version__)

    dirDif = "resources/difficult/"
    dir = "resources/"
    current = dir
    directory = os.listdir(current)

    for im in directory:
        if im == "difficult":
            continue

        image = cv2.imread(current + im)

        # resizing maybe use scale?
        scale_percent = 220  # percent of original size
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resize image
        image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        # image = cv2.resize(image, (224,224), interpolation=cv2.INTER_AREA)
        output = image.copy()

        # display the image width, height, and number of channels
        # (h, w, c) = image.shape[:3]
        # print("width: {} pixels".format(w))
        # print("height: {}  pixels".format(h))
        # print("channels: {}".format(c))

        # converting image to gray color
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # blurring image
        # gray = cv2.GaussianBlur(gray, (3, 3), cv2.BORDER_DEFAULT)
        gray = cv2.blur(gray, (3, 3))

        # show image and wait for keypress
        # cv2.imshow("Image", gray)
        # cv2.waitKey(0)

        # circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 1000, param1=30, param2=65, minRadius=0, maxRadius=0) todo from Shubham Chopra
        # detect circles in the image - doesnt detect tiny ball in ball5.jfif (should be smaller than camera feed finds)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2.5, 1000, param1=350, param2=100, minRadius=0, maxRadius=0)
        # ensure at least some circles were found
        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")
            # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                # draw the circle in the output image, then draw a rectangle
                # corresponding to the center of the circle
                cv2.circle(output, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
                # todo: do math to place ball in one of the 3 x 3 segments and set ballSegment to code number

            # show the output image
            cv2.imshow("output", np.hstack([image, output]))
            cv2.waitKey(0)
            print("Circle Found")
        else:
            print("found no circles")


if __name__ == "__main__":
    main()


