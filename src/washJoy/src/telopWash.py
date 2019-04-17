#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16
from sensor_msgs.msg import Joy


# This ROS Node converts Joystick inputs from the joy node
# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Velocity commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed

def convertToInt(raw):
    result = int(raw/2*25)
    #if result < 0:
    #    result -= 50
    #else:
    #    result += 50
    return result


def callback(data):
    leftWheelVel = data.axes[1]
    rightWheelVel = data.axes[3]
    squirt = data.buttons[0]
    global lastSquirt
    if squirt > .5 and lastSquirt < .5:
       pubSquirt.publish(1)
    lastSquirt = squirt
    if abs(leftWheelVel) > -.1:
        pubLeft.publish(convertToInt(leftWheelVel))
    if abs(rightWheelVel) > -.1:
        pubRight.publish(convertToInt(rightWheelVel))

# Intializes everything
def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    rospy.init_node('Joy2Wash')
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
    # starts the node
    rospy.spin()

if __name__ == '__main__':
    start()
