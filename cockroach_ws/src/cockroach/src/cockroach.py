#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def scan_callback(msg):
	global g_range_ahead
	g_range_ahead = min(msg.ranges)
	
	
g_range_ahead = 1.2
scan_sub = rospy.Subscriber('scan',LaserScan,scan_callback)
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

rospy.init_node('cockroach')
state_change_time = rospy.Time.now()
driving_forward = True
rate = rospy.Rate(10)

go_forward = "GO FORWARD!"
turn = "Turn!"
twist = Twist()

def go_back():
	twist=Twist()
	twist.linear.x= -1

while not rospy.is_shutdown():
	if driving_forward :
		if (g_range_ahead < 1.1 and rospy.Time.now() > state_change_time):
			driving_forward = False
			state_change_time = rospy.Time.now() + rospy.Duration(2)
		elif (g_range_ahead < 0.5 or g_range_ahead > 5) :
			go_back()
	
	else :
		if rospy.Time.now() > state_change_time :
			driving_forward = True
			state_change_time = rospy.Time.now() + rospy.Duration(10)
	
	if driving_forward:
		twist.linear.x = 0.2
		twist.angular.z=0
		
	else:
		twist.angular.z = 0.8
		twist.linear.x=0
		

	cmd_vel_pub.publish(twist)

	rate.sleep()
