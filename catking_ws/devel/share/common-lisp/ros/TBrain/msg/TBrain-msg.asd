
(cl:in-package :asdf)

(defsystem "TBrain-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "4vec" :depends-on ("_package_4vec"))
    (:file "_package_4vec" :depends-on ("_package"))
    (:file "pose" :depends-on ("_package_pose"))
    (:file "_package_pose" :depends-on ("_package"))
  ))