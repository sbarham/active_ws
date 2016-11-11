#!/usr/bin/env python

# import config
# temporary
language_topic_name = "language_input_msg"
# temporary



import rospy
from std_msgs.msg import String

#print config.language_topic_name
#print "success!!"

pub = rospy.Publisher(language_topic_name, String)
rospy.init_node("language_input")

input = ""

while True:
    input = raw_input("Say something to ROS: ")
    if input == "exit":
        break
    pub.publish(input)


    
