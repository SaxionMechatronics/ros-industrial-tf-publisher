# ros-industrial-tf-publisher
Small example to subscribe to and broadcast tf using python

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
