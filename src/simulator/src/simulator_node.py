#!/usr/bin/env python

import rospy
from std_msgs.msg import String

pub = rospy.Publisher('simulator_msg',String,queue_size=50)

def callback(data):
        global pub
        print "In simulator, just got: %s"%data.data
        rospy.sleep(1)
        pub.publish("hello alma, this is simulator")
        rospy.sleep(1)
        print "simulator exiting..."
        exit(1)
  
def main():

	rospy.init_node('simulator_node', anonymous=True)
	rospy.Subscriber("alma_to_simulator", String, callback)
	rospy.spin()

if __name__ == '__main__':
	main()
