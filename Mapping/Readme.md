# Map

## 1. map.yaml

YAML File of map named by 'map'.

``` py
image: map.pgm                                # this map is stored in 'map.pgm'
resolution: 0.050000                          # express world coordinates for cell scaled by 0.05cm^2 
origin: [-100.000000, -100.000000, 0.000000]  # origin is (-100, -100, 0)
negate: 0                                     # if negate is 1, occupied place is white, free is black
occupied_thresh: 0.65                         # over 65%, it is occupied
free_thresh: 0.196                            # below 19.6%, it is free
```

## 2. ROS bag

Tool that is recording messages and playig lately that.

It helps to seperate bugs and fix it, providing equivalent data repeat to algorithm.

=> It is useful when it debugging new algorithm.

It can develop algorithm not using always robot.


``` c
$ rosbag record (topic name)                          # rosbag record /scan /tf
$ rosbag record -O(--output-name) goo.bag /scan /tf   # save goo.bag 
$ rosbag record -o(--output-prefix) goo /scan /tf     # goo_2018-08-14-11-15-10.bag
$ rosbag record -a                                    # record all of published topic 
$ rosbag play --clock goo.bag                         # play a set of recorded message files 
			                                                # can set playtime or start point etc (wiki) 
# --clock is making rosbag pusblish clock time it is important to make a map                    
```

### Use it

<img width="400" src="https://user-images.githubusercontent.com/35755034/44071998-4a692f08-9fc7-11e8-9092-8cdf386a3e10.png"><img width="450" img height="400" src="https://user-images.githubusercontent.com/35755034/44072019-75eb3f68-9fc7-11e8-9843-aa5d6943eedc.png">

``` c
$ roslaunch turtlebot_stage turtlebot_in_stage.launch
$ roslaunch turtlebot_teleop keyboard_teleop.launch
$ rosbag record -O data.bag /scan /tf
```

* If have any problem about STAGE FILE, 

``` c
$ sudo apt-get install ros-kinetic-turtlebot-stage
$ export TURTLEBOT_STAGE_MAP_FILE=/opt/ros/kinetic/share/turtlebot_stage/maps/stage/maze.world
``` 
and then reboot.

For using ***slam_gmapping***

``` c
$ roscore
$ rosparam set use_sim_time true
$ rosrun gmapping slam_gmapping
$ rosbag play --clock data.bag
// ..... if all done ....
$ rosrun map_server map_saver
```
### my result

<img width="400" src="https://user-images.githubusercontent.com/35755034/44072237-8bc28250-9fc8-11e8-90b9-2b84dff380f3.png">
