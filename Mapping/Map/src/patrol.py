#!/usr/bin/env python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

waypoints = [[(2.0, 2.0, 0,0), (0.0, 0.0, 0.0, 1.0)], [(2.93, 2.0, 0.0), (0.0, 0.0, 0.0, 0.0)], [(6.78, 0.93, 0.0), (0.0, 0.0, 0.0, 1.0)], [(0.82, 4.85, 0.0), (0.0, 0.0, 0.0, 1.0)], [(6.78, 3.34, 0.0), (0.0, 0.0, 0.0, 1.0)], [(0.58, 6.35, 0.0), (0.0, 0.0, 0.0, 1.0)], [(8.04, 1.57, 0.0), (0.0, 0.0, 0.0, 1.0)], [(8.98, 9.01, 0.0), (0.0, 0.0, 0.0, 1.0)], [(0.52, 9.06, 0.0), (0.0, 0.0, 0.0, 1.0)], [(9.08, 8.92, 0.0), (0.0, 0.0, 0.0, 1.0)]]

def goal_pose(pose):
	goal_pose = MoveBaseGoal()
	goal_pose.target_pose.header.frame_id='map'
	goal_pose.target_pose.pose.position.x=pose[0][0]
	goal_pose.target_pose.pose.position.y=pose[0][1]
	goal_pose.target_pose.pose.position.z=pose[0][2]
	goal_pose.target_pose.pose.orientation.x=pose[1][0]
	goal_pose.target_pose.pose.orientation.y=pose[1][1]
	goal_pose.target_pose.pose.orientation.z=pose[1][2]
	goal_pose.target_pose.pose.orientation.w=pose[1][3]

	return goal_pose

if __name__ == '__main__':
	rospy.init_node('patrol')
	
	client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
	client.wait_for_server()

	while True:
		for pose in waypoints:
			goal = goal_pose(pose)
			client.send_goal(goal)
			client.wait_for_result()
	
