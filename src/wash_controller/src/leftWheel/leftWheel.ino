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
// Left motor
#define DIR_L 4
#define STEP_L 5

BasicStepperDriver stepperL(MOTOR_STEPS, DIR_L, STEP_L);


ros::NodeHandle nh;
int16_t leftVel = 0;

SERV RPMserver (0,0);

int ledState = LOW;
const int ledPin =  8;


void getLeftVelCallback(const std_msgs::Int16& vel_msg) {
  RPMserver.leftRPM = vel_msg.data;
}

 
void motorCallback(const std_msgs::Int16& vel_msg) {
  stepperL.begin(abs(RPMserver.leftRPM), MICROSTEPS);
  int Ldir = -RPMserver.leftRPM/abs(RPMserver.leftRPM);
  stepperL.rotate(Ldir*abs(RPMserver.leftRPM/10*6));
}

void squirtCallback(const std_msgs::Int16& vel_msg) {
    if (ledState == LOW) {
      ledState = HIGH;
    } else {
      ledState = LOW;
    }
    digitalWrite(8, ledState);
}

ros::Subscriber<std_msgs::Int16> leftVelSub("leftVel", &getLeftVelCallback);
ros::Subscriber<std_msgs::Int16> rumMotorSub("rumMotors", &motorCallback);
ros::Subscriber<std_msgs::Int16> squirtSub("squirt", &squirtCallback);

void setup() {
  // init node and subcribe
  pinMode(8, OUTPUT);
  nh.initNode();
  nh.subscribe(leftVelSub);
  nh.subscribe(rumMotorSub);
  nh.subscribe(squirtSub);
}

void loop() {
  nh.spinOnce();
}
