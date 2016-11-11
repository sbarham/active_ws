#!/usr/bin/env python

import rospy
from std_msgs.msg import String

pub = rospy.Publisher('vision_msg',String,queue_size=50)

def callback(data):
        global pub
        print "In vision, just got: %s"%data.data
        rospy.sleep(1)
        pub.publish("hello alma, this is vision")
        rospy.sleep(1)
        print "vision exiting..."
        exit(1)
  
def main():

	rospy.init_node('vision_node', anonymous=True)
	rospy.Subscriber("alma_to_vision", String, callback)
	rospy.spin()

if __name__ == '__main__':
	main()
