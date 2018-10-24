from gluoncv import model_zoo
from moviepy.editor import VideoFileClip, ImageSequenceClip
import mxnet as mx
from mxnet import image as timage
from util import print_progress_bar
import time
import cv2


class CarDetector:
    def __init__(self, video_path, sub_clip=None):
        """Initializes a new car detector class. Prepares the video and gathers the pre-trained model.
            :param str video_path: The absolute path of the video file
            :param tuple sub_clip: Optional parameter to crop the video. A tuple containing two integers,
            first being the start second and second being the end.
        """
        self.video_path = video_path
        self.video = VideoFileClip(video_path)
        print('Video found.')

        # If sub_clip is defined, crop the video accordingly
        if sub_clip:
            self.video = self.video.subclip(sub_clip[0], sub_clip[1])
            print('Video has been edited accordingly to sub clip!')

        self.frames = []
        self.total_frames = self.video.duration * self.video.fps


        print('Starting to download the pre-trained dataset')
        # Obtain pre-trained model from Gluon Zoo
        self.network = model_zoo.get_model('ssd_512_resnet50_v1_voc', pretrained=True)
        print('Pre-trained data obtained')


    def draw_bboxs_on_frame(self, frame, bboxes, scores, labels):
        color = (0, 255, 0)

        for i, score in enumerate(scores):
            sc = score.asscalar()
            if sc > .7:
                xmin, ymin, xmax, ymax = [int(x.asscalar()) for x in bboxes[i]]
                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 1)
                cv2.putText(frame,
                            self.network.classes[int(labels[i].asscalar())],
                            (xmin, ymin - 2), cv2.FONT_HERSHEY_SIMPLEX, 1.0, color, lineType=cv2.LINE_AA)

            else:
                # Since they are ordered high-to-min, once we are lower the threst, no need to look for more
                break
        return frame

    def process_frame(self, frame, short):
        '''
        Process a single frame for object detection
        :param array[][] frame: frame as 2-Dimensional Array
        :param int short: value for resize the image to
        :return NDArray: processed frame
        '''
        mean = (0.485, 0.456, 0.406)
        std = (0.229, 0.224, 0.225)
        max_size = 1024

        img = mx.nd.array(frame)
        img = mx.image.resize_short(img, short)
        if isinstance(max_size, int) and max(img.shape) > max_size:
            img = timage.resize_long(img, max_size)

        orig_img = img.asnumpy().astype('uint8')
        img = mx.nd.image.to_tensor(img)
        img = mx.nd.image.normalize(img, mean=mean, std=std)

        return img.expand_dims(0), orig_img

    def detect(self):
        """
        Detects the cars in the video
        """
        total_time_start = time.time()
        print_progress_bar(0, self.total_frames, prefix='Progress:', suffix='Complete')

        # Loop through the all frames off the video
        for i, frame in enumerate(self.video.iter_frames()):
            start = time.time()

            # We need to process the frames for MxNet
            x, img = self.process_frame(frame, 512)

            class_IDs, scores, bounding_boxs = self.network(x)
            frame = self.draw_bboxs_on_frame(img, bounding_boxs[0], scores[0], class_IDs[0])

            self.frames.append(frame)

            suffix = 'Complete, Frame Process Time:{0:.2f}| Total Elapsed Time:{1:.2f}'.format(time.time() - start,
                                                                                       time.time() - total_time_start)
            print_progress_bar(i + 1, self.total_frames, prefix='Progress:', suffix=suffix)
        print('Total time elapsed processing: {0:.2f}'.format(time.time() - total_time_start))

    def save(self):
        """
        Saves the video with the bounding boxes around the cars
        """
        clip = ImageSequenceClip(self.frames, self.video.fps)

        # Separate the path and the extension
        split = self.video_path.split('.')

        clip.write_videofile("{0}_{1}.{2}".format(split[0], 'detection_result', split[1]))
