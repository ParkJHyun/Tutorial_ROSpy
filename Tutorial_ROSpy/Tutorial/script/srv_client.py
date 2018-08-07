#!/usr/bin/env python

import rospy
from Tutorial.srv import WordCount
import sys

rospy.init_node('srv_client')
rospy.wait_for_service('count')
word_counter=rospy.ServiceProxy('count', WordCount)
words=' '.join(sys.argv[1:])
word_count=word_counter(words)

client_msg='srv_clinet find a service!'
rospy.loginfo(client_msg)
print words,'->', word_count.count
