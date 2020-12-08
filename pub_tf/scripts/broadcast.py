#!/usr/bin/env python

import rospy

# Because of transformations
import tf_conversions
import tf2_ros
import geometry_msgs.msg

def broadcaster():
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(25)  # Rate in Hz

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    while not rospy.is_shutdown():
        rospy.loginfo("Publish tf ...")

        br = tf2_ros.TransformBroadcaster()

        transformStamped = geometry_msgs.msg.TransformStamped()

        transformStamped.header.stamp = rospy.Time.now()
        transformStamped.header.frame_id = "box"
        transformStamped.child_frame_id = "my_frame"

        transformStamped.transform.translation.x = 1.5
        transformStamped.transform.translation.y = 0
        transformStamped.transform.translation.z = 0

        quat = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)
        transformStamped.transform.rotation.x = quat[0]
        transformStamped.transform.rotation.y = quat[1]
        transformStamped.transform.rotation.z = quat[2]
        transformStamped.transform.rotation.w = quat[3]

        br.sendTransform(transformStamped)

        # Find out where it is in the world (in this case odom)
        try:
            trans = tfBuffer.lookup_transform("odom", 'my_frame', rospy.Time())

        except tf2_ros.LookupException as e:
            print(e)
            rate.sleep()
            continue

        except (tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rospy.loginfo("Connectivity Expception")
            rate.sleep()
            continue

        # It has succeeded
        rospy.loginfo("Found ..." + str(trans.transform.translation.x) + ", " +
                      str(trans.transform.translation.y))

        rate.sleep()

if __name__ == '__main__':
    try:
        broadcaster()
    except rospy.ROSInterruptException:
        pass