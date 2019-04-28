#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')
import rospy
import math
import tf
import geometry_msgs.msg


if __name__ == '__main__':
    rospy.init_node('tf_listener_broadcaster')
    listener = tf.TransformListener()
    br = tf.TransformBroadcaster()
    #ti = listener.getLatestCommonTime("map","camera_link")
    listener.waitForTransform("map","camera_link",rospy.Time(), rospy.Duration(4.0))
    trans,rot = listener.lookupTransform('map', 'camera_link', rospy.Time(0))
    #t = geometry_msgs.msg.TransformStamped()
    #t.header.stamp = rospy.Time.now()
    #t.header.frame_id = "map"
    #t.child_frame_id = "base_link"
    x = trans[0]-0.4;
    y = trans[1]
    z = trans[2];
    rx = rot[0];
    ry = rot[1];
    rz = rot[2];
    rw = rot[3];
    rate = rospy.Rate(30)

  

    rate = rospy.Rate(30)


    while( not rospy.is_shutdown()):
        rate.sleep()
        br.sendTransform((0.0,0.0,0.0),(0.0,0.0,0.0,1.0), rospy.Time.now(),'base_link','odom')
       
        trans,rot = listener.lookupTransform('map', 'camera_link', rospy.Time(0))
        x = trans[0]-0.4;
        y = trans[1];
        z = trans[2];
        rx = rot[0];
        ry = rot[1];
        rz = rot[2];
        rw = rot[3];
        br.sendTransform((x,y,z),(rx,ry,rz,rw),rospy.Time.now(),"map","base_link")
        br.sendTransform((x+0.4,y,z),(rx,ry,rz,rw),rospy.Time.now(),"map","camera_link")

           
    
    #rospy.spin()
