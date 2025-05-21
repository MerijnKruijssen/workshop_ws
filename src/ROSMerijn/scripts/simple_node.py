#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    # Initialiseer de ROS-node
    rospy.init_node('mijn_ros_node', anonymous=True)

    # Maak een publisher die berichten zal publiceren naar het topic "chatter"
    pub = rospy.Publisher('chatter', String, queue_size=10)

    # Stel de rate in op 1 Hz (1 bericht per seconde)
    rate = rospy.Rate(1)

    # Het programma blijft berichten publiceren totdat het wordt afgesloten
    while not rospy.is_shutdown():
        msg = "Hallo, ROS! Het is " + str(rospy.get_time())  # Het bericht
        rospy.loginfo(msg)  # Log het bericht naar de console
        pub.publish(msg)  # Publiceer het bericht naar het topic "chatter"
        rate.sleep()  # Wacht totdat het tijd is voor het volgende bericht

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
