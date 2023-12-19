; Auto-generated. Do not edit!


(cl:in-package blueprintlab_reachsystem_ros_messages-msg)


;//! \htmlinclude single_int.msg.html

(cl:defclass <single_int> (roslisp-msg-protocol:ros-message)
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
   (value
    :reader value
    :initarg :value
    :type cl:integer
    :initform 0))
)

(cl:defclass single_int (<single_int>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <single_int>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'single_int)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name blueprintlab_reachsystem_ros_messages-msg:<single_int> is deprecated: use blueprintlab_reachsystem_ros_messages-msg:single_int instead.")))

(cl:ensure-generic-function 'stamp-val :lambda-list '(m))
(cl:defmethod stamp-val ((m <single_int>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader blueprintlab_reachsystem_ros_messages-msg:stamp-val is deprecated.  Use blueprintlab_reachsystem_ros_messages-msg:stamp instead.")
  (stamp m))

(cl:ensure-generic-function 'device_id-val :lambda-list '(m))
(cl:defmethod device_id-val ((m <single_int>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader blueprintlab_reachsystem_ros_messages-msg:device_id-val is deprecated.  Use blueprintlab_reachsystem_ros_messages-msg:device_id instead.")
  (device_id m))

(cl:ensure-generic-function 'value-val :lambda-list '(m))
(cl:defmethod value-val ((m <single_int>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader blueprintlab_reachsystem_ros_messages-msg:value-val is deprecated.  Use blueprintlab_reachsystem_ros_messages-msg:value instead.")
  (value m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <single_int>) ostream)
  "Serializes a message object of type '<single_int>"
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
  (cl:let* ((signed (cl:slot-value msg 'value)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <single_int>) istream)
  "Deserializes a message object of type '<single_int>"
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
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'value) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<single_int>)))
  "Returns string type for a message object of type '<single_int>"
  "blueprintlab_reachsystem_ros_messages/single_int")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'single_int)))
  "Returns string type for a message object of type 'single_int"
  "blueprintlab_reachsystem_ros_messages/single_int")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<single_int>)))
  "Returns md5sum for a message object of type '<single_int>"
  "29dcc1b9012662f9ba2eec6d39f61407")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'single_int)))
  "Returns md5sum for a message object of type 'single_int"
  "29dcc1b9012662f9ba2eec6d39f61407")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<single_int>)))
  "Returns full string definition for message of type '<single_int>"
  (cl:format cl:nil "time stamp~%uint8 device_id~%int32 value~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'single_int)))
  "Returns full string definition for message of type 'single_int"
  (cl:format cl:nil "time stamp~%uint8 device_id~%int32 value~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <single_int>))
  (cl:+ 0
     8
     1
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <single_int>))
  "Converts a ROS message object to a list"
  (cl:list 'single_int
    (cl:cons ':stamp (stamp msg))
    (cl:cons ':device_id (device_id msg))
    (cl:cons ':value (value msg))
))
