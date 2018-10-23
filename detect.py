from car_detector import CarDetector
import sys

if len(sys.argv) < 2:
    raise Exception("Please specify the absolute path of the video file. Ex: python detect.py C:\\Users\\user\\movie.mov")

detector = CarDetector(sys.argv[1])

