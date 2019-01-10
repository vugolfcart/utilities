import rosbag
import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys


def main(path):
    bag = rosbag.Bag(path)
    topics = [
        '/zed/rgb/image_rect_color'
    ]

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    video = cv2.VideoWriter('{}.avi'.format(path), fourcc, 30.0, (1280, 720))

    for topic, message, timestamp in bag.read_messages(topics=topics):
        data = np.array(map(ord, message.data), dtype=np.uint8)
        image = data.reshape(message.height, message.width, 3)
        
        print '{}: [{}]: {}'.format(timestamp, topic, '')
        print 'height={} width={}'.format(message.height, message.width)
        print 'shape={}'.format(image.shape)

        # BGR -> RGB
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)        
        
        # cv2.imshow('image', image)
        # cv2.waitKey(0)
        # plt.imshow(image)
        # plt.show()
        
        # video.write(image)

    video.release()
    bag.close()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'please include path to bag'
        sys.exit()

    path = sys.argv[1]
    main(path)
