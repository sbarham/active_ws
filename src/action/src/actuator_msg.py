#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    print "data from vision: %s"%data.data

if __name__=="__main__":
    
    rospy.init_node('actuator_msg')
    pub = rospy.Publisher('actuator', String, queue_size=1)
    counter = 0
    rospy.Subscriber('vision_iter',String,callback)
    while not rospy.is_shutdown():
		hello_str = "HELLO from actuator (%d)!"%counter
                counter += 1
		pub.publish(hello_str)
		rospy.sleep(1.)
