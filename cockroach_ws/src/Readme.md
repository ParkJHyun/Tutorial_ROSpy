# Cockroach in Gazebo


# Before you start

## This is running turtlebot in Gazebo

first you must install turtlebot-gazebo

```c
$ sudo apt-get update
```

In this book, It says that about 'indigo' but, my ROS version is 'kinetic'. 

So note that what yours version

```c
$ sudo apt-get install ros-kinetic-turtlebot-gazebo
```

```c
$ roslaunch turtlebot_gazebo turtlebot_world.launch
```

IF you have some problem which is like 'no world file', then you write it in shell script

```c
$ export TURTLEBOT_GAZEBO_WORLD_FILE=/opt/ros/kinetic/share/turtlebot_gazebo/worlds/playground.world
```

and in this book, I think it has some mistake in python code so I modify some code.
