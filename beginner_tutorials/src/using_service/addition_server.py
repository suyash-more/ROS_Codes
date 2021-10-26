#!/usr/bin/env python
 
from beginner_tutorials.srv import custom_srv, custom_srvResponse
# from beginner_tutorials.msg import custom_msg
import rospy

def handle_add_two_ints(req):
    print("Returning {0}".format(req))
    return custom_srvResponse(req.A + req.B)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', custom_srv, handle_add_two_ints)
    print("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()