#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def scan_callback(msg):
	global g_range_ahead
	g_range_ahead = min(msg.ranges)
	print g_range_ahead
	
g_range_ahead = 1
scan_sub = rospy.Subscriber('scan',LaserScan,scan_callback)
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

rospy.init_node('cockroach')
state_change_time = rospy.Time.now()
driving_forward = True
rate = rospy.Rate(10)

go_forward = "GO FORWARD!"
turn = "Turn!"
twist = Twist()

while not rospy.is_shutdown():
	print "%d" % driving_forward
	if driving_forward :
		if (g_range_ahead < 0.6 or rospy.Time.now() > state_change_time):
			driving_forward = False
			state_change_time = rospy.Time.now() + rospy.Duration(2)
	else:
		if rospy.Time.now() > state_change_time :
			driving_foward = True
			state_change_time = rospy.Time.now() + rospy.Duration(2)
		else :
			print "else!"
	
	
	if driving_forward:
		twist.linear.x = 0.2
		rospy.loginfo(go_forward)
	else:
		twist.angular.z = 0.5
		print "Trun!!"

	cmd_vel_pub.publish(twist)

	rate.sleep()
