#!/usr/bin/env python

import rospy
from std_msgs.msg import String

pub = []
counter = [0,0,0,0]

def language_callback(data):
        global pub, counter
        print "In alma, just got: %s"%data.data
        rospy.sleep(5)
        pub[1].publish("vision, your turn")
        counter[0] += 1


def vision_callback(data):
        global pub, counter
        print "In alma, just got: %s"%data.data
        rospy.sleep(5)
        pub[2].publish("simulator, your turn")
        counter[1] += 1

def simulator_callback(data):
        global pub, counter
        print "In alma, just got: %s"%data.data
        rospy.sleep(5)
        pub[3].publish("action, your turn")
        counter[2] += 1


def action_callback(data):
        global pub, counter
        print "In alma, just got: %s"%data.data
        rospy.sleep(5)
        pub[0].publish("language, we're done")
        counter[3] += 1
  
def main():
        global pub

# In ROS, nodes are uniquely named. If two nodes with the same
# node are launched, the previous one is kicked off. The
# anonymous=True flag means that rospy will choose a unique
# name for our 'listener' node so that multiple listeners can
# run simultaneously.
	rospy.init_node('alma_node', anonymous=True)

	rospy.Subscriber("vision_msg", String, vision_callback)
        rospy.Subscriber("language_msg", String, language_callback)
        rospy.Subscriber("simulator_msg", String, simulator_callback)
        rospy.Subscriber("action_msg", String, action_callback)

        pub.append(rospy.Publisher("alma_to_language", String, queue_size=50))
        pub.append(rospy.Publisher("alma_to_vision", String, queue_size=50))
        pub.append(rospy.Publisher("alma_to_simulator", String, queue_size=50))
        pub.append(rospy.Publisher("alma_to_action", String, queue_size=50))

        print pub
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
	main()
