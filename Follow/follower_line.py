#!/usr/bin/env python
import rospy, cv2, cv_bridge, numpy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

class Follower:
	def __init__(self):
		self.bridge = cv_bridge.CvBridge()
		# cv.namedWindow("window", 1)
		self.image_sub = rospy.Subscriber('camera/image', Image, self.image_callback)
		self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

		self.twist = Twist()

	def image_callback(self, msg):
		image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

		lower_yellow = numpy.array([ 20 ,100, 200])
		upper_yellow = numpy.array([ 30, 255, 255])
		mask_y = cv2.inRange(hsv, lower_yellow, upper_yellow)

		lower_white = numpy.array([200, 200, 200])
		upper_white = numpy.array([255, 255, 255])
		mask_w = cv2.inRange(image, lower_white, upper_white)


		# Get Pixel Height, Weight, density
		height, weight, density = image.shape

		# Make ROI
		top_h = 5*height/6
		bot_h = top_h+40
		mask_y[0:top_h, 0:weight] = 0
		mask_y[bot_h:height, 0:weight] = 0
		mask_w[0:top_h, 0:weight] = 0
		mask_w[bot_h:height, 0:weight]=0

		# Total_image = mask_w+mask_y

		# Sobel Edge
		# rising_sobel = cv2.Sobel(Total_image,cv2.CV_8U,1,0,ksize=3)
		sobel_y = cv2.Sobel(mask_y,cv2.CV_64F,1,0,ksize=3)
		sobel_w = cv2.Sobel(mask_w,cv2.CV_64F,1,0,ksize=3)

		cv2.imshow("sobel_y", sobel_y)
		cv2.imshow("sobel_w", sobel_w)
		# cv2.imshow("Sobel", rising_sobel)

		# Get momentum
		M1 = cv2.moments(sobel_y)
		M2 = cv2.moments(sobel_w)

		if M1['m00']>0 and M2['m00']>0:
			cx_y = int(M1['m10']/M1['m00'])
			cy_y = int(M1['m01']/M1['m00'])
			cx_w = int(M2['m10']/M2['m00'])
			cy_w = int(M2['m01']/M2['m00'])
			err = (cx_w-cx_y) - weight/2
			self.twist.linear.x = 0.01
			img = cv2.circle(image, (err,weight), 5, (0,0,255), -1)
			#self.twist.angular.z = -float(err) / 100
			self.cmd_vel_pub.publish(self.twist)
			cv2.imshow("window1", img)

		cv2.imshow("window", image)
		cv2.waitKey(3)

rospy.init_node('follower')
follower = Follower()
rospy.spin()
