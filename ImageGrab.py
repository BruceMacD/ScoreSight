import pyscreenshot as ImageGrab
import cv2
import os


def capture_custom(box):
    im = ImageGrab.grab(bbox=(box['x1'], box['y1'], box['x2'], box['y2']))
    # save to to file for use with unique name
    filename = "{}.png".format(os.getpid())
    im.save(filename, "PNG")
    return filename


def grayscale(src):
    img = cv2.imread(src)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # not doing any noise removal or threshold preprocessing
    # it makes results worse in this case

    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    return filename


def cleanup(files):
    # clean up files after processing
    for file in files:
        os.remove(file)
