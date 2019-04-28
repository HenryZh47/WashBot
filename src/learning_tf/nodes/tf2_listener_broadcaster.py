#/usr/bin/env python  
import rospy

import math
import tf2_ros
import geometry_msgs.msg
from nav_msgs.msg import Odometry

if __name__ == '__main__':
    rospy.init_node('tf2_listener')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    br = tf2_ros.TransformBroadcaster()
    pub = rospy.Publisher("odom",nav_msgs.Odometry,quwuw_size = 1000)


  




    
    rate = rospy.Rate(15.0)
    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform('map', 'base_link', rospy.Time(0))
            od = Odometry()
            od.pose.pose.x = trans.transform.translation.x
            od.pose.pose.y = trans.transform.translation.y
            od.pose.pose.z = trans.transform.translation.z
            pub.publish(od)
            
            
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue
        rate.sleep()
