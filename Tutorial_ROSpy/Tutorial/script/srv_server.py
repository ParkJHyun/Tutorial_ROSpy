#!/usr/bin/env python

import rospy
from Tutorial.srv import WordCount, WordCountResponse

def count_word(request):
	return WordCountResponse(len(request.words.split()))

rospy.init_node('srv_server')
service = rospy.Service('count', WordCount, count_word)
info = "Service Server Start!"
rospy.loginfo(info)

rospy.spin()

