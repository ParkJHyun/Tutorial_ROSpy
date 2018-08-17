#!/usr/bin/env python
import rospy, cv2, cv_bridge, numpy
from sensor_msgs.msg import Image

class Follower:
	def __init__(self):
		self.bridge = cv_bridge.CvBridge()
		# cv.namedWindow("window", 1)
		self.image_sub = rospy.Subscriber('camera/image', Image, self.image_callback)
	
	def image_callback(self, msg):
		image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		lower_yellow = numpy.array([ 20 ,100, 100])
		upper_yellow = numpy.array([ 30, 255, 255])
		mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
		
		h, w, d = image.shape
		search_top = 3*h/4
		search_bot = search_top+40
		mask[0:search_top, 0:w] = 0
		mask[search_bot:h, 0:w] = 0
		cv2.imshow("image_raw", image)
		masked = cv2.bitwise_and(image, image, mask=mask)
		sobelx = cv2.Sobel(mask,cv2.CV_8U,1,0,ksize=3)
		cv2.imshow("window2", sobelx)
		cv2.waitKey(3)

rospy.init_node('follower')
follower = Follower()
rospy.spin()
