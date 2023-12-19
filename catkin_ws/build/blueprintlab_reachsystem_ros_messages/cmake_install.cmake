# Install script for directory: /home/jiang/catkin_ws/src/blueprintlab_reachsystem_ros_messages

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/jiang/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/blueprintlab_reachsystem_ros_messages/msg" TYPE FILE FILES
    "/home/jiang/catkin_ws/src/blueprintlab_reachsystem_ros_messages/msg/single_float.msg"
    "/home/jiang/catkin_ws/src/blueprintlab_reachsystem_ros_messages/msg/single_int.msg"
    "/home/jiang/catkin_ws/src/blueprintlab_reachsystem_ros_messages/msg/generic.msg"
    "/home/jiang/catkin_ws/src/blueprintlab_reachsystem_ros_messages/msg/request_list.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/blueprintlab_reachsystem_ros_messages/cmake" TYPE FILE FILES "/home/jiang/catkin_ws/build/blueprintlab_reachsystem_ros_messages/catkin_generated/installspace/blueprintlab_reachsystem_ros_messages-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/jiang/catkin_ws/devel/include/blueprintlab_reachsystem_ros_messages")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/jiang/catkin_ws/devel/share/roseus/ros/blueprintlab_reachsystem_ros_messages")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/jiang/catkin_ws/devel/share/common-lisp/ros/blueprintlab_reachsystem_ros_messages")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/jiang/catkin_ws/devel/share/gennodejs/ros/blueprintlab_reachsystem_ros_messages")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/jiang/catkin_ws/devel/lib/python2.7/dist-packages/blueprintlab_reachsystem_ros_messages")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/jiang/catkin_ws/devel/lib/python2.7/dist-packages/blueprintlab_reachsystem_ros_messages")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/jiang/catkin_ws/build/blueprintlab_reachsystem_ros_messages/catkin_generated/installspace/blueprintlab_reachsystem_ros_messages.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/blueprintlab_reachsystem_ros_messages/cmake" TYPE FILE FILES "/home/jiang/catkin_ws/build/blueprintlab_reachsystem_ros_messages/catkin_generated/installspace/blueprintlab_reachsystem_ros_messages-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/blueprintlab_reachsystem_ros_messages/cmake" TYPE FILE FILES
    "/home/jiang/catkin_ws/build/blueprintlab_reachsystem_ros_messages/catkin_generated/installspace/blueprintlab_reachsystem_ros_messagesConfig.cmake"
    "/home/jiang/catkin_ws/build/blueprintlab_reachsystem_ros_messages/catkin_generated/installspace/blueprintlab_reachsystem_ros_messagesConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/blueprintlab_reachsystem_ros_messages" TYPE FILE FILES "/home/jiang/catkin_ws/src/blueprintlab_reachsystem_ros_messages/package.xml")
endif()

