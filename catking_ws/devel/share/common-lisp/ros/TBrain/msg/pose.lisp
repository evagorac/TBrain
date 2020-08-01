; Auto-generated. Do not edit!


(cl:in-package TBrain-msg)


;//! \htmlinclude pose.msg.html

(cl:defclass <pose> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (matrix
    :reader matrix
    :initarg :matrix
    :type (cl:vector TBrain-msg:4vec)
   :initform (cl:make-array 0 :element-type 'TBrain-msg:4vec :initial-element (cl:make-instance 'TBrain-msg:4vec)))
   (other
    :reader other
    :initarg :other
    :type cl:fixnum
    :initform 0))
)

(cl:defclass pose (<pose>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <pose>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'pose)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name TBrain-msg:<pose> is deprecated: use TBrain-msg:pose instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <pose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader TBrain-msg:header-val is deprecated.  Use TBrain-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'matrix-val :lambda-list '(m))
(cl:defmethod matrix-val ((m <pose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader TBrain-msg:matrix-val is deprecated.  Use TBrain-msg:matrix instead.")
  (matrix m))

(cl:ensure-generic-function 'other-val :lambda-list '(m))
(cl:defmethod other-val ((m <pose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader TBrain-msg:other-val is deprecated.  Use TBrain-msg:other instead.")
  (other m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <pose>) ostream)
  "Serializes a message object of type '<pose>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'matrix))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'matrix))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'other)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <pose>) istream)
  "Deserializes a message object of type '<pose>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'matrix) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'matrix)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'TBrain-msg:4vec))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'other)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<pose>)))
  "Returns string type for a message object of type '<pose>"
  "TBrain/pose")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'pose)))
  "Returns string type for a message object of type 'pose"
  "TBrain/pose")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<pose>)))
  "Returns md5sum for a message object of type '<pose>"
  "610b28f21dd689a9c2eec18803824590")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'pose)))
  "Returns md5sum for a message object of type 'pose"
  "610b28f21dd689a9c2eec18803824590")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<pose>)))
  "Returns full string definition for message of type '<pose>"
  (cl:format cl:nil "Header header~%~%TBrain/4vec[] matrix~%uint8 other~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: TBrain/4vec~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'pose)))
  "Returns full string definition for message of type 'pose"
  (cl:format cl:nil "Header header~%~%TBrain/4vec[] matrix~%uint8 other~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: TBrain/4vec~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <pose>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'matrix) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <pose>))
  "Converts a ROS message object to a list"
  (cl:list 'pose
    (cl:cons ':header (header msg))
    (cl:cons ':matrix (matrix msg))
    (cl:cons ':other (other msg))
))
