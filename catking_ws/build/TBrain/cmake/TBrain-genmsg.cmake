# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "TBrain: 2 messages, 0 services")

set(MSG_I_FLAGS "-ITBrain:/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(TBrain_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/4vec.msg" NAME_WE)
add_custom_target(_TBrain_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "TBrain" "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/4vec.msg" ""
)

get_filename_component(_filename "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/pose.msg" NAME_WE)
add_custom_target(_TBrain_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "TBrain" "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/pose.msg" "TBrain/4vec:std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(TBrain
  "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/4vec.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/TBrain
)
_generate_msg_cpp(TBrain
  "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/pose.msg"
  "${MSG_I_FLAGS}"
  "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/4vec.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/TBrain
)

### Generating Services

### Generating Module File
_generate_module_cpp(TBrain
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/TBrain
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(TBrain_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(TBrain_generate_messages TBrain_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/4vec.msg" NAME_WE)
add_dependencies(TBrain_generate_messages_cpp _TBrain_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/pose.msg" NAME_WE)
add_dependencies(TBrain_generate_messages_cpp _TBrain_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(TBrain_gencpp)
add_dependencies(TBrain_gencpp TBrain_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS TBrain_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(TBrain
  "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/4vec.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/TBrain
)
_generate_msg_eus(TBrain
  "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/pose.msg"
  "${MSG_I_FLAGS}"
  "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/4vec.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/TBrain
)

### Generating Services

### Generating Module File
_generate_module_eus(TBrain
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/TBrain
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(TBrain_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(TBrain_generate_messages TBrain_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/4vec.msg" NAME_WE)
add_dependencies(TBrain_generate_messages_eus _TBrain_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/pose.msg" NAME_WE)
add_dependencies(TBrain_generate_messages_eus _TBrain_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(TBrain_geneus)
add_dependencies(TBrain_geneus TBrain_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS TBrain_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(TBrain
  "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/4vec.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/TBrain
)
_generate_msg_lisp(TBrain
  "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/pose.msg"
  "${MSG_I_FLAGS}"
  "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/4vec.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/TBrain
)

### Generating Services

### Generating Module File
_generate_module_lisp(TBrain
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/TBrain
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(TBrain_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(TBrain_generate_messages TBrain_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/4vec.msg" NAME_WE)
add_dependencies(TBrain_generate_messages_lisp _TBrain_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/pose.msg" NAME_WE)
add_dependencies(TBrain_generate_messages_lisp _TBrain_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(TBrain_genlisp)
add_dependencies(TBrain_genlisp TBrain_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS TBrain_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(TBrain
  "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/4vec.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/TBrain
)
_generate_msg_nodejs(TBrain
  "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/pose.msg"
  "${MSG_I_FLAGS}"
  "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/4vec.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/TBrain
)

### Generating Services

### Generating Module File
_generate_module_nodejs(TBrain
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/TBrain
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(TBrain_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(TBrain_generate_messages TBrain_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/4vec.msg" NAME_WE)
add_dependencies(TBrain_generate_messages_nodejs _TBrain_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/pose.msg" NAME_WE)
add_dependencies(TBrain_generate_messages_nodejs _TBrain_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(TBrain_gennodejs)
add_dependencies(TBrain_gennodejs TBrain_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS TBrain_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(TBrain
  "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/4vec.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/TBrain
)
_generate_msg_py(TBrain
  "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/pose.msg"
  "${MSG_I_FLAGS}"
  "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/4vec.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/TBrain
)

### Generating Services

### Generating Module File
_generate_module_py(TBrain
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/TBrain
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(TBrain_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(TBrain_generate_messages TBrain_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/4vec.msg" NAME_WE)
add_dependencies(TBrain_generate_messages_py _TBrain_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chris/PycharmProjects/TBrain/catking_ws/src/TBrain/msg/pose.msg" NAME_WE)
add_dependencies(TBrain_generate_messages_py _TBrain_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(TBrain_genpy)
add_dependencies(TBrain_genpy TBrain_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS TBrain_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/TBrain)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/TBrain
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(TBrain_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/TBrain)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/TBrain
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(TBrain_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/TBrain)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/TBrain
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(TBrain_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/TBrain)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/TBrain
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(TBrain_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/TBrain)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/TBrain\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/TBrain
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(TBrain_generate_messages_py std_msgs_generate_messages_py)
endif()
