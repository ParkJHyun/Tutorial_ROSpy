#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int32

def talker():
    pub = rospy.Publisher('count', Int32, queue_size=2)
    rospy.init_node('publish_node', anonymous=True)
    count = 0
    rate = rospy.Rate(2) # 10hz
    while not rospy.is_shutdown():
        pub.publish(count)
	count += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
