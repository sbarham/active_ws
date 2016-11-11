#!/usr/bin/env python

import rospy
from std_msgs.msg import String

pub = rospy.Publisher('action_msg',String)

def callback(data):
        global pub
#	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        print "In actuator listener, just got: %s"%data.data
        rospy.sleep(1)
        pub.publish("hello alma, this is action")
        rospy.sleep(1)
        print "exiting action..."
        exit(1)
  
def listener():

# In ROS, nodes are uniquely named. If two nodes with the same
# node are launched, the previous one is kicked off. The
# anonymous=True flag means that rospy will choose a unique
# name for our 'listener' node so that multiple listeners can
# run simultaneously.
	rospy.init_node('actuator_listener', anonymous=True)

	rospy.Subscriber("alma_to_action", String, callback)

	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
	listener()
