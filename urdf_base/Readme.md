# URDF_Tutorial

## 1. URDF 만들기

``` c
  $ cd ~/catkin_ws/src
  $ catkin_create_pkg (package_name) urdf
  $ cd (package_name) && mkdir urdf
  $ cd urdf
  $ sudo atom (urdf_name).urdf
```
※ atom이 아닌 다른 편집 tool 가능

## 2. URDF 작성

``` xml
  <material name="black">
    <color rgba="0 0 0 1"/>
  </material>
  <material name="yellow">
    <color rgba="1 0.7 0 0.8"/>
  </material>
```
<material>을 통해 색깔 지정(RGBA)

``` xml
  <link name="base_link">
    <visual>
      <geometry>
        <cylinder length="0.3" radius="0.7"/>
        </geometry>
        <material name="yellow"/>
    </visual>
  </link>
```
link(**'base_link'**)에 대한 특성 지정

  - 해당 link의 이름은 "base_link"
  
  - 원기둥의 형태이며, 높이는 0.3 크기, 0.7 크기의 반지름을 가지고 있음
  
  - 위에서 정한 material 중 'yellow'를 선택 즉, 원기둥의 색깔은 노란색으로 지정
  
## 3. URDF Check

``` c
  $ check_urdf (urdf_name).urdf
```
만들어진 urdf 내용이 올바르게 되어 있는 지 체크할 수 있음

해당 bash shell에서 urdf와 관련된 것들을 결과로 확인 가능

**Option**

``` c
 $ urdf_to_graphiz (urdf_name).urdf
```
urdf 블록선도를 pdf로 생성하여 확인할 수 있음

## 4. Make Launch file
``` c
  $ cd ~/catkin_ws/src/(package_name)
  $ mkdir launch && cd launch
  $ sudo atom (launch_name).launch
```
※ atom이 아닌 다른 편집 tool 가능

``` xml
<launch>
	<arg name="model" default="$(find urdf_base)/urdf/cylinder.urdf" />
	<arg name="gui" default="True" />
	<param name="robot_description" textfile="$(arg model)" />
	<param name="use_gui" value="$(arg gui)" />
	<node name="joint_state_publisher" pkg="joint_state_publisher" type="joint_state_publisher"/>
	<node name="robot_state_publisher" pkg="robot_state_publisher" type="state_publisher" />
</launch>
```
launch 파일 내용은 아래와 같음
  - 실행 시킬 urdf 파일(model)에 대한 경로 설정 
  - GUI 설정
  - Rviz에서 받을 "robot_description" 설정
  - "joint_state_publisher"와 "robot_state_publisher"의 노드를 통해 시뮬레이션 상에서 상태를 조정할 수 있게 함
  
## 5. Build and Run

``` c
  $ cd ~/catkin_ws/ && catkin_make
  $ rospack profile
```
빌드가 성공적으로 종료되면 

``` c
  $ roslaunch (package_name) (launch_name).launch
```
작성하였던 launch 파일 실행

``` c
  $ rosrun rviz rviz
```
Rviz 실행

## 6. Rviz

실행된 Rviz 상에서 

1. 'Add' 버튼 클릭

2. 'RobotModel' 선택

3. 'FixedFrame' 설정

여기에서 FixedFrame은 'base_link'이므로 base_link로 선택함

