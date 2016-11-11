#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def callback(s):
    global counter
    print "Received msg from language: " + s.data
    print "Apparently I saw a bottle ... or something."
    print "Anyway the demo worked."
    pub.publish("from lang_out: %d"%counter)
    counter += 1

counter = 0;
pub = rospy.Publisher('language_output',String)
rospy.init_node('language_output')
rospy.Subscriber('alma', String, callback)

rospy.spin()
