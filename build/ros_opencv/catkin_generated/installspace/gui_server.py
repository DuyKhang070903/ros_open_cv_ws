#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def qr_code_callback(data):
    # Hiển thị dữ liệu mã QR nhận được
    rospy.loginfo(f"Nhận được mã QR: {data.data}")
    
    # Đây là nơi bạn có thể hiển thị thông tin mã QR trên GUI hoặc xử lý nó
    # Giả sử chỉ in ra thông tin mã QR để minh họa
    print(f"Thông tin mã QR: {data.data}")

def gui_server():
    # Khởi tạo ROS node
    rospy.init_node('gui_server', anonymous=True)
    
    # Đăng ký subscriber cho topic '/qr_code_data'
    rospy.Subscriber('/qr_code_data', String, qr_code_callback)
    
    # Giữ node chạy
    rospy.spin()

if __name__ == '__main__':
    try:
        gui_server()
    except rospy.ROSInterruptException:
        pass

