# CarDetector
Simple Car Detector that detects cars in videos and draws bounding boxes back on the video


## Installation Guide
This project uses:
* [MXNet][1] to download trained data and detect objects. 
* [OpenCV][2] is used to draw the bounding boxes to the frames
* [MoviePY][2] is used for looping through the frames of the video and rendering a new video with bounding boxes

Install the requirements with pip:
`pip install -r requirements.txt`

[1]: http://mxnet.incubator.apache.org/ "MxNet"
[2]: https://zulko.github.io/moviepy/ "MoviePy"
[3]: https://opencv.org/ "OpenCV"

## Usage
Open up a command prompt(Windows) or terminal(Mac, Linux) and go to the project folder. Then run the command:  
`python detect.py {video_path}`  

`video_path`: is the absolute path of the video file. Ex: `python detect.py C:\Users\user\movie.mov`

