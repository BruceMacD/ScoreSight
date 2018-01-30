# import the necessary packages
from PIL import Image
import pytesseract
import cv2
import os

# statically set image for testing
file_src = "data/JustFoxScore.png"


def grayscale(src):
    img = cv2.imread(src)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # not doing any noise removal or threshold preprocessing
    # it makes results worse in this case

    # image must be saved processing, would like a workaround, this is some overhead
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    return filename


def cleanup(files):
    # clean up files after processing
    for file in files:
        os.remove(file)


def read_score(frame):
    # TODO: find team names and score from data read
    text = pytesseract.image_to_string(Image.open(grayscale_file))
    words = text.split()
    print(words)


if __name__ == "__main__":
    grayscale_file = grayscale(file_src)
    read_score(grayscale_file)
    cleanup([grayscale_file])
