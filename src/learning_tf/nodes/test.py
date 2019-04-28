#!/usr/bin/env python  
import rospy

import math
import tf2_ros
import geometry_msgs.msg

if __name__ == '__main__':
    rospy.init_node('tf2_turtle_listener')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    br = tf2_ros.TransformBroadcaster()

    t_camera_base = geometry_msgs.msg.TransformStamped()
    t_camera_base.header.stamp = rospy.Time(0)
    t_camera_base.header.frame_id = "camera_link_copy"
    t_camera_base.child_frame_id = "base_link"
    t_camera_base.transform.translation.x = -0.4
    t_camera_base.transform.translation.y = 0.0
    t_camera_base.transform.translation.z = 0.0
    # q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
    t_camera_base.transform.rotation.x = 0.0
    t_camera_base.transform.rotation.y = 0.0
    t_camera_base.transform.rotation.z = 0.0
    t_camera_base.transform.rotation.w = 1.0

    t_base_odom = geometry_msgs.msg.TransformStamped()
    t_base_odom.header.stamp = rospy.Time(0)
    t_base_odom.header.frame_id = "base_link"
    t_base_odom.child_frame_id = "odom"
    t_base_odom.transform.translation.x = 0.0
    t_base_odom.transform.translation.y = 0.0
    t_base_odom.transform.translation.z = 0.0
    # q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
    t_base_odom.transform.rotation.x = 0.0
    t_base_odom.transform.rotation.y = 0.0
    t_base_odom.transform.rotation.z = 0.0
    t_base_odom.transform.rotation.w = 1.0

    t_map_camera = geometry_msgs.msg.TransformStamped()
    t_map_camera.header.stamp = rospy.Time(0)
    t_map_camera.header.frame_id = "map_copy"
    t_map_camera.child_frame_id = "camera_link_copy"
    t_map_camera.transform.translation.x = 0.0
    t_map_camera.transform.translation.y = 0.0
    t_map_camera.transform.translation.z = 0.0
    # q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
    t_map_camera.transform.rotation.x = 0.0
    t_map_camera.transform.rotation.y = 0.0
    t_map_camera.transform.rotation.z = 0.0
    t_map_camera.transform.rotation.w = 1.0


    t_map = geometry_msgs.msg.TransformStamped()
    t_map.header.stamp = rospy.Time(0)
    t_map.header.frame_id = "map"
    t_map.child_frame_id = "base_link"
    t_map.transform.translation.x = 0.0
    t_map.transform.translation.y = 0.0
    t_map.transform.translation.z = 0.0
    # q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
    t_map.transform.rotation.x = 0.0
    t_map.transform.rotation.y = 0.0
    t_map.transform.rotation.z = 0.0
    t_map.transform.rotation.w = 1.0




    #br.sendTransform(t_camera_base)
    #br.sendTransform(t_base_odom)
    #br.sendTransform(t_map)




    
    rate = rospy.Rate(30.0)
    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform('map', 'camera_link', rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue
        t_map_camera = trans;
        t_map_camera.header.frame_id = "map_copy"
        t_map_camera.child_frame_id = "camera_link_copy"
        t_map_camera.header.stamp = rospy.Time(0)
        t_base_odom.header.stamp = rospy.Time(0)
        t_camera_base.header.stamp = rospy.Time(0)
        t_map.header.stamp = rospy.Time(0)


        #br.sendTransform(t_camera_base)
        #br.sendTransform(t_base_odom)
        #br.sendTransform(t_map_camera)
        br.sendTransform(t_map)
        rate.sleep()
