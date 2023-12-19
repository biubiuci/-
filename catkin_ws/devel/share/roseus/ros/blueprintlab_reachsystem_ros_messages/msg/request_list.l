;; Auto-generated. Do not edit!


(when (boundp 'blueprintlab_reachsystem_ros_messages::request_list)
  (if (not (find-package "BLUEPRINTLAB_REACHSYSTEM_ROS_MESSAGES"))
    (make-package "BLUEPRINTLAB_REACHSYSTEM_ROS_MESSAGES"))
  (shadow 'request_list (find-package "BLUEPRINTLAB_REACHSYSTEM_ROS_MESSAGES")))
(unless (find-package "BLUEPRINTLAB_REACHSYSTEM_ROS_MESSAGES::REQUEST_LIST")
  (make-package "BLUEPRINTLAB_REACHSYSTEM_ROS_MESSAGES::REQUEST_LIST"))

(in-package "ROS")
;;//! \htmlinclude request_list.msg.html


(defclass blueprintlab_reachsystem_ros_messages::request_list
  :super ros::object
  :slots (_stamp _device_id _requests ))

(defmethod blueprintlab_reachsystem_ros_messages::request_list
  (:init
   (&key
    ((:stamp __stamp) (instance ros::time :init))
    ((:device_id __device_id) 0)
    ((:requests __requests) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _stamp __stamp)
   (setq _device_id (round __device_id))
   (setq _requests __requests)
   self)
  (:stamp
   (&optional __stamp)
   (if __stamp (setq _stamp __stamp)) _stamp)
  (:device_id
   (&optional __device_id)
   (if __device_id (setq _device_id __device_id)) _device_id)
  (:requests
   (&optional __requests)
   (if __requests (setq _requests __requests)) _requests)
  (:serialization-length
   ()
   (+
    ;; time _stamp
    8
    ;; uint8 _device_id
    1
    ;; int32[] _requests
    (* 4    (length _requests)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; time _stamp
       (write-long (send _stamp :sec) s) (write-long (send _stamp :nsec) s)
     ;; uint8 _device_id
       (write-byte _device_id s)
     ;; int32[] _requests
     (write-long (length _requests) s)
     (dotimes (i (length _requests))
       (write-long (elt _requests i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; time _stamp
     (send _stamp :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _stamp :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint8 _device_id
     (setq _device_id (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; int32[] _requests
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _requests (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _requests i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get blueprintlab_reachsystem_ros_messages::request_list :md5sum-) "ef8741fe5bbee719df0c3943df9fc5c1")
(setf (get blueprintlab_reachsystem_ros_messages::request_list :datatype-) "blueprintlab_reachsystem_ros_messages/request_list")
(setf (get blueprintlab_reachsystem_ros_messages::request_list :definition-)
      "time stamp
uint8 device_id
int32[] requests

")



(provide :blueprintlab_reachsystem_ros_messages/request_list "ef8741fe5bbee719df0c3943df9fc5c1")


