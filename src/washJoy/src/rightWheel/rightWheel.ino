/*
 * Carnegie Mellon University
 * Washbot Project
 * Hans Kumar and Henry Zhang
 * Motor controll using rosserial and joystick
 */
#include <ros.h>
#include <std_msgs/Int16.h>
#include <Arduino.h>
#include "BasicStepperDriver.h"
#include "MultiDriver.h"
#include "SyncDriver.h"
#include "SERV.h"

#define MICROSTEPS 128
#define MOTOR_STEPS 200
// Right Motor
#define DIR_R 6
#define STEP_R 7

BasicStepperDriver stepperR(MOTOR_STEPS, DIR_R, STEP_R);


ros::NodeHandle nh;
int16_t leftVel = 0;

SERV RPMserver (0,0);


void getRightVelCallback(const std_msgs::Int16& vel_msg) {
  RPMserver.rightRPM = vel_msg.data;
}

 
void motorCallback(const std_msgs::Int16& vel_msg) {
  stepperR.begin(abs(RPMserver.rightRPM), MICROSTEPS);
  int Rdir = RPMserver.rightRPM/abs(RPMserver.rightRPM);
  stepperR.rotate(Rdir*abs(RPMserver.rightRPM/10*6));
}

ros::Subscriber<std_msgs::Int16> rightVelSub("rightVel", &getRightVelCallback);
ros::Subscriber<std_msgs::Int16> rumMotorSub("rumMotors", &motorCallback);

void setup() {
  // init node and subcribe
  nh.initNode();
  nh.subscribe(rightVelSub);
  nh.subscribe(rumMotorSub);
}

void loop() {
  nh.spinOnce();
}
