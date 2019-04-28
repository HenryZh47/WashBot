#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <tf/transform_listener.h>
#include <nav_msgs/Odometry.h>


int main(int argc, char** argv){
  ros::init(argc, argv, "robot_tf_publisher");
  ros::NodeHandle n;

  ros::Rate r(20);

  ros::Publisher odom_pub = n.advertise<nav_msgs::Odometry>("odom",1000);

  tf::TransformBroadcaster broadcaster;
  tf::TransformListener listener;
  tf::StampedTransform camera_frame;
  bool get_transform;

  while(n.ok()){
    

    tf::StampedTransform transform;
    tf::Quaternion q;
    try{
      listener.lookupTransform("map","camera_link",ros::Time(0),transform);
      double x = transform.getOrigin().x();
      double y = transform.getOrigin().y();
      double z = transform.getOrigin().z();
      double roll, pitch, yaw;
      double nx, ny, nz;
      double nroll, npitch, nyaw;
      q = transform.getRotation();
      tf::Matrix3x3 m(q);
      m.getRPY(roll, pitch, yaw);
      
      // change the x, y, z and row pitch yaw to new coordinates
      nx = -z;
      ny = y;
      nz = x;
      nyaw = -roll;
      nroll = 0;
      npitch = 0;
      tf::Quaternion nq = tf::createQuaternionFromRPY(nroll, npitch, nyaw);

      //publish odom from transform
      nav_msgs::Odometry odom;
      odom.header.stamp = ros::Time::now();
      odom.header.frame_id = "odom";
      odom.pose.pose.position.x = nx;
      odom.pose.pose.position.y = ny;
      odom.pose.pose.position.z = nz;
      geometry_msgs::Quaternion odom_quat = tf::createQuaternionMsgFromYaw(nyaw);
      odom.pose.pose.orientation = odom_quat;
      odom.child_frame_id = "base_link";
      odom_pub.publish(odom);

      // construct new transform
      tf::StampedTransform new_transform(tf::Transform(nq, tf::Vector3(nx-0.1, ny, nz)), ros::Time::now(), "map", "base_link");
      broadcaster.sendTransform(new_transform);
    } catch (tf::TransformException ex) {
    }





    //broadcaster.sendTransform(
    //  tf::StampedTransform(
    //    tf::Transform(tf::createQuaternionFromRPY(0,3.14159/2.0*3.0,0), tf::Vector3(0, 0, -.1)),
    //    ros::Time::now(),"camera_link", "base_link"));
    
    broadcaster.sendTransform(
      tf::StampedTransform(
        tf::Transform(tf::Quaternion(0, 0, 0, 1), tf::Vector3(0, 1, 0)),
        ros::Time::now(),"base_link", "odom"));


    r.sleep();
  }
}
