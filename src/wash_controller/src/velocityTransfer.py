#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed

def convertToInt(raw):
    result = int(raw/25*200)
    #if 0 < result < 2:
#	result = 2
    #    result -= 50
    #else:
    #    result += 50
    return result


def callback(data):
    leftWheelVel = data.axes[3]
    rightWheelVel = data.axes[1]
    squirt = data.buttons[0]
    global lastSquirt
    if squirt > .5 and lastSquirt < .5:
       pubSquirt.publish(1)
    lastSquirt = squirt
    #if abs(leftWheelVel) > -.1:
        #pubLeft.publish(convertToInt(leftWheelVel))
    #if abs(rightWheelVel) > -.1:
        #pubRight.publish(convertToInt(rightWheelVel))


def TransferVelocity(data):
    wheel_distance = 0.53
    velocity = data.linear.x
    rotation = data.angular.z
    #right_speed = (rotation*wheel_distance)/2+velocity
    #left_speed = velocity*2 - right_speed
    left_speed =  (rotation*wheel_distance)/2+velocity
    right_speed = velocity*2 - left_speed
    if(abs(left_speed)<0.05):
        left_speed = 0;
    if(abs(right_speed)<0.05):
        right_speed = 0;
    #global lastSquirt
    #if squirt > .5 and lastSquirt < .5:
       #pubSquirt.publish(1)
    #lastSquirt = squirt
    if abs(left_speed) > -.1:
        pubLeft.publish(convertToInt(left_speed))
    if abs(right_speed) > -.1:
        pubRight.publish(convertToInt(right_speed))


# Intializes everything
def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    rospy.init_node('vel2wash')
    global pubLeft
    global pubRight
    global pubSquirt
    global lastSquirt 
    lastSquirt = 0
    pubLeft = rospy.Publisher('leftVel', Int16)
    pubRight = rospy.Publisher('rightVel', Int16)
    pubSquirt = rospy.Publisher('squirt', Int16)

    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    rospy.Subscriber("cmd_vel",Twist,TransferVelocity)
    # starts the node
    rospy.spin()

if __name__ == '__main__':
    start()
