# import the necessary packages
from PIL import Image
import pytesseract


def read_score(frame):
    # TODO: find team names and score from data read
    text = pytesseract.image_to_string(Image.open(frame))
    words = text.split()
    print(words)
