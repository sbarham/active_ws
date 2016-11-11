#!/usr/bin/env python

###################
# imports go here #
###################

import rospy
# temporary / import config
alma_topic_name = "alma"
language_input_topic_name = "language_input"
# /temporary
from std_msgs.msg import String


###################
# methods go here #
###################

def publish(s):
    alma_topic.publish(s)

def process_language(msg):
    # pretend to process the language ...
    # everything parses to "hello"
    publish("msg from language input: %s\n"%msg.data)
    

def callback(data):
    print "language resceived msg from alma: %s"%data.data
    print "language is exiting..."
    rospy.sleep(1)
    exit(1)

##########################
# top-level code follows #
##########################

# instantiate the topic(s)
alma_topic = rospy.Publisher("language_msg", String)
rospy.Subscriber("language_input_msg", String, process_language)
rospy.Subscriber('alma_to_language', String, callback)
rospy.init_node('language_node')

rospy.spin()
