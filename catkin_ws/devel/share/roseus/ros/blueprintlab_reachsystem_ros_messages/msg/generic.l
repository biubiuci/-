;; Auto-generated. Do not edit!


(when (boundp 'blueprintlab_reachsystem_ros_messages::generic)
  (if (not (find-package "BLUEPRINTLAB_REACHSYSTEM_ROS_MESSAGES"))
    (make-package "BLUEPRINTLAB_REACHSYSTEM_ROS_MESSAGES"))
  (shadow 'generic (find-package "BLUEPRINTLAB_REACHSYSTEM_ROS_MESSAGES")))
(unless (find-package "BLUEPRINTLAB_REACHSYSTEM_ROS_MESSAGES::GENERIC")
  (make-package "BLUEPRINTLAB_REACHSYSTEM_ROS_MESSAGES::GENERIC"))

(in-package "ROS")
;;//! \htmlinclude generic.msg.html


(defclass blueprintlab_reachsystem_ros_messages::generic
  :super ros::object
  :slots (_stamp _device_id _packet_id _data ))

(defmethod blueprintlab_reachsystem_ros_messages::generic
  (:init
   (&key
    ((:stamp __stamp) (instance ros::time :init))
    ((:device_id __device_id) 0)
    ((:packet_id __packet_id) 0)
    ((:data __data) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _stamp __stamp)
   (setq _device_id (round __device_id))
   (setq _packet_id (round __packet_id))
   (setq _data __data)
   self)
  (:stamp
   (&optional __stamp)
   (if __stamp (setq _stamp __stamp)) _stamp)
  (:device_id
   (&optional __device_id)
   (if __device_id (setq _device_id __device_id)) _device_id)
  (:packet_id
   (&optional __packet_id)
   (if __packet_id (setq _packet_id __packet_id)) _packet_id)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; time _stamp
    8
    ;; uint8 _device_id
    1
    ;; uint8 _packet_id
    1
    ;; float32[] _data
    (* 4    (length _data)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; time _stamp
       (write-long (send _stamp :sec) s) (write-long (send _stamp :nsec) s)
     ;; uint8 _device_id
       (write-byte _device_id s)
     ;; uint8 _packet_id
       (write-byte _packet_id s)
     ;; float32[] _data
     (write-long (length _data) s)
     (dotimes (i (length _data))
       (sys::poke (elt _data i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; time _stamp
     (send _stamp :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _stamp :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint8 _device_id
     (setq _device_id (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _packet_id
     (setq _packet_id (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float32[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _data i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get blueprintlab_reachsystem_ros_messages::generic :md5sum-) "3d9227290a2d905fa3823529454d5aa2")
(setf (get blueprintlab_reachsystem_ros_messages::generic :datatype-) "blueprintlab_reachsystem_ros_messages/generic")
(setf (get blueprintlab_reachsystem_ros_messages::generic :definition-)
      "time stamp
uint8 device_id
uint8 packet_id
float32[] data

")



(provide :blueprintlab_reachsystem_ros_messages/generic "3d9227290a2d905fa3823529454d5aa2")


