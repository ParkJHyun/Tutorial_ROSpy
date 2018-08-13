# Key_Twist

This tutorial is that inputs which is from keyboard change Twist message outputs

## 1. Key_publish.py

wait for keyboard input and generate std_msgs/String of ***'keys'*** topic.

``` py
termios.tcgetattr(sys.stdin) # set structure member from sys.stdin
```

``` py
tty.setcbreak(sys.stdin.fileno()) # convert file descriptor 'fd' into cbreak
```

위의 2개의 코드는 키보드를 누르자 마자 곧바로 프로그램의 표준 입력 스트림으로 키를 받게 하기 위해 설정

``` py
select.select([sys.stdin], [], [], 0)[0] == [sys.stdin] # polling continually stdin stream.
# set timeout to 0, calling select(0) immediately can return
```

``` py
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_attr) # convert console mode into standard mode 
```

## 2. Keys_to_Twist.py

Workout generator, generate workout if it receive keyboard input for move of robot.

``` py
key_mapping = {'w': [0,1], 'x': [0, -1], 'a': [-1, 0], 'd': [1, 0], 's': [0, 0]} # python dictionary, correspond key input with target move
```

``` py
if len(msg.data) == 0 or not key_mapping.has_key(msg.data[0]): 
  return 
vels = key_mapping[msg.data[0]] # if have continuous key input stream, it operate for generating Twist message for robot
```
## 3. key_to_Twist_rosrate.py

Repeat last command if it doesn't any input.

Get constant results through ROS rate structure which estimates time for executing repetitive statement.

``` c
$ rostopic hz 'message' # compute rate of average message generates per second and print estimates 
                        # rostopic hz cmd_vel
```

``` py
rate = rospy.Rate(10)  # consistently 10Hz
g_last_twist = Twist()
while not rospy.is_shutdown():
  twist_pub.publish(g_last_twist) # continue to publish 
  rate.sleep()
```

## Visualizaion Tool, ***'rqt_plot'***

before it starts

``` c
$ rostopic echo 'message' # can identify information of published message
$ rostopic info 'message' # rostopic info cmd_vel
$ rosmsg show             # rosmsg show geometry_msgs/Twist
```
find messages which you want to visualize

and then

``` c
$ rqt_plot message # rqt_plot cmd_vel/linear/x cmd_vel/angular/z
```
<img width="1000" src="https://user-images.githubusercontent.com/35755034/44014325-4fabc906-9f06-11e8-97f2-f98cfa148b16.png">