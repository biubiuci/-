; Auto-generated. Do not edit!


(cl:in-package blueprintlab_reachsystem_ros_messages-msg)


;//! \htmlinclude generic.msg.html

(cl:defclass <generic> (roslisp-msg-protocol:ros-message)
  ((stamp
    :reader stamp
    :initarg :stamp
    :type cl:real
    :initform 0)
   (device_id
    :reader device_id
    :initarg :device_id
    :type cl:fixnum
    :initform 0)
   (packet_id
    :reader packet_id
    :initarg :packet_id
    :type cl:fixnum
    :initform 0)
   (data
    :reader data
    :initarg :data
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass generic (<generic>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <generic>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'generic)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name blueprintlab_reachsystem_ros_messages-msg:<generic> is deprecated: use blueprintlab_reachsystem_ros_messages-msg:generic instead.")))

(cl:ensure-generic-function 'stamp-val :lambda-list '(m))
(cl:defmethod stamp-val ((m <generic>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader blueprintlab_reachsystem_ros_messages-msg:stamp-val is deprecated.  Use blueprintlab_reachsystem_ros_messages-msg:stamp instead.")
  (stamp m))

(cl:ensure-generic-function 'device_id-val :lambda-list '(m))
(cl:defmethod device_id-val ((m <generic>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader blueprintlab_reachsystem_ros_messages-msg:device_id-val is deprecated.  Use blueprintlab_reachsystem_ros_messages-msg:device_id instead.")
  (device_id m))

(cl:ensure-generic-function 'packet_id-val :lambda-list '(m))
(cl:defmethod packet_id-val ((m <generic>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader blueprintlab_reachsystem_ros_messages-msg:packet_id-val is deprecated.  Use blueprintlab_reachsystem_ros_messages-msg:packet_id instead.")
  (packet_id m))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <generic>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader blueprintlab_reachsystem_ros_messages-msg:data-val is deprecated.  Use blueprintlab_reachsystem_ros_messages-msg:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <generic>) ostream)
  "Serializes a message object of type '<generic>"
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'stamp)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'stamp) (cl:floor (cl:slot-value msg 'stamp)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'device_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'packet_id)) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <generic>) istream)
  "Deserializes a message object of type '<generic>"
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'stamp) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'device_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'packet_id)) (cl:read-byte istream))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<generic>)))
  "Returns string type for a message object of type '<generic>"
  "blueprintlab_reachsystem_ros_messages/generic")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'generic)))
  "Returns string type for a message object of type 'generic"
  "blueprintlab_reachsystem_ros_messages/generic")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<generic>)))
  "Returns md5sum for a message object of type '<generic>"
  "3d9227290a2d905fa3823529454d5aa2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'generic)))
  "Returns md5sum for a message object of type 'generic"
  "3d9227290a2d905fa3823529454d5aa2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<generic>)))
  "Returns full string definition for message of type '<generic>"
  (cl:format cl:nil "time stamp~%uint8 device_id~%uint8 packet_id~%float32[] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'generic)))
  "Returns full string definition for message of type 'generic"
  (cl:format cl:nil "time stamp~%uint8 device_id~%uint8 packet_id~%float32[] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <generic>))
  (cl:+ 0
     8
     1
     1
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <generic>))
  "Converts a ROS message object to a list"
  (cl:list 'generic
    (cl:cons ':stamp (stamp msg))
    (cl:cons ':device_id (device_id msg))
    (cl:cons ':packet_id (packet_id msg))
    (cl:cons ':data (data msg))
))
