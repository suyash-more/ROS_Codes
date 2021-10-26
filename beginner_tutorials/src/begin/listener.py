#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from beginner_tutorials.msg import custom_msg

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
    
def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("custom_topic", custom_msg, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()


# to run the nodes 
# rosrun {package_name} {node file name}