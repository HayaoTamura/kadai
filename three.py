#!/usr/bin/env python

import rospy

from std_msgs.msg import Int32



n = 0



def cb(message):

    global n
    global p
    n = message.data*2
    p = message.data


if __name__ == '__main__': 

    rospy.init_node('twice')

    sub = rospy.Subscriber('count_up', Int32, cb) 

    pub = rospy.Publisher('twice', Int32, queue_size=1) 

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():

        pub.publish(2*n+3*p)

        rate.sleep()
