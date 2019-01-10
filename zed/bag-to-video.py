import rosbag
import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys
from cv_bridge import CvBridge, CvBridgeError


def main(path):
    bridge = CvBridge()
    bag = rosbag.Bag(path)
    topics = [
        '/zed/rgb/image_rect_color'
    ]

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    video = cv2.VideoWriter('{}.avi'.format(path), fourcc, 30.0, (1280, 720), True)

    for topic, message, timestamp in bag.read_messages(topics=topics):
        print '{}: [{}]: {}'.format(timestamp, topic, '')

        try:
            image = bridge.imgmsg_to_cv2(message)
            video.write(image)
        except CvBridgeError as e:
            print e

    bag.close()
    cv2.destroyAllWindows()
    video.release()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'please include path to bag'
        sys.exit()

    path = sys.argv[1]
    main(path)
