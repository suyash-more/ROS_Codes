#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


target = 1


def movebase_client():
    global target
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    if target == 1:
        goal.target_pose.pose.position.x = -9.1
        goal.target_pose.pose.position.y = -1.2
        goal.target_pose.pose.orientation.w = 0.5
    if target == 2:
        goal.target_pose.pose.position.x = 10.4 #10.4 works
        goal.target_pose.pose.position.y = 10.25 #10.2
        goal.target_pose.pose.orientation.w = 0.3 #0.7
    if target == 3:
        goal.target_pose.pose.position.x = 13.0
        goal.target_pose.pose.position.y = -1.6 #-1.5
        goal.target_pose.pose.orientation.w = 0.2 #-0.2
    if target == 4:
        goal.target_pose.pose.position.x = 18.2
        goal.target_pose.pose.position.y = -1.4
        goal.target_pose.pose.orientation.w = 0.2
    if target ==5:
        goal.target_pose.pose.position.x = -2
        goal.target_pose.pose.position.y = 4
        goal.target_pose.pose.orientation.w = 0.2

   
    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

if __name__ == '__main__':
    while target <=5:
        try:
            rospy.init_node('movebase_client_py')
            result = movebase_client()
            if result:
                rospy.loginfo("Goal execution done!")
                target += 1
        except rospy.ROSInterruptException:
            rospy.loginfo("Navigation test finished.")
