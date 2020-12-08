# ros-industrial-tf-publisher
Small example to subscribe to and broadcast tf using Python. The node will broadcast a tf 1.5m in from of the head of the robot (`box` frame)

<img src="https://github.com/SaxionMechatronics/ros-industrial-tf-publisher/blob/main/pub_tf/images/without.png" width="400"> <img src="https://github.com/SaxionMechatronics/ros-industrial-tf-publisher/blob/main/pub_tf/images/with.png" width="400">

# Requirements
This code needs to run together with the urdf sim tutorial, which can be installed with

    $ sudo apt-get install ros-melodic-urdf-sim-tutorial
    
The simulation with the R2D2 robot can be started with:

    $ roslaunch urdf_sim_tutorial 13-diffdrive.launch
    
Once this is running, the publisher node can be started with

    $ rosrun pub_tf broadcast.py

The package must be build and source before it can be started.

    $ cd <workspace>
    $ catkin build
    $ source devel/setup.bash
