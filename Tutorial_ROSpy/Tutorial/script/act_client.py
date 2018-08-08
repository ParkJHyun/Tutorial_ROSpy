#!/usr/bin/env python

import rospy

import actionlib
from Tutorial.msg import TimerGoal, TimerAction, TimerResult

rospy.init_node('act_client')
client=actionlib.SimpleActionClient('timer', TimerAction)

client.wait_for_server()
goal=TimerGoal()
goal.time_to_wait=rospy.Duration.from_sec(10.0)
client.send_goal(goal)
client.wait_for_result()
print('Timer elapsed : %f'%(client.get_result().time_elapsed.to_sec()))

