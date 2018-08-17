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
		search_bot = search_top+20
		mask[0:search_top, 0:w] = 0
		mask[search_bot:h, 0:w] = 0
		M = cv2.moments(mask)
		if M['m00'] > 0:
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			cv2.circle(image, (cx, cy), 3, (0, 0, 255), -1)
	
		cv2.imshow("window2", image)
		cv2.waitKey(3)

rospy.init_node('follower')
follower = Follower()
rospy.spin()
