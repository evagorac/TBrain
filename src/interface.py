import numpy as np
import setup

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

    # DH param encoded as clomuns for theta, d, alpha, and a in that order
    # distance units are meters
    # angle units are radian
    # NOTE odrive wants turns, not radians
    # theta initialized to zero

    DH_path = '../Math/DH.csv'
    __dh_param = np.genfromtxt(DH_path,skip_header=1, delimiter=',')[:,1:]
    __base_pose_offset = None
    __inv_base_pose_offset = None

    max_acceleration = 1  # m/s^2
    max_velocity = .05  # m/s
    max_alpha = 1  # rad/s^2
    max_omega = np.pi/10  # rad/s

    current_pose = None
    test_joint_angles = None

    def __init__(self, RC_pipe, JC_pipe, base_pose_offset=np.eye(4)):
        self.__base_pose_offset = base_pose_offset
        self.__inv_base_pose_offset = np.linalg.inv(base_pose_offset)

        current_joint_angles = None # get current joint angles from call to Joint Controller after calibration has completed

        if current_joint_angles is None:
            print('\033[93m')
            print('MotionController instance received Nonetype for current_joint_angles during instantiation')
            print('\033[0m')
            return

        self.update_joint_angles(current_joint_angles) # update joint angles in DH param class variable
        self.current_pose = self.fkine(0,6) # find current pose through call to fkine with current joint angles

    def get_DH(self):
        return self.__dh_param

    def get_joint_angles(self):
        return self.__dh_param[:,0]

    def update_joint_angles(self, joint_angles):
        # replaces thetas in class DH param with new ones
        # if theta passed == None, skip and leave previous theta inside

        l = len(joint_angles)
        if l != 6:
            raise Exception("joint angle list of length {l} is not of length 6")

        for i in range(l):
            angle = joint_angles[i]
            if angle is not None:
                self.__dh_param[i,0] = angle

    def get_serial_transform(self, starting_joint, joint_angle=None, inverse=False):
        # given joint, return transform to get to the next join in the robot
        # if inverse, get tranform to previous joint in robot
        # manually pass in joint_angle to use instead of dh param if needed
        #   -this could be useful while solving for joint angles and finding that target pose is impossible, so dh param stay unmodified

        if type(starting_joint) != int:
            raise Exception("Joint must be an integer")

        if not inverse:
            if starting_joint not in range(0,6):
                raise Exception(f"forward transform for starting joint {starting_joint} does not exist")

            if starting_joint == 0:
                return self.__base_pose_offset

            joint_idx = starting_joint - 1
            theta_DH, d, alpha, a = self.__dh_param[joint_idx]

            if joint_angle is not None: #check if joint manually passed into function, otherwise get from DH param
                theta = joint_angle
            else:
                theta = theta_DH

            ct = np.cos(theta)
            st = np.sin(theta)
            ca = np.cos(alpha)
            sa = np.sin(alpha)

            Z = np.array([[ct, -st, 0, 0], [st, ct, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]]) # translation and rotation about Z axis
            X = np.array([[1, 0, 0, a], [0, ca, -sa, 0], [0, sa, ca, 0], [0, 0, 0, 1]]) # translation and rotation about X axis

            T = np.matmul(Z, X)
            return T

        else:
            # if inverse is selected, retrace one joint and use parameters for inverse transform
            if starting_joint not in range(1,7):
                raise Exception(f"inverse transform for starting joint {starting_joint} does not exist")

            joint_idx = starting_joint - 2
            theta_DH, d, alpha, a = self.__dh_param[joint_idx]

            if joint_angle is not None: #check if joint manually passed into function, otherwise get from DH param
                theta = joint_angle
            else:
                theta = theta_DH

            ct = np.cos(theta)
            st = np.sin(theta)
            ca = np.cos(alpha)
            sa = np.sin(alpha)

            X_inv = np.array([[1, 0, 0, -a], [0, ca, sa, 0], [0, -sa, ca, 0], [0, 0, 0, 1]]) # translation and rotation about X axis
            Z_inv = np.array([[ct, st, 0, 0], [-st, ct, 0, 0], [0, 0, 1, -d], [0, 0, 0, 1]]) # translation and rotation about Z axis

            T_inv = np.matmul(X_inv, Z_inv)
            return T_inv


    def fkine(self, start_joint, end_joint, use_test_angles=False, reverse=False):
        # takes starting joint and ending joint, and returns the pose of the end joint in the starting joint's frame
        # check to see if start and end are within domain
        # if use_test_angles is true, use class variable test_joint_angles instead of parsing dh param

        if start_joint not in range(0,7):
            raise Exception(f"start joint {start_joint} out of range for fkine calculation")
        if end_joint not in range(0,7):
            raise Exception(f"end joint {end_joint} out of range for fkine calculation")

        if not reverse:
            if end_joint - start_joint < 1:
                raise Exception(f"end joint {end_joint} is not ahead of start joint{start_joint} for forward fkine calculation")

            if start_joint == 0: # if start joint is 0, include base offset pose
                pose = self.__base_pose_offset
                start_joint += 1
            else: # else set pose of start joint to identity
                pose = np.eye(4) 

            for joint in range(start_joint, end_joint):
                if use_test_angles:
                    T = self.get_serial_transform(joint, joint_angle=self.test_joint_angles[joint-1])
                else:
                    T = self.get_serial_transform(joint)
                pose = np.matmul(pose, T)
            return pose

        else: #reverse selected
            if start_joint - end_joint < 1:
                raise Exception(f"end joint {end_joint} is not behind of start joint{start_joint} for reverse fkine calculation")

            pose = np.eye(4)

            if end_joint == 0: # if end joint is 0, must include inverse base offset pose at end of chain
                include_inv_base = True
                end_joint += 1
            else: # else set pose of start joint to identity
                include_inv_base = False

            for joint in range(start_joint, end_joint, -1): # start at joint just before end_joint, iterate backwards until you reach the end joint, inclusive
                if use_test_angles:
                    T_inv = self.get_serial_transform(joint, joint_angle=self.test_joint_angles[joint-1], inverse=True)
                else:
                    T_inv = self.get_serial_transform(joint, inverse=True)
                pose = np.matmul(pose, T_inv)

            if include_inv_base:
                pose = np.matmul(pose, self.__inv_base_pose_offset)
            return pose


    def ikine(self, pose):
        # given desired pose, return vector of 6 angles for theta
        
        # game plan:
        # find sphere location from desired pose
        # solve for corresponding angles for J1-J3
        # pass solved angles to fkine from J1 to J3 to extract orientation
        # find relative orientation between J3 and J6 desired
        # solve for J4-J6
        # check validity of joint angles
        # return joint angles

        # find sphere location:
        sphere_to_end_effector_dist = self.__dh_param[5,1]
        sphere_xyz = pose[:3, 3] - sphere_to_end_effector_dist * pose[:3, 2] # z axis of end effector

        # solve for J1-J3
        sphere_xyz_base = np.linalg.solve(self.__base_pose_offset, sphere_xyz.T) # put sphere location in frame of base instead of world
        x_b, y_b, z_b = sphere_xyz_base[:3,0]
        J1 = np.atan2(y_b, x_b)

        # r is radial dist of sphere location to J1 axis of rotation
        r = np.sqrt(np.power(x_b,2) + np.power(y_b,2))
        # d_z is height of sphere location - height of J2 axis
        d_z = z_b - self.__dh_param[5,1]

        # equations for solving for J2 and J3 from:
        # https://robotacademy.net.au/lesson/inverse-kinematics-for-a-2-joint-robot-arm-using-geometry/
        a1, a2 = self.__dh_param[1:3, 3]

        num = np.power(r,2) + np.power(d_z,2) - np.power(a1,2) - np.power(a2,2)
        den = 2 * a1 * a2
        q2 = np.arccos(num / den)

        num = a2 * np.sin(q2)
        den = a1 + a2*np.cos(q2)
        q1 = np.atan2(z_b, r) - np.atan2(num/den)

        J2 = q1
        J3 = q2

        return


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

    def __init__(self, RC_pipe, MC_pipe, ODSerialsPath):
        self.odrives = setup.import_odrives(ODSerialsPath)
        if len(self.odrives) != 3:
            raise Exception("Error importing odrives correctly. Expected 3 but received {}.".format(len(self.odrives)))

    def calib_axes(self, full_calib=True):
        for od_idx in range(len(self.odrives)):
            for axis in [0,1]:
                try:
                    setup.odrive_axis_calib(self.odrives[od_idx], axis, full_calib=full_calib)
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

