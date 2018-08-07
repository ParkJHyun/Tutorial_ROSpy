#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callback(msg):
	print msg.data

rospy.init_node('subscribe_node')
sub = rospy.Subscriber('count',Int32,callback)

rospy.spin()
