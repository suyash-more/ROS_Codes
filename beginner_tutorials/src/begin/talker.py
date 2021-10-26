#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from beginner_tutorials.msg import custom_msg


def talker():
    pub = rospy.Publisher('custom_topic', custom_msg, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    custom_msg_obj = custom_msg()
    while not rospy.is_shutdown():
        custom_msg_obj.A = 10
        custom_msg_obj.B = 20

        rospy.loginfo(custom_msg_obj)
        pub.publish(custom_msg_obj)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass