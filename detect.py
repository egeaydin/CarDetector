from car_detector import CarDetector
import sys

if len(sys.argv) < 2:
    raise Exception("Please specify the absolute path of the video file. Ex: python detect.py C:\\Users\\user\\movie.mov")

sub_clip = None
# means only the start second specified
if len(sys.argv) == 3:
    raise Exception("Please specify the end second of the sub_clip. Ex: python detect.py C:\\Users\\user\\movie.mov 10 40")

# means we have enough parameters to specify a sub clip
if len(sys.argv) == 4:

    try:
        sub_clip = (int(sys.argv[2]), int(sys.argv[3]))
    except ValueError:
        raise Exception("Start and End second parameters has to be valid integers!")

detector = CarDetector(sys.argv[1], sub_clip)
# Detect the cars in the video
detector.detect()

# Save the video to a new video file
detector.save()

