import cv2



# -d configure which camera device to use
# -r Size of foto
# -S visibility range 1 - 10 if parameter not set or set to 0 foto will be black
# if path not specified /home/pi is the default
# EXAMPLE: "fswebcam -d /dev/video0 --no-banner -r 320x240 -S 10 /home/pi/foto.jpg
def main():
    dirFoto = "/home/pi/"
    imageName = "camView.jpg"
    commandToTakeFoto = "fswebcam -d /dev/video0 --no-banner -r 320x240 -S 10 " + dirFoto + imageName
    print("hi")


if __name__ == "__main__":
    main()


