#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

prev_data=None

def callback(data):
	global prev_data
	pub = rospy.Publisher('/robot/joint1_position_controller/command', Float64, queue_size=10)
	
	if prev_data is not None and data<prev_data:
		
		 pub.publish(data)
	prev_data=data
   
	
    
    
   
    	

def listener():
	
  
	
    rospy.init_node('listener', anonymous=True)
    
    rospy.Subscriber('robotData', Float64, callback)
    
    
    
    rospy.spin()

if __name__ == '__main__':
	
    listener()
