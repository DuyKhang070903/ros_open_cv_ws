#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def image_callback(msg):
    bridge = CvBridge()  # Dùng để chuyển đổi giữa ROS Image và OpenCV
    try:
        frame = bridge.imgmsg_to_cv2(msg, "bgr8")
        cv2.imshow("Camera Frame", frame)
        cv2.waitKey(1)

    except Exception as e:
        rospy.logerr("Lỗi khi chuyển đổi hình ảnh: %s", str(e))

def main():
    rospy.init_node('camera_listener')
    rospy.Subscriber("/camera/image_raw", Image, image_callback)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
