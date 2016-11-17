#!/usr/bin/env python

import rospy
from std_msgs.msg import String

demo_bottle_sightings = ["yes","no","yes","yes","yes","no","yes","yes","yes","no","yes"]
idx = 0

pub = rospy.Publisher('vision_msg',String,queue_size=50)

def callback(data):
        global pub, demo_bottle_sightings, idx
        print "In vision, just got: %s"%data.data
        rospy.sleep(1)
        pub.publish(demo_bottle_sightings[idx])
        idx += 1
  
def main():

	rospy.init_node('vision_node', anonymous=True)
	rospy.Subscriber("alma_to_vision", String, callback)
	rospy.spin()

if __name__ == '__main__':
	main()
