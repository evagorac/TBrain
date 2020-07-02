import numpy as np

print("working")


class Pose:
    # matrix pose handler and wrapper

    pose = None

    def __init__(self, r_matrix=None, pos_vec=None, identity=False):
        if identity:
            self.pose = np.identity(4)
        else:
            self.pose = np.block([[r_matrix, pos_vec], [0, 0, 0, 1]])

    def set(self, r_matrix=None, pos_vec=None):
        if r_matrix is not None:
            self.pose[:3, :3] = r_matrix
        if pos_vec is not None:
            self.pose[:3, 3] = pos_vec

    def multiply(self, pose2):
        return np.matmul(self.pose, pose2)


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

    def home_joints(self):
        pass

    def abs_move(self, pos=None, r_matrix=None):
        pass

    def rel_move(self, pos=None, r_matrix=None):
        pass

    def abs_rapid(self, pos=None, r_matrix=None):
        pass

    def rel_rapid(self, pos=None, r_matrix=None):
        pass

    def abs_joint_move(self, joint_no, angle):
        # radians
        pass

    def rel_joint_move(self, joint_no, angle):
        # radians
        pass

    def actuate_end_effector(self):
        pass


class MotionController:
    # handles movement commands from Robot class, will lerp and slerp, will compute joint angles for Joint Controller

    cur_joint_angles = None
    motor_pos = None

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
