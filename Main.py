
import cv2
import numpy as np

# -d configure which camera device to use
# -r Size of foto
# -S visibility range 1 - 10 if parameter not set or set to 0 foto will be black
# if path not specified /home/pi is the default
# EXAMPLE: "fswebcam -d /dev/video0 --no-banner -r 320x240 -S 10 /home/pi/foto.jpg


def main():
    dirFoto = "/home/pi/"
    imageName = "camView.jpg"
    commandToTakeFoto = "fswebcam -d /dev/video0 --no-banner -r 320x240 -S 10 " + dirFoto + imageName
    print("openCV version: " + cv2.__version__)


    image = cv2.imread('resources/ball.png')
    output = image.copy()


    # display the image width, height, and number of channels
    (h, w, c) = image.shape[:3]
    print("width: {} pixels".format(w))
    print("height: {}  pixels".format(h))
    print("channels: {}".format(c))

    # converting image to gray color
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # blurring image
    blur = cv2.blur(image, (5, 5))

    # draw rectangle on image
    # rectangle = cv2.rectangle(image, (50, 50), (175, 175), (255, 0, 0), 5)

    # show image and wait for keypress
    cv2.imshow("Image", gray)
    cv2.waitKey(0)

    # detect circles in the image
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.5, 150)
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
        # show the output image
        cv2.imshow("output", np.hstack([image, output]))
        cv2.waitKey(0)
        print("Circle Found")
    else:
        print("found no circles")




if __name__ == "__main__":
    main()


