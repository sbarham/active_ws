#!/usr/bin/env python

import time
import rospy
from std_msgs.msg import String

topics = ['vision_msg','language_msg','simulator_msg',
          'action_msg','alma_to_language','alma_to_vision',
          'alma_to_simulator','alma_to_action']

def print_callback(data):
        t = time.localtime()
        t_str = "%d:%d:%d:"%(t.tm_hour,t.tm_min,t.tm_sec)
        print "%s: msg: %s"%(t_str,data.data)
  
def main():
        global topics
        
	rospy.init_node('print_node', anonymous=True)

        for msg in topics:
                rospy.Subscriber(msg,String,print_callback)

	rospy.spin()

if __name__ == '__main__':
	main()