# J2 and J3 map functions derived from math/screw_solution.jpg and annotated.png
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
        th = -joint_angle * np.pi/2 + np.pi/2 # this line is important, think about it
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
        max_step_degrees = 1
        max_step_radians = max_step_degrees * 180/np.pi

        if abs(current - prev) > max_step_radians:
            raise Exception("warning, change in joint angle exceeded {} in one step".format(current-prev))

    def set(self, J_vec):
        # J_vec is a 6 element np array of joint setpoints in order from J1-J6
        # this function takes a np array of rotational setpoints for the joints and sends commands to odrives accordingly
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


    def simple_set(self, M_pos, testing=False):
        # M_pos a 6 element row vector of wanted motor angles relative to startup
        # simpler set function that directly writes to each motor pos instead of joint angle used for debugging
        # do not call this function along with set from the same JC instance, the field variables will be messed up
        # please set testing=True to aknowledge this statement
        if not testing:
            return

        for motor in [1,2,3,4]:
            motor_setpoint = M_pos[motor-1]
            od_idx, axis = self.__J14_lookup[motor] # get corresponding odrive and axis for joint in question
            axis_object = setup.get_axis_object(self.odrives[od_idx], axis) # get odrive axis object to command motor
            axis_object.controller.input_pos = motor_setpoint

        J5_angle = M_pos[4]
        J6_angle = M_pos[5]
        M5_pos = 0
        M6_pos = 0
        M5_pos += J5_angle
        M6_pos += J5_angle
        M5_pos += J6_angle
        M6_pos -= J6_angle

        M5_axis = setup.get_axis_object(self.odrives[2], 0)
        M6_axis = setup.get_axis_object(self.odrives[2], 1)

        M5_axis.controller.input_pos = M5_pos
        M6_axis.controller.input_pos = M6_pos


# ------------------- Begin Test cases -------------------
if __name__ == "__main__":
    print('running test cases for motioncontroller')
    MC = MotionController(None, None)
    test_angles = np.zeros(6)
    MC.update_joint_angles(test_angles)
    print('retreiving DH param:')
    print(MC.get_DH())
    print()
    print('finding pose of each joint relative to base and respective inverse:')
    for joint in range(1,7):
        f = MC.fkine(0, joint)
        i = MC.fkine(joint, 0, reverse=True)
        print(f"Joint #{joint}")
        print('forward')
        print(f)
        print('reverse')
        print(i)
        print('actual inverse')
        print(np.linalg.inv(i))
        print('check')
        print((np.matmul(f, i)))
        print()
