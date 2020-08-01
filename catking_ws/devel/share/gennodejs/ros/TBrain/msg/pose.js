// Auto-generated. Do not edit!

// (in-package TBrain.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let 4vec = require('./4vec.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class pose {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.matrix = null;
      this.other = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('matrix')) {
        this.matrix = initObj.matrix
      }
      else {
        this.matrix = [];
      }
      if (initObj.hasOwnProperty('other')) {
        this.other = initObj.other
      }
      else {
        this.other = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type pose
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [matrix]
    // Serialize the length for message field [matrix]
    bufferOffset = _serializer.uint32(obj.matrix.length, buffer, bufferOffset);
    obj.matrix.forEach((val) => {
      bufferOffset = 4vec.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [other]
    bufferOffset = _serializer.uint8(obj.other, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type pose
    let len;
    let data = new pose(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [matrix]
    // Deserialize array length for message field [matrix]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.matrix = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.matrix[i] = 4vec.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [other]
    data.other = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += 32 * object.matrix.length;
    return length + 5;
  }

  static datatype() {
    // Returns string type for a message object
    return 'TBrain/pose';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '610b28f21dd689a9c2eec18803824590';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new pose(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.matrix !== undefined) {
      resolved.matrix = new Array(msg.matrix.length);
      for (let i = 0; i < resolved.matrix.length; ++i) {
        resolved.matrix[i] = 4vec.Resolve(msg.matrix[i]);
      }
    }
    else {
      resolved.matrix = []
    }

    if (msg.other !== undefined) {
      resolved.other = msg.other;
    }
    else {
      resolved.other = 0
    }

    return resolved;
    }
};

module.exports = pose;
