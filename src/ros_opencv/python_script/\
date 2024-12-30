#!/usr/bin/env python

import cv2 as cv
from pyzbar import pyzbar
import rospy
from std_msgs.msg import String

def qr_code_scanner():
    # Khởi tạo ROS node
    rospy.init_node('qr_code_scanner', anonymous=True)
    
    # Tạo ROS Publisher, gửi dữ liệu mã QR lên topic '/qr_code_data'
    qr_pub = rospy.Publisher('/qr_code_data', String, queue_size=10)

    # Mở camera
    cap = cv.VideoCapture(2)

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            rospy.loginfo("Không thể nhận diện khung hình")
            break

        # Phát hiện mã QR code
        barcodes = pyzbar.decode(frame)

        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type
            text = "{} - {} ".format(barcodeData, barcodeType)

            # Xuất thông tin mã QR lên ROS topic
            rospy.loginfo(f"Đã phát hiện mã QR: {text}")
            qr_pub.publish(f"{barcodeData} - {barcodeType}")
            
            # Hiển thị thông tin lên cửa sổ video
            cv.putText(frame, text, (x - 10, y - 10), cv.FONT_HERSHEY_SIMPLEX, 
                       0.5, (0, 0, 255), 1)

        # Hiển thị khung hình
        cv.imshow('Doc Ma Vach - Ma QR', frame)

        # Nhấn phím 'q' để thoát
        if cv.waitKey(1) == ord('q'):
            break

    # Giải phóng tài nguyên
    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    try:
        qr_code_scanner()
    except rospy.ROSInterruptException:
        pass

