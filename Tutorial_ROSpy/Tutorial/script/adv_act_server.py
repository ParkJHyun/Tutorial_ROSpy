#! /usr/bin/env python
import rospy

import time
import actionlib
from Tutorial.msg import TimerAction, TimerResult, TimerGoal, TimerFeedback

def do_timer(goal):
	start_time=time.time()
	update_count=0
	
	if goal.time_to_wait.to_sec() > 30.0:
	   result = TimerResult
	   result.time_elapsed = rospy.Duration.from_sec(time.time()-start_time)
	   result.updates_sent =  update_count
	   server.set_aborted(result, "Timer aborted due to long wait!")
	   return 
	while (time.time()-start_time)<goal.time_to_wait.to_sec():
		if server.is_preempt_requested():
		   result = TimerResult
		   result.time_elapsed = \
		   rospy.Duration.from_sec(time.time()-start_time)
		   server.set_preempted(result,"Timer preempted!")
		
		feedback=TimerFeedback()
		feedback.time_elapsed = rospy.Duration.from_sec(time.time()-start_time)
		feedback.time_remaining = goal.time_to_wait - feedback.time_elapsed		
		server.publish_feedback(feedback)		
		update_count += 1
		
		time.sleep(1.0)

	result=TimerResult()
	result.time_elapsed=rospy.Duration.from_sec(time.time()-start_time)
	result.updates_sent = update_count
	server.set_succeeded(result, "Timer completed successfully")

rospy.init_node('adv_act_server')
act_start="Advanced Action Server Actuating ...."
rospy.loginfo(act_start)
server=actionlib.SimpleActionServer('timer',TimerAction, do_timer, False)
server.start()
rospy.spin()
