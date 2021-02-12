import numpy as np
import setup

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


# ------------------- Begin Robot class definition -------------------
class Robot:
    # high level, easy to manipulate robot object

    def __init__(self, MC_pipe, JC_pipe):
        pass

    def joint_state(self, j):
        pass

    def home_joint(self, j):
        pass

    def move(self, pos=np.zeros(3), r_matrix=np.identity(3), absolute=True, rapid=False):
        pass

    def joint_move(self, joint_no, angle, absolute=True):
        # radians
        pass

    def actuate_end_effector(self):
        pass


# ------------------- Begin Motion controller class definition -------------------
class MotionController:
    # handles movement commands from Robot class, will lerp and slerp, will compute joint angles for Joint Controller

    __dh_param = None
    __limit_offsets = None
    __base_pose_offset = None

    max_acceleration = 1  # m/s^2
    max_velocity = .05  # m/s
    max_alpha = 1  # rad/s^2
    max_omega = np.pi/10  # rad/s

    cur_joint_angles = None
    motor_pos = None

    def __init__(self, base_pose_offset):
        self.__dh_param = dh_param
        self.__limit_offsets = limit_offsets
        self.__base_pose_offset = base_pose_offset

    def fkine(self, joint_angles):
        pass

    def ikine(self, pose, cur_pose):
        pass

    def within_tol(self, trans_tol, angle_tol):
        pass


