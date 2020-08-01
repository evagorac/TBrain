;; Auto-generated. Do not edit!


(when (boundp 'TBrain::pose)
  (if (not (find-package "TBRAIN"))
    (make-package "TBRAIN"))
  (shadow 'pose (find-package "TBRAIN")))
(unless (find-package "TBRAIN::POSE")
  (make-package "TBRAIN::POSE"))

(in-package "ROS")
;;//! \htmlinclude pose.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass TBrain::pose
  :super ros::object
  :slots (_header _matrix _other ))

(defmethod TBrain::pose
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:matrix __matrix) ())
    ((:other __other) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _matrix __matrix)
   (setq _other (round __other))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:matrix
   (&rest __matrix)
   (if (keywordp (car __matrix))
       (send* _matrix __matrix)
     (progn
       (if __matrix (setq _matrix (car __matrix)))
       _matrix)))
  (:other
   (&optional __other)
   (if __other (setq _other __other)) _other)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; TBrain/4vec[] _matrix
    (apply #'+ (send-all _matrix :serialization-length)) 4
    ;; uint8 _other
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; TBrain/4vec[] _matrix
     (write-long (length _matrix) s)
     (dolist (elem _matrix)
       (send elem :serialize s)
       )
     ;; uint8 _other
       (write-byte _other s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; TBrain/4vec[] _matrix
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _matrix (let (r) (dotimes (i n) (push (instance TBrain::4vec :init) r)) r))
     (dolist (elem- _matrix)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; uint8 _other
     (setq _other (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get TBrain::pose :md5sum-) "610b28f21dd689a9c2eec18803824590")
(setf (get TBrain::pose :datatype-) "TBrain/pose")
(setf (get TBrain::pose :definition-)
      "Header header

TBrain/4vec[] matrix
uint8 other

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: TBrain/4vec
float64 x
float64 y
float64 z
float64 w

")



(provide :TBrain/pose "610b28f21dd689a9c2eec18803824590")


