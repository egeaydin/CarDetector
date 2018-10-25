# CarDetector
Simple Car Detector that detects cars in videos and draws bounding boxes back on the video

![Original Video Example][4] ![Detected Video Example][5]

## Installation Guide
This project uses:
* [MXNet][1] to download trained data and detect objects. 
* [OpenCV][2] is used to draw the bounding boxes to the frames
* [MoviePY][2] is used for looping through the frames of the video and rendering a new video with bounding boxes

Install the requirements with pip:
`pip install -r requirements.txt`

## Usage
Open up a command prompt(Windows) or terminal(Mac, Linux) and go to the project folder. Then run the command:  
`python detect.py {video_path} {start_second} {end_second}`  

`param str video_path`: is the absolute path of the video file.  
`param int start_second`: optional parameter for defining at which second of the video detection should start. 
If you specify start second you need to specify the end second as well.  
`param int end_second`: optional parameter for defining at which second of the video detection should stop.

### Example commands
`python detect.py C:\Users\user\movie.mov`: will detect the cars in the entire video.  
`python detect.py C:\Users\user\movie.mov 0 40`: will detect the car from the beginning to 40th second of the video 
and the new video will be between those seconds.  
`python detect.py C:\Users\user\movie.mov 10 50`: will detect the car from the 10th second to 50th second of the video 
and the new video will be between those seconds. 


## Issues
* Drawing the bounding boxes takes a long time
* Some vehicles are not detected if they are hidden or far
* Dataset is free and limited, a better dataset can be used for better accuracy

## Eager to help?
Everybody is welcome for contribution. Let's exceed the potential of this project and get the maximum accuracy,
 this cannot be done alone. Even small advices and suggestions are appreciated.

[1]: http://mxnet.incubator.apache.org/ "MxNet"
[2]: https://zulko.github.io/moviepy/ "MoviePy"
[3]: https://opencv.org/ "OpenCV"
[4]: github/example_org.gif
[5]: github/example_detected.gif