# ------------------- Begin Joint controller class definition -------------------
class JointController:
    # communicates with odrives and receives commands from Motion Controller

    odrives = None
    __joint_angle_setpoints = np.array([0,np.pi/2,0,0,0,0]) #TODO make better defaults, might send it straight down
    __motor_calibration_states = np.zeros(6, dtype=bool) # list of indicators for each motor is calibrated
    __J14_lookup = {1:(0,0), 2:(1,0), 3:(0,1), 4:(1,1)} # maps joint # from 1-4 to a odrive axis pair

    # define gear ratios for joints excluding J2 an J3 which require a separate function
    # this is defined as the number of input revolutions of the motor for one output revolution of the robot joint
    J1_ratio = 1 # TODO insert gear ratios
    J4_ratio = 1
    J5_ratio = 1
    J6_ratio = 1

    in_to_m = 0.0254

    def __init__(self, ODSerialsPath):
        self.odrives = setup.import_odrives(ODSerialPath)
        if len(self.odrives) != 3:
            raise Exception("Error importing odrives correctly. Expected 3 but received {}.".format(len(self.odrives)))

    def calib_axes(self, full_calib=True):
        for od_idx in range(len(self.odrives)):
            for axis in [0,1]:
                try:
                    setup.odrive_axis_calib(odrives[od_idx], axis, full_calib=full_calib)
                    self.__joint_calibration_states[od_idx + axis] = True
                except Exception as inst: # catches excpetion if calib fails
                    print(inst.args)

    def home(self): # will home with switches and use limit offsets to zero machine
        pass #TODO

    def get_joint_setpoints(self):
        return self.__joint_angle_setpoints

    # the following functions return motor positions from desired joint angles
    def linear_joint_map(self, joint_angle, ratio=1):
        return joint_angle * ratio

    def J2_map(self, joint_angle):
        # define constants from math
        # a positive value for motor pos corresponds to the carriage moving downwards and towards the limit switch
        th = joint_angle
        tanth = np.tan(th)
        a = 2.5 * self.in_to_m 
        b = 5 * self.in_to_m
        c = 4.25 * self.in_to_m
        r = 9 * self.in_to_m
        beta = 1/np.sqrt(1+tanth**2)

        # the following follow the form (A+sqrt(B))/C
        A = -2*beta*(thanth*(a-beta*c) + beta*c*tanth-b)
        B = 4*beta**2*(tanth*(a-beta*c)+beta*c*tanth-b)**2 - 4*beta**2*(1+tanth**2)*((a-beta*c)**2 + (beta*c*tanth-b)**2 - r**2)
        C = 2*beta**2*(1+tanth**2)

        x = (A + np.sqrt(B)) / C
        
        # lastly convert position of carraige to motor position
        motor_screw_ratio = 2 # turns of input to output
        pitch = .005 # meters / turn

        return motor_screw_ratio * x / pitch

    def J3_map(self, joint_angle):
        # define constants from math
        # a positive value for motor pos corresponds to the carriage moving downwards and away from the limit switch
        th = -joint_angle * np.pi/2 + np.pi/2
        tanth = np.tan(th)
        a = 3.5 * self.in_to_m
        b = 7 * self.in_to_m
        c = 4.25 * self.in_to_m
        r = 11.5 * self.in_to_m
        beta = 1/np.sqrt(1+tanth**2)

        pitch = .005 # meters

        # the following follow the form (A+sqrt(B))/C
        A = -2*beta*(thanth*(a-beta*c) + beta*c*tanth-b)
        B = 4*beta**2*(tanth*(a-beta*c)+beta*c*tanth-b)**2 - 4*beta**2*(1+tanth**2)*((a-beta*c)**2 + (beta*c*tanth-b)**2 - r**2)
        C = 2*beta**2*(1+tanth**2)

        x = (A + np.sqrt(B)) / C

        # lastly convert position of carraige to motor position
        motor_screw_ratio = 2 # turns of input to output
        pitch = .005 # meters / turn

        return motor_screw_ratio * x / pitch

    def J56_diff_map(self, J5_angle, J6_angle, J5_ratio=1, J6_ratio=1):
        # function returns motor position values for M5(A) and M6(B) for inputs for J5 and J6 angles
        # assume positive change in motor position for M5 and M6 correspond to a positive change in J5_angle
        # assume positive change in M5 and negative change in M6 correspond to a positive change in J6_angle
        M5_pos = 0
        M6_pos = 0

        M5_pos += J5_angle * J5_ratio
        M6_pos += J5_angle * J5_ratio

        M5_pos += J6_angle * J6_ratio
        M6_pos -= J6_angle * J6_ratio
        
        return (M5_pos, M6_pos)

    def check_discontinuity(self, prev, current):
        # checks to see if step in joint angle is within reason to prevent accidents
        max_step_degrees = 5
        max_step_radians = max_step_degrees * 180/np.pi

        if abs(current - prev) > max_step_radians:
            raise Exception("warning, change in joint angle exceeded {}".format(current-prev))


    def set(self, J_vec):
        # J_vec is a 6 element np array of joint setpoints in order from J1-J6
        # this function takes a np array of rotational setpoints for the joints and commands to odrives
        # before writing to odrives we must also do the ballscrew trig to make setpoints correctly

        '''setup returns odrives from bottom to top, but because the odrives were wired to spread current fairly
        evenly according to how hard each motor has to work the odrives, the axis objects are not ordered
        the same as the joints are.  J14_lookup defined in the class field maps joints 1-4 desired to a
        respective odrive and axis tuple excluding J5 and J6 because of the differential which requires both
        to move together.'''

        # ----- Begin J1-J4 -----
        for joint in [1, 2, 3, 4]:
            self.check_discontinuity(self.__joint_angle_setpoints[joint-1], J_vec[joint-1])
            angle_setpoint = J_vec[joint-1]

            self.__joint_angle_setpoints[joint-1] = angle_setpoint # make new setpoint the previous setpoint for the next set function call
            od_idx, axis = self.__J14_lookup[joint] # get corresponding odrive and axis for joint in question
            axis_object = setup.get_axis_object(odrives[od_idx], axis) # get odrive axis object to command motor

            if joint in [1, 4]: # if the joint is not a ball screw joint, do simple linear map
                ratio = (self.J1_ratio if joint==1 else self.J4_ratio)
                motor_setpoint = self.linear_joint_map(angle_setpoint, ratio)
            elif joint == 2: # if we are dealing with joint 2 or 3, pass through joint angle to motor pos function taking into account the geometry of screws
                motor_setpoint = self.J2_map(angle_setpoint)
            elif joint == 3:
                motor_setpoint = self.J3_map(angle_setpoint)
            else:
                raise Exception("error, joint {} is not between 1 and 4".format(joint))

            axis_object.controller.input_pos = motor_setpoint

        # ----- Begin J5&J6 -----
        J5_setpoint = J_vec[4]
        J6_setpoint = J_vec[5]

        for joint in [5,6]:
            self.check_discontinuity(self.__joint_angle_setpoints[joint-1], J_vec[joint-1])
            self.__joint_angle_setpoints[joint-1] = J_vec[joint-1]

        M5_pos, M6_pos = self.J56_diff_map(J5_setpoint, J6_setpoint, J5_ratio=self.J5_ratio, J6_ratio=self.J6_ratio)
        setup.get_axis_object(odrives[2], 0).controller.input_pos = M5_pos
        setup.get_axis_object(odrives[2], 1).controller.input_pos = M6_pos


# ------------------- Begin Test cases -------------------
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