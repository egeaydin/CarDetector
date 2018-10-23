from gluoncv import model_zoo
from moviepy.editor import VideoFileClip


class CarDetector:
    def __init__(self, video_path):
        self.video = VideoFileClip(video_path)

        print('Video found, starting to download the dataset.')

        # Obtain pre-trained model from Gluon Zoo
        self.network = model_zoo.get_model('ssd_512_resnet50_v1_voc', pretrained=True)
        print('pre-trained data obtained')

