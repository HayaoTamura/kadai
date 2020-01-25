#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

n = 0
p = 0
def cb(message):
    global n
    global p
    n = message.data*2
    p = message.data*3
    
if __name__ == '__main__': 
    rospy.init_node('three')
    sub = rospy.Subscriber('count_up', Int32, cb) 
    pub = rospy.Publisher('twice', Int32, queue_size=1) 
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()
        
if __name__ == '__main__': 
    rospy.init_node('three')
    sub = rospy.Subscriber('count_up', Int32, cb) 
    pub = rospy.Publisher('three', Int32, queue_size=1) 
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(p)
        rate.sleep()
       
        
        
        
