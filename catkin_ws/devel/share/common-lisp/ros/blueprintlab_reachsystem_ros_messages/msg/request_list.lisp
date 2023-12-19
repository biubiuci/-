; Auto-generated. Do not edit!


(cl:in-package blueprintlab_reachsystem_ros_messages-msg)


;//! \htmlinclude request_list.msg.html

(cl:defclass <request_list> (roslisp-msg-protocol:ros-message)
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
   (requests
    :reader requests
    :initarg :requests
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass request_list (<request_list>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <request_list>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'request_list)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name blueprintlab_reachsystem_ros_messages-msg:<request_list> is deprecated: use blueprintlab_reachsystem_ros_messages-msg:request_list instead.")))

(cl:ensure-generic-function 'stamp-val :lambda-list '(m))
(cl:defmethod stamp-val ((m <request_list>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader blueprintlab_reachsystem_ros_messages-msg:stamp-val is deprecated.  Use blueprintlab_reachsystem_ros_messages-msg:stamp instead.")
  (stamp m))

(cl:ensure-generic-function 'device_id-val :lambda-list '(m))
(cl:defmethod device_id-val ((m <request_list>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader blueprintlab_reachsystem_ros_messages-msg:device_id-val is deprecated.  Use blueprintlab_reachsystem_ros_messages-msg:device_id instead.")
  (device_id m))

(cl:ensure-generic-function 'requests-val :lambda-list '(m))
(cl:defmethod requests-val ((m <request_list>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader blueprintlab_reachsystem_ros_messages-msg:requests-val is deprecated.  Use blueprintlab_reachsystem_ros_messages-msg:requests instead.")
  (requests m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <request_list>) ostream)
  "Serializes a message object of type '<request_list>"
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
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'requests))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'requests))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <request_list>) istream)
  "Deserializes a message object of type '<request_list>"
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
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'requests) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'requests)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<request_list>)))
  "Returns string type for a message object of type '<request_list>"
  "blueprintlab_reachsystem_ros_messages/request_list")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'request_list)))
  "Returns string type for a message object of type 'request_list"
  "blueprintlab_reachsystem_ros_messages/request_list")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<request_list>)))
  "Returns md5sum for a message object of type '<request_list>"
  "ef8741fe5bbee719df0c3943df9fc5c1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'request_list)))
  "Returns md5sum for a message object of type 'request_list"
  "ef8741fe5bbee719df0c3943df9fc5c1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<request_list>)))
  "Returns full string definition for message of type '<request_list>"
  (cl:format cl:nil "time stamp~%uint8 device_id~%int32[] requests~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'request_list)))
  "Returns full string definition for message of type 'request_list"
  (cl:format cl:nil "time stamp~%uint8 device_id~%int32[] requests~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <request_list>))
  (cl:+ 0
     8
     1
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'requests) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <request_list>))
  "Converts a ROS message object to a list"
  (cl:list 'request_list
    (cl:cons ':stamp (stamp msg))
    (cl:cons ':device_id (device_id msg))
    (cl:cons ':requests (requests msg))
))
