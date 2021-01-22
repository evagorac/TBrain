import numpy as np

class PoseWrap:
  # matrix pose handler
  def __init__(self, pose):
    pose = np.array(pose)
    self.check_pose_legality(pose)
    self.__pose = pose

  def set_pose(self, pose):
    pose = np.array(pose)
    self.check_pose_legality(pose)
    self.__pose = pose

  def set_r_matrix(self, r_matrix):
    r_matrix = np.array(r_matrix)
    if ~self.is_r_matrix_legal(r_matrix):
      raise Exception("rotaion matrix is illegal " + str(r_matrix))
    self.__pose[:3, :3] = r_matrix

  def set_pos(self, pos_vec):
    pos_vec = np.array(pos_vec)
    if pos_vec.shape != (3,1) or np.any(~np.isreal(pos_vec)):
      raise Exception("position vector is illegal " + str(pos_vec))
    self.__pose[:3, 3] = pos_vec

  def is_r_matrix_legal(self, r_matrix):
    if r_matrix.shape != (3,3):
      return False
    # check if r_matrix is orthogonal by dotting all col vecs, making sure
    # all are at right angles and make sure determinant == 1
    epsilon = .00001
    if np.abs(np.linalg.det(r_matrix)-1) > epsilon:
      return False
    for col1 in range(3):
      for col2 in range(col1+1, 3):
        if np.abs(np.dot(r_matrix[:, col1], r_matrix[:, col2])) > epsilon:
          return False
    return True

  def check_pose_legality(self, pose):
    pose = np.array(pose)
    # pose is np 4x4 trans matrix
    # check to see if pose is legal
    if pose.shape != (4,4):
      raise Exception("pose is not a 4x4 matrix " + str(pose))

    # check for real numbers
    if np.any(~np.isreal(pose)):
      raise Exception("nonreal numbers present in pose matrix " + str(pose))

    # ensure rotation matrix is legal
    r_matrix = pose[:3, :3]
    if not self.is_r_matrix_legal(r_matrix):
      raise Exception("rotation matrix is illegal " + str(r_matrix))

    # ensure the bottom row of transformation matrix is correct
    if np.any(~np.equal(pose[3, :], np.array([0, 0, 0, 1]))):
      raise Excpetion("transformation matrix is nonhomogenous " + str(pose))

  def forward(self, ext_pose):
    # perform forward transform of class pose by ext_pose matrix
    # equivalent to matmul(ext_pose, class_pose)
    if not isinstance(ext_pose, PoseWrap):
      raise Exception("pose object passed to forward transform is not a PoseWrap instance")
    return np.matmul(ext_pose.get_pose(), self.__pose)

  def inverse(self, ext_pose):
    # perform inverse transform of class pose by the inverse of ext_pose matrix
    # equivalent to matmul(inv(ext_pose), class_pose)
    if not isinstance(ext_pose, PoseWrap):
      raise Exception("pose object passed to inverse transform is not a PoseWrap instance")
    return np.linalg.solve(ext_pose.get_pose(), self.__pose)

  def get_pose(self):
    return self.__pose

  def get_r_matrix(self):
    return self.__pose[:3, :3]

  def get_pos_vec(self):
    return self.__pose[:3, 3].reshape((3,1))

  def __str__(self):
    return str(self.__pose)


class Robot:
  # high level, easy to manipulate robot object

  dh_param = None
  limit_offsets = None
  cur_joint_angles = None
  base_pose = None

  max_acceleration = 1  # m/s^2
  max_velocity = .05  # m/s
  max_alpha = 1  # rad/s^2
  max_omega = np.pi/10  # rad/s

  def __init__(self, dh_param=None, limit_offsets=np.zeros(6), cur_joint_angles=np.zeros(6), base_pose=np.identity(4)):
    self.dh_param = dh_param
    self.limit_offsets = limit_offsets
    self.cur_joint_angles = cur_joint_angles
    self.base_pose = base_pose

  def home_joints(self, remember_pos=False):
    pass

  def move(self, pos=np.zeros(3), r_matrix=np.identity(3), absolute=True, rapid=False):
    pass

  def joint_move(self, joint_no, angle, absolute=True):
    # radians
    pass

  def actuate_end_effector(self):
    pass


class MotionController:
  # handles movement commands from Robot class, will lerp and slerp, will compute joint angles for Joint Controller

  cur_joint_angles = None
  motor_pos = None

  def __init__(self):
    pass

  def ikine(self, pose, cur_pose):
    pass

  def fkine(self, joint_angles):
    pass

  def within_tol(self, trans_tol, angle_tol):
    pass


class JointController:
  # communicates with odrives and receives commands from Motion Controller

  def __init__(self):
    pass

  def get_joint_pos_legality(self):
    pass


if __name__ == "__main__":
  print("running test cases")
  print("start with pose wrapper")

  t1 = PoseWrap([[0,1,0,1],[1,0,0,1],[0,0,-1,1],[0,0,0,1]])
  x = np.array([[0,1,0,1],[1,0,0,1],[0,0,-1,1],[0,0,0,1]])
  t2 = PoseWrap(x)
  res = t2.forward(t1)
  print(t1)
  print(t2)
  print(res)
