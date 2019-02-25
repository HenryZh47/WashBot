/*
 * Carnegie Mellon University
 * Washbot Project
 * Henry Zhang
 * Motor controll using rosserial and joystick
 */
#include <ros.h>
#include <std_msgs/Int16.h>

ros::NodeHandle nh;
int16_t rightVel = 0;
int16_t leftVel = 0;

int PUL1 = 5;  // pulse 
int DIR1 = 4;  // direction
int PUL2 = 7;
int DIR2 = 6;

void getRightVelCallback(const std_msgs::Int16& vel_msg) {
  rightVel = vel_msg.data;
  
  if (rightVel > 10) {
    digitalWrite(LED_BUILTIN, HIGH-digitalRead(LED_BUILTIN));
  }
  
}

void getLeftVelCallback(const std_msgs::Int16& vel_msg) {
  leftVel = vel_msg.data;
}

ros::Subscriber<std_msgs::Int16> rightVelSub("rightVel", &getRightVelCallback);

void setup() {
  // put your setup code here, to run once:
  pinMode(PUL1, OUTPUT);
  pinMode(PUL2, OUTPUT);
  pinMode(DIR1, OUTPUT);
  pinMode(DIR2, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  // init node and subcribe
  nh.initNode();
  nh.subscribe(rightVelSub);
}

void loop() {
  // put your main code here, to run repeatedly:
  // create rising edge
  digitalWrite(PUL1, HIGH);
  digitalWrite(PUL1, LOW);
  nh.spinOnce();

}
