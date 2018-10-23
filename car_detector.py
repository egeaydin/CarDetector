from gluoncv import model_zoo

class CarDetector:
    def __init__(self, video_path):
        print('starting')

        self.network = model_zoo.get_model('ssd_512_resnet50_v1_voc', pretrained=True)
        print('pre-trained data obtained')

        print(video_path)
