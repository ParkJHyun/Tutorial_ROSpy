#!/usr/bin/env python

import rospy
from smach import State, StateMachine

from time import sleep

class Drive(State):
    def __init__(self, distance):
        State.__init__(self, outcomes=['success'])
        self.distance = distance

    def execute(self, userdata):
        print 'Driving', self.distance
        sleep(1)
        return 'success'

class Turn(State):
    def __init__(self, angle):
        State.__init__(self, outcomes=['success'])
        sleep(1)
        self.angle = angle

    def execute(self, userdata):
        print 'Turn', self.angle
        sleep(1)
        return 'success'

def polygon(sides):
    polygon = StateMachine(outcomes=['success'])
    with polygon:
        for i in xrange(sides - 1):
            StateMachine.add('SIDE_{0}'.format(i+1), Drive(1), transitions={'success':'TURN_{0}'.format(i+1)})

        for i in xrange(sides - 1):
            StateMachine.add('TURN_{0}'.format(i+1), Turn(360.0/sides), transitions={'success':'SIDE_{0}'.format(i+2)})

        StateMachine.add('SIDE_{0}'.format(sides), Drive(1), transitions={'success':'success'})

    return polygon

if __name__=='__main__':
    triangle = polygon(3)
    square = polygon(4)

    shapes = StateMachine(outcomes=['success'])
    with shapes:
        StateMachine.add('TRIANGLE', triangle, transitions={'success':'SQUARE'})
        StateMachine.add('SQUARE', square, transitions={'success':'success'})

    shapes.execute()



