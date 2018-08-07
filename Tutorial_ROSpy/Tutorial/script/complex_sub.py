#!/usr/bin/env python
import rospy
from Tutorial.msg import Complex

def callback(msg):
	print "Real :", msg.real
	print "Imaginary :", msg.imaginary
	print

rospy.init_node('complex_sub')
sub = rospy.Subscriber('complex', Complex, callback)
rate=rospy.Rate(2)

rospy.spin()
