;; Auto-generated. Do not edit!


(when (boundp 'blueprintlab_reachsystem_ros_messages::single_int)
  (if (not (find-package "BLUEPRINTLAB_REACHSYSTEM_ROS_MESSAGES"))
    (make-package "BLUEPRINTLAB_REACHSYSTEM_ROS_MESSAGES"))
  (shadow 'single_int (find-package "BLUEPRINTLAB_REACHSYSTEM_ROS_MESSAGES")))
(unless (find-package "BLUEPRINTLAB_REACHSYSTEM_ROS_MESSAGES::SINGLE_INT")
  (make-package "BLUEPRINTLAB_REACHSYSTEM_ROS_MESSAGES::SINGLE_INT"))

(in-package "ROS")
;;//! \htmlinclude single_int.msg.html


(defclass blueprintlab_reachsystem_ros_messages::single_int
  :super ros::object
  :slots (_stamp _device_id _value ))

(defmethod blueprintlab_reachsystem_ros_messages::single_int
  (:init
   (&key
    ((:stamp __stamp) (instance ros::time :init))
    ((:device_id __device_id) 0)
    ((:value __value) 0)
    )
   (send-super :init)
   (setq _stamp __stamp)
   (setq _device_id (round __device_id))
   (setq _value (round __value))
   self)
  (:stamp
   (&optional __stamp)
   (if __stamp (setq _stamp __stamp)) _stamp)
  (:device_id
   (&optional __device_id)
   (if __device_id (setq _device_id __device_id)) _device_id)
  (:value
   (&optional __value)
   (if __value (setq _value __value)) _value)
  (:serialization-length
   ()
   (+
    ;; time _stamp
    8
    ;; uint8 _device_id
    1
    ;; int32 _value
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; time _stamp
       (write-long (send _stamp :sec) s) (write-long (send _stamp :nsec) s)
     ;; uint8 _device_id
       (write-byte _device_id s)
     ;; int32 _value
       (write-long _value s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; time _stamp
     (send _stamp :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _stamp :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint8 _device_id
     (setq _device_id (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; int32 _value
     (setq _value (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get blueprintlab_reachsystem_ros_messages::single_int :md5sum-) "29dcc1b9012662f9ba2eec6d39f61407")
(setf (get blueprintlab_reachsystem_ros_messages::single_int :datatype-) "blueprintlab_reachsystem_ros_messages/single_int")
(setf (get blueprintlab_reachsystem_ros_messages::single_int :definition-)
      "time stamp
uint8 device_id
int32 value

")



(provide :blueprintlab_reachsystem_ros_messages/single_int "29dcc1b9012662f9ba2eec6d39f61407")


