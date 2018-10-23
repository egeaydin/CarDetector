from gluoncv import model_zoo
from moviepy.editor import VideoFileClip


class CarDetector:
    def __init__(self, video_path, sub_clip=None):
        """Initializes a new car detector class. Prepares the video and gathers the pre-trained model.
            :param str video_path: The absolute path of the video file
            :param tuple sub_clip: Optional parameter to crop the video. A tuple containing two integers,
            first being the start second and second being the end.
        """

        self.video = VideoFileClip(video_path)

        # If sub_clip is defined, crop the video accordingly
        if sub_clip:
            self.video = self.video.subclip(sub_clip[0], sub_clip[1])


        print('Video found, starting to download the dataset.')

        # Obtain pre-trained model from Gluon Zoo
        self.network = model_zoo.get_model('ssd_512_resnet50_v1_voc', pretrained=True)
        print('pre-trained data obtained')

