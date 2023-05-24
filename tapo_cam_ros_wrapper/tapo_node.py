import rclpy
from rclpy.node import Node
import cv2
import os
from ament_index_python.packages import get_package_share_directory
from rclpy.executors import MultiThreadedExecutor, SingleThreadedExecutor
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

import time

'''
ROS2 node, 
subscribe to RGB image, 
detect human and 
publish x,y,width,height as bounding box

ros2 run yolostate detecthuman --ros-args -p camera:=/smart_home/camera/color/image_raw -p view_camera:=true
'''


class PublishImages(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        print('init')
        self.declare_parameter("username", "default_value")
        # Access the parameter value
        username = self.get_parameter("username").get_parameter_value().string_value

        self.declare_parameter("ip_address", "default_value")
        # Access the parameter value
        ip_address = self.get_parameter("ip_address").get_parameter_value().string_value

        self.declare_parameter("pub_topic_name", "default_value")
        # Access the parameter value
        pub_topic_name = self.get_parameter("pub_topic_name").get_parameter_value().string_value
        print("gGGGGGGGGGGGGG", username , ip_address, pub_topic_name )
        password = os.environ['TAPO_CAMERA_PASS']
        self.link = "rtsp://" + username + ":" + password + "@" + ip_address + "/stream2"

        self.node_name = node_name
        self.bridge = CvBridge()

        self.rgb8pub = self.create_publisher(Image, pub_topic_name, 10)

        self.cap = cv2.VideoCapture(self.link, cv2.CAP_FFMPEG)

    def camera_callback(self):
        # cap = cv2.VideoCapture(0)

        print('camera_callback', self.node_name)
        import random

        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                # Convert ROS Image message to OpenCV image BGR8
                self.rgb8pub.publish(self.bridge.cv2_to_imgmsg(frame, "bgr8"))



def main(args=None):
    rclpy.init(args=args)
    node = PublishImages("my_node")

    # ip_address_living = "192.168.1.35"
    # username_living = 'Living_room'
    # link_living = "rtsp://" + username_living + ":" + password + "@" + ip_address_living + "/stream2"
    # node_living_room = PublishImages('living_room_cam', link_living, '/camera_living_room/color/image_raw')
    #


    print('before_ok')
    while rclpy.ok():
        print('after_ok')
        # node_kitchen.camera_callback()
        # node_dining_room.camera_callback()
        # node_living_room.camera_callback()
        node.camera_callback()
        # time.sleep(2)

    # executor = SingleThreadedExecutor()
    #
    # executor.add_node(node_living_room)
    # executor.add_node(node_kitchen)
    # executor.add_node(node_dining_room)
    # executor.add_node(node_bedroom)
    #
    # executor.spin()
    # rclpy.spin(node_dining_room)
    rclpy.shutdown()

    node.cap.release()
    # node_dining_room.cap.release()
    # node_bedroom.cap.release()
    # node_living_room.cap.release()


if __name__ == '__main__':
    main()
