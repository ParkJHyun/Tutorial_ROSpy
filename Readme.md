# Tutorial_ROSpy

## 1Day

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
## 2Day

Add complex message 'Complex.msg' containing

``` c
  float32 real
  float32 imaginary
```

in msg directory

Change **package.xml**

``` c
  <build_depend>message_generation</build_depend>
  <exec_depend>message_runtime</exec_depend>
```

and **CMakeList.txt**
``` c
  find_package(catkin REQUIRED COMPONENTS
    rospy
    std_msgs
    message_generation
 )
```

``` c
  catkin_package(
    CATKIN_DEPENDS message_runtime
    ...(something else)
 )
```

``` c
  add_message_files(
    FILES
    Complex.msg
 )
```


``` c
  generate_message(
    DEPENDENCIES
    std_msgs
 )
```

Then you can generate it like 1Day

**Publisher** is 'complex_pub.py'

**Subscriber** is 'complex_sub.py'
