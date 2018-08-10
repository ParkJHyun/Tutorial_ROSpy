# Cockroach in Gazebo

## Snapshot 

----------

<img width="600" src="https://user-images.githubusercontent.com/35755034/43958009-d14ae1f0-9ce4-11e8-8d1f-61a3bb783199.jpg">

----------

# Before you start

## This is running turtlebot in Gazebo

first you must install turtlebot-gazebo

```c
$ sudo apt-get update
```

In this book, It says that about 'indigo' but, my ROS version is ***'kinetic'***. 

So note that what yours version

```c
$ sudo apt-get install ros-kinetic-turtlebot-gazebo
```

```c
$ roslaunch turtlebot_gazebo turtlebot_world.launch
```

If you have some problem which is like ***'no world file'***, then you write it in shell script

```c
$ export TURTLEBOT_GAZEBO_WORLD_FILE=/opt/ros/kinetic/share/turtlebot_gazebo/worlds/playground.world
```

At another command,   

```c
$ cd ~/cockroach_ws/src/cockroach/src
```

```c
cockroach/src $ ./cockroach.py
```

and in this book, I think it has some mistake in python code so I modify some code.
