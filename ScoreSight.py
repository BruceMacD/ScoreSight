from ScoreReader import read_score
from ImageGrab import capture_custom, grayscale, cleanup
from pymouse import PyMouseEvent
import time

# bounding box (x1,y1,x2,y2)
bounding_box = {}


# workaround to break from OnClick listener
class OnClickInterrupt(Exception):
    pass


class InvalidBoundingBox(Exception):
    pass


# manages the click coordinates to set bounding box
class OnClick(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)

    def click(self, x, y, button, press):
        if button == 1:
            if press:
                if 'x1' not in bounding_box:
                    # set first coordinate
                    bounding_box["x1"] = x
                    bounding_box["y1"] = y
                    print("Please select the bottom right corner of your box (x2, y2).\n")
                else:
                    # set second coordinate
                    bounding_box["x2"] = x
                    bounding_box["y2"] = y
                    raise OnClickInterrupt("Bounding box set.")
        else:
            print("Setup aborted. Exiting...")
            exit(0)


def error_check_box():
    # check for unexpected overlap in coordinates
    if bounding_box['x1'] >= bounding_box['x2']:
        raise InvalidBoundingBox("The value of coordinate x1 should be less than x2.")
    if bounding_box['y1'] >= bounding_box['y2']:
        # value of y goes down as clicked position goes up
        raise InvalidBoundingBox("The value of coordinate y1 should be less than y2.")


if __name__ == "__main__":
    print("Welcome to ScoreSight\n")
    print("Beginning selection of bounding box. To exit right-click anywhere.\n")
    print("Please select the top left corner of your box (x1, y1).\n")
    # get user input for area to capture
    Click = OnClick()
    try:
        Click.run()
    except OnClickInterrupt as e:
        print(e.args[0])

    try:
        error_check_box()
    except InvalidBoundingBox as e:
        print("Error: {}".format(e.args[0]))
        print("Bounding box: {}".format(bounding_box))
        exit(1)

    print("Processing... (CTRL+C to exit)")

    while True:
        frame = capture_custom(bounding_box)
        gray_frame = grayscale(frame)

        read_score(gray_frame)
        cleanup([gray_frame])

        # TODO: remove wait?
        # Wait for a new frame
        time.sleep(1)
