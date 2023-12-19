# ROS for the Reach5Mini

BlueprintLab ROS packages for interfacing with the Reach5Mini products via ROS.

## File Structure Overview

* **R5M_Examples (repository main directory):**  
    * **src/blueprintlab_reachsystem_ros_messages（必需）:** 用于存储 ROS 消息类型的 ROS 包
    * **src/reach5mini_ros_passthrough (required):** 用于R5M 数据传输的底层 ROS 到串行直通脚本。主要脚本: `scripts/r5m_passthrough.py`
    * **src/Examples/keyboard_r5m_test:** 使用键盘作为输入来控制 Reach 5 Mini (R5M) 上关节的包. Main script: `scripts/keyboard_r5m.py`
    * **src/Examples/r5m_ros_controller:** 高端控制接口，用于向 R5M ROS 主题发送命令并从 R5M ROS 主题接收数据. Main script: `scripts/r5m_control.py`
    * **src/ILoSA-main:**为训练机械臂轨迹各个节点，和预测轨迹各个几点`gp.py`
    * **src/blueprintlab_reachsystem_ros_messages:**为对于收到外界阻力干扰后，机械臂关机角度回发生偏差，其功能为纠正回机械臂轨迹经过预测后的轨迹`scripts/tidai.py`


## Installation
要在此存储库中安装必要的组件，请按照以下步骤操作。

### Top Side Installation 
**Ubuntu 18.04 (or Linux equivalent) top side** Ubuntu 18.04（或 Linux 等效版本）顶部如果使用 Ubuntu 16.04（或 Linux 等效版本），应该类似，但使用apt-get代替。

安装Python3和依赖项。
```bash
sudo apt update
sudo apt install python3-dev python3-setuptools python3-pip python3-yaml
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install pyserial numpy 
```


#### Enable Python3 support for ROS
```bash
sudo pip3 install rospkg catkin_pkg
```

#### Workspace setup and compilation

To install the components from this git repository, follow the below steps to create the workspace and install:
```bash
cd ~
mkdir catkin_ws/src
```
Copy the ROS packages from this repository to the `~/catkin_ws/src/` folder. Then follow the below commands:
```bash
cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash
```
Note: You must source the file via the command `source ~/catkin_ws/devel/setup.bash` everytime you open a new terminal. You can make this permanent by adding the line to your `~/.bashrc` config file via command `echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc`

Now the installation is complete.




## Usage

### ROS消息类型和用途

ROS 包blueprintlab_reachsystem_ros_messages包含所有要使用的 ROS 消息类型。要在节点之间通过 ROS 进行通信，您必须将此包导入到 ROS 节点中。

每条消息都有一个遵循约定的样式：1 个时间戳容器（ROS“时间”数据类型）、1 个 device_id 容器（“uint8”数据类型）和 1 个或多个值/数据容器。

目前的消息类型如下：

* **single_float.msg** （通过 python 导入from blueprintlab_reachsystem_ros_messages.msg import single_float）：消息有一个“float32”类型。目前用于处理packet_ids：POSITION、VELOCITY、CURRENT、OPENLOOP.
* **single_int.msg** （通过 python 导入from blueprintlab_reachsystem_ros_messages.msg import single_int）：消息具有单个“int32”类型。目前用于处理packet_ids：MODE。
request_list.msg（通过 python 导入from blueprintlab_reachsystem_ros_messages.msg import request_list）：消息具有未定义长度的“int32[]”数组类型。目前用于处理数据包请求列表。
* **generic.msg** （通过 python 导入from blueprintlab_reachsystem_ros_messages.msg import generic）：消息有一个类型为“uint8”的 packet_id 容器，以及一个用于存储值的未定义长度“float32[]”数组类型。如果 packet_id 应该传输“int”而不是“float”，那么在 ROS 系统上传输时必须将其转换为“float”，并在另一端转换回“int”。当前用于处理不在先前消息列表中的任何其他 packet_id。

The timestamp should be updated everytime you are about to publish the message, which could be used to track latency in the system.


### Current packages and scripts


#### blueprintlab_reachsystem_ros_messages 
用于存储 ROS 消息类型的 ROS 包。必须编译并安装才能使用 BlueprintLab 中的任何其他软件包。如何运行：仅消息容器。不作为节点运行。

#### reach5mini_ros_passthrough 
用于 R5M 数据传输的底层 ROS 到串行直通脚本。主脚本：`scripts/r5m_passthrough.py` 如何运行：
How to run: 

1. 通过rosrun：rosrun reach5mini_ros_passthrough r5m_passthrough.py <args>。 <args>是一个可选参数，设计用于运行包的不同实例。<args>包含2个参数：R5M实例号和串口地址。 is 的用法示例rosrun reach5mini_ros_passthrough r5m_passthrough.py 0 /dev/ttyUSB0。如果没有<args>，实例编号默认为 0，端口默认为/dev/ttyUSB0。

2. 通过roslaunch：roslaunch reach5mini_ros_passthrough run_reach5mini_passthrough.launch。这是使用 location 处的启动文件reach5mini_ros_passthrough/launch/run_reach5mini_passthrough.launch。这旨在以reach5mini_ros_passthrough与上述 (rosrun) 示例相同的格式启动具有预设用户参数的多个实例。编辑文件以更改默认值或启用该包的多个实例的运行。

#### keyboard_r5m_test 
使用键盘作为输入来控制 R5M 上关节的软件包。主脚本：scripts/keyboard_r5m.py 如何运行：rosrun keyboard_r5m_test keyboard_r5m.py

#### r5m_ros_controller 
这是顶部控制脚本的模板。用户可以对其进行克隆和修改。它设计用于向 R5M ROS 主题发送命令或请求以及从 R5M ROS 主题接收数据。主脚本：scripts/r5m_control.py 如何运行：


How to run:

1. 通过rosrun：rosrun r5m_ros_controller r5m_control.py <args>。 <args>是一个可选参数，设计用于运行包的不同实例。<args>包含1个参数：R5M实例号。 is 的用法示例rosrun reach5mini_ros_passthrough r5m_passthrough.py 0。如果没有<args>，实例编号默认为 0。

2. 通过roslaunch：roslaunch r5m_ros_controller run_reach5mini_control.launch。这是使用 location 处的启动文件r5m_ros_controller/launch/run_reach5mini_control.launch。这旨在以r5m_ros_controller与上述 (rosrun) 示例相同的格式启动具有预设用户参数的多个实例。编辑文件以更改默认值或启用该包的多个实例的运行。
#### gp.py
1. 为通过各个关节的id，按键所需要的时间，和角速度为输入，输出为各个关节的id，当前关节上一个位置角度，和当前关节的角度为输出进行训练最，按键盘e为停止数据的输入，并开始高斯过程机械臂轨迹的训练和预测 
#### tidai.py
1. 为通过高斯过程轨迹预测之后，订阅其服务，将预测的的位置和当前轨迹复现的位置逐一对比，如果相同则进行下一关节的运动，如果不同则进行纠正。