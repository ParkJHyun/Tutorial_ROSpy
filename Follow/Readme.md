# Follow

This chapter is detecting line and following lane.

Here, I use OpenCV in ROS, if you want using Opencv in ROS python, then you should include ***CV_Bridge***.

I use gazebo simulation ROBOTIS turtlebot3 autorace.

http://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#turtlebot3-autorace-2017-teaser

<img width="800" src="https://user-images.githubusercontent.com/35755034/44276715-46f9ed80-a283-11e8-9b14-c749224ac796.png">

## follower_line_edge.py

``` c
$ roslaunch turtlebot3_gazebo turtlebot3_autorace_mission.launch
$ roslaunch turtlebot3_gazebo turtlebot3_autorace.launch
$ ./follower_line_edge.py
```

Make ROI pixels, find ***yellow line*** and using ***Sobel*** edge, rising edge

First, get image and convert HSV then find yellow region in HSV make mask.

``` py
image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_yellow = numpy.array([ 20 ,100, 100])
upper_yellow = numpy.array([ 30, 255, 255])
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
```

Second, Make ROI pixel mask because of improve processing time so I use 40 height pixels and make binary image.

``` py
h, w, d = image.shape
search_top = 3*h/4
search_bot = search_top+40
mask[0:search_top, 0:w] = 0
mask[search_bot:h, 0:w] = 0
masked = cv2.bitwise_and(image, image, mask=mask)
```

Third, using Sobel edge (CV_8U), find rising edge.

'CV_8U' means I consider only positive pixel gradient that means rising edge is positive gradient so only rising edge.

``` py
sobelx = cv2.Sobel(mask,cv2.CV_8U,1,0,ksize=3)
```

## Result

Left image : image_raw, Right image : line_detect

<img width="400" src="https://user-images.githubusercontent.com/35755034/44276778-89232f00-a283-11e8-8f33-d1734cacf3fc.png">                                  <img width="400" src="https://user-images.githubusercontent.com/35755034/44276804-a0621c80-a283-11e8-9e14-004f93775ad8.png">
