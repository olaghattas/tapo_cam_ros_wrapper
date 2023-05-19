import rclpy
from rclpy.node import Node
import cv2
import os
from ament_index_python.packages import get_package_share_directory
from rclpy.executors import MultiThreadedExecutor, SingleThreadedExecutor
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

'''
ROS2 node, 
subscribe to RGB image, 
detect human and 
publish x,y,width,height as bounding box

ros2 run yolostate detecthuman --ros-args -p camera:=/smart_home/camera/color/image_raw -p view_camera:=true
'''


class PublishImages(Node):
    def __init__(self, node_name, link, pub_topic_name):
        super().__init__('publish_images')

        self.node = rclpy.create_node(node_name)

        self.link = link

        self.node_name = node_name
        self.bridge = CvBridge()

        self.rgb8pub = self.create_publisher(Image, pub_topic_name, 10)

        timer_period = 0.01 # seconds
        self.timer = self.create_timer(timer_period, self.camera_callback)

    def camera_callback(self):
        cap = cv2.VideoCapture(self.link, cv2.CAP_FFMPEG)
        # cap = cv2.VideoCapture(0)

        print('camera_callback', self.node_name)

        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                # Convert ROS Image message to OpenCV image BGR8
                self.bgr8pub.publish(self.bridge.cv2_to_imgmsg(frame, "bgr8"))

            else:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        self.cap.release()


def main(args=None):
    rclpy.init(args=args)

    password = os.environ['TAPO_CAMERA_PASS']

    ip_address_living = "192.168.1.35"
    username_living = 'Living_room'
    link_living = "rtsp://" + username_living + ":" + password + "@" + ip_address_living + "/stream2"
    node_living_room = PublishImages('living_room_cam', link_living, '/camera_living_room/color/image_raw')

    ip_address_bedroom = "192.168.1.38"
    username_bedroom = 'Bedroom'
    link_bedroom = "rtsp://" + username_bedroom + ":" + password + "@" + ip_address_bedroom + "/stream2"
    node_bedroom = PublishImages('bedroom_cam', link_bedroom, '/camera_living_room/color/image_raw')

    ip_address_dining = "192.168.1.34"
    username_dining = 'Dining'
    link_dining = "rtsp://" + username_dining + ":" + password + "@" + ip_address_dining + "/stream2"
    node_dining_room = PublishImages('dining_room_cam', link_dining, '/camera_living_room/color/image_raw')

    ip_address_kitchen = "192.168.1.37"
    username_kitchen = 'Kitchen'
    link_kitchen = "rtsp://" + username_kitchen + ":" + password + "@" + ip_address_kitchen + "/stream2"
    node_kitchen = PublishImages('kitchen_cam', link_kitchen, '/camera_living_room/color/image_raw')

    executor = SingleThreadedExecutor()

    executor.add_node(node_living_room)
    executor.add_node(node_kitchen)
    executor.add_node(node_dining_room)
    executor.add_node(node_bedroom)

    executor.spin()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
