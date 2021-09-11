#!/usr/bin/env python

import rospy, numpy
from std_msgs.msg import Float64

def movejoint():
	
    pub = rospy.Publisher('robotData', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
		id =numpy.array([2,0,1],dtype=numpy.float64)
		for x in id:
			rospy.loginfo(x)
			pub.publish(x)
			rate.sleep()

if __name__ == '__main__':
    try:
        movejoint()
    except rospy.ROSInterruptException:
        pass
