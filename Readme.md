# Tutorial_ROSpy

This is ROS basic Tutorial with **python** 

I referenced this book http://www.yes24.com/24/goods/37617833

Before You start, Please ready for below operation

- Have labtop with Ubuntu 16.04(LTS) and installed ROS Kinetic 

``` c
  $ mkdir catkin_ws && cd src
```

First, make workspace in catkin_ws

``` c
  $ catkin_create_pkg Tutorial rospy std_msgs
```

Second, make **Tutorial** package with depend package rospy, std_msgs 

``` c
  $ cd Tutorial/script
  $ chmod u+x publish_node.py subscribe_node.py
```

Third, change permit publish_node.py and subscriber_node.py

``` c
  $ cd catkin_ws && catkin_make
```

``` c
  $ rospack profile
```

``` c
  $ roscore
  $ rosrun Tutorial publish_node.py (another terminal)
  $ rosrun Tutorial subscribe_node.py (another terminal)
```
