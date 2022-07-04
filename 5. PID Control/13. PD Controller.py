# -----------
# User Instructions
#
# Implement a PD controller by running 100 iterations
# of robot motion. The steering angle should be set
# by the parameter tau_p and tau_d so that:
#
# steering = -tau_p * CTE - tau_d * diff_CTE
# where differential crosstrack error (diff_CTE)
# is given by CTE(t) - CTE(t-1)
#
#
# Only modify code at the bottom! Look for the TODO
# ------------
 
import random
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------
# 
# this is the Robot class
#

class Robot(object):
    def __init__(self, length=20.0):
        """
        Creates robot and initializes location/orientation to 0, 0, 0.
        """
        self.x = 0.0
        self.y = 0.0
        self.orientation = 0.0
        self.length = length
        self.steering_noise = 0.0
        self.distance_noise = 0.0
        self.steering_drift = 0.0

    def set(self, x, y, orientation):
        """
        Sets a robot coordinate.
        """
        self.x = x
        self.y = y
        self.orientation = orientation % (2.0 * np.pi)

    def set_noise(self, steering_noise, distance_noise):
        """
        Sets the noise parameters.
        """
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.steering_noise = steering_noise
        self.distance_noise = distance_noise

    def set_steering_drift(self, drift):
        """
        Sets the systematical steering drift parameter
        """
        self.steering_drift = drift

    def move(self, steering, distance, tolerance=0.001, max_steering_angle=np.pi / 4.0):
        """
        steering = front wheel steering angle, limited by max_steering_angle
        distance = total distance driven, most be non-negative
        """
        if steering > max_steering_angle:
            steering = max_steering_angle
        if steering < -max_steering_angle:
            steering = -max_steering_angle
        if distance < 0.0:
            distance = 0.0

        # apply noise
        steering2 = random.gauss(steering, self.steering_noise)
        distance2 = random.gauss(distance, self.distance_noise)

        # apply steering drift
        steering2 += self.steering_drift

        # Execute motion
        turn = np.tan(steering2) * distance2 / self.length

        if abs(turn) < tolerance:
            # approximate by straight line motion
            self.x += distance2 * np.cos(self.orientation)
            self.y += distance2 * np.sin(self.orientation)
            self.orientation = (self.orientation + turn) % (2.0 * np.pi)
        else:
            # approximate bicycle model for motion
            radius = distance2 / turn
            cx = self.x - (np.sin(self.orientation) * radius)
            cy = self.y + (np.cos(self.orientation) * radius)
            self.orientation = (self.orientation + turn) % (2.0 * np.pi)
            self.x = cx + (np.sin(self.orientation) * radius)
            self.y = cy - (np.cos(self.orientation) * radius)

    def __repr__(self):
        return '[x=%.5f y=%.5f orient=%.5f]' % (self.x, self.y, self.orientation)

############## ADD / MODIFY CODE BELOW ####################
# ------------------------------------------------------------------------
#
# run - does a single control run

# previous P controller
def run_p(robot, tau, n=100, speed=1.0):
    x_trajectory = []
    y_trajectory = []
    for i in range(n):
        cte = robot.y
        steer = -tau * cte
        robot.move(steer, speed)
        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)
    return x_trajectory, y_trajectory
    
robot = Robot()
robot.set(0, 1, 0)

def run(robot, tau_p, tau_d, n=100, speed=1.0):
    x_trajectory = []
    y_trajectory = []
    # TODO: your code here
    prev_CTE = robot.y
    
    for i in range(n):
        CTE = robot.y
        diff_CTE = CTE - prev_CTE
        steering = -tau_p * CTE - tau_d * diff_CTE
        robot.move(steering, speed)
        print(robot, steering)
        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)
        prev_CTE = CTE
    
    return x_trajectory, y_trajectory
    
x_trajectory, y_trajectory = run(robot, 0.2, 3.0)
n = len(x_trajectory)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
ax1.plot(x_trajectory, y_trajectory, 'g', label='PD controller')
ax1.plot(x_trajectory, np.zeros(n), 'r', label='reference')


# Output
# ([x=0.99998 y=0.99493 orient=6.27305], -0.2) ([x=1.99987 y=0.98015 orient=6.26376], -0.18378333598598148) ([x=2.99960 y=0.95690 orient=6.25611], -0.1516842775874949) ([x=3.99914 y=0.92678 orient=6.25000], -0.1216337420201711) ([x=4.99851 y=0.89122 orient=6.24524], -0.0949841761939183) ([x=5.99772 y=0.85149 orient=6.24165], -0.07156814197837777) ([x=6.99680 y=0.80869 orient=6.23910], -0.05110895139499122) ([x=7.99579 y=0.76378 orient=6.23743], -0.03334383824482076) ([x=8.99475 y=0.71804 orient=6.23653], -0.018029917957323977) ([x=9.99366 y=0.67140 orient=6.23621], -0.006382375627704218) ([x=10.99255 y=0.62444 orient=6.23649], 0.005648026914503668) ([x=11.99146 y=0.57776 orient=6.23729], 0.01599661085355987) ([x=12.99044 y=0.53249 orient=6.23851], 0.024486171690353914) ([x=13.98947 y=0.48856 orient=6.23998], 0.02930782454118365) ([x=14.98858 y=0.44622 orient=6.24168], 0.034061229012650074) ([x=15.98775 y=0.40568 orient=6.24357], 0.037779634095909384) ([x=16.98701 y=0.36709 orient=6.24560], 0.040503090305401196) ([x=17.98634 y=0.33057 orient=6.24772], 0.04235139554591569) ([x=18.98575 y=0.29619 orient=6.24989], 0.04344183651052162) ([x=19.98523 y=0.26400 orient=6.25209], 0.04388218388855875) ([x=20.98478 y=0.23401 orient=6.25428], 0.04377043823380972) ([x=21.98440 y=0.20618 orient=6.25644], 0.04319521963426495) ([x=22.98407 y=0.18049 orient=6.25855], 0.042236248296967455) ([x=23.98379 y=0.15689 orient=6.26060], 0.04096485719409202) ([x=24.98355 y=0.13529 orient=6.26257], 0.03944452219940331) ([x=25.98336 y=0.11562 orient=6.26446], 0.037731399893982595) ([x=26.98320 y=0.09780 orient=6.26626], 0.03587486476361619) ([x=27.98307 y=0.08172 orient=6.26795], 0.033918038844831244) ([x=28.98297 y=0.06728 orient=6.26955], 0.03189830821233954) ([x=29.98288 y=0.05439 orient=6.27104], 0.029847821892485624) ([x=30.98282 y=0.04294 orient=6.27243], 0.027793969903473225) ([x=31.98277 y=0.03283 orient=6.27372], 0.025759838032490733) ([x=32.98273 y=0.02396 orient=6.27491], 0.023764637763156314) ([x=33.98270 y=0.01623 orient=6.27600], 0.02182411039730141) ([x=34.98267 y=0.00904 orient=6.27700], 0.01995090494121996) ([x=35.98265 y=0.00285 orient=6.27798], 0.01975117642232451) ([x=36.98264 y=-0.00235 orient=6.27888], 0.017995972518009263) ([x=37.98263 y=-0.00665 orient=6.27969], 0.016073186575157786) ([x=38.98262 y=-0.01015 orient=6.28040], 0.01423378036594168) ([x=39.98262 y=-0.01293 orient=6.28103], 0.012522119197073118) ([x=40.98262 y=-0.01509 orient=6.28157], 0.010944077878629423) ([x=41.98262 y=-0.01671 orient=6.28205], 0.00949759959243894) ([x=42.98262 y=-0.01784 orient=6.28246], 0.008178412357118185) ([x=43.98261 y=-0.01857 orient=6.28281], 0.006981239228902848) ([x=44.98261 y=-0.01895 orient=6.28310], 0.005900172943412628) ([x=45.98261 y=-0.01904 orient=0.00016], 0.004928879074386568) ([x=46.98261 y=-0.01887 orient=0.00036], 0.004060749339671447) ([x=47.98261 y=-0.01851 orient=0.00053], 0.003289028753839875) ([x=48.98261 y=-0.01798 orient=0.00066], 0.0026069225719359823) ([x=49.98261 y=-0.01732 orient=0.00076], 0.0020076856718467097) ([x=50.98261 y=-0.01656 orient=0.00083], 0.0014846963315628433) ([x=51.98261 y=-0.01573 orient=0.00089], 0.0010315161354998922) ([x=52.98261 y=-0.01484 orient=0.00092], 0.0006419376067767534) ([x=53.98261 y=-0.01392 orient=0.00093], 0.0003100210414547083) ([x=54.98261 y=-0.01299 orient=0.00094], 3.012190467312041e-05) ([x=55.98261 y=-0.01205 orient=0.00092], -0.00020308996400429397) ([x=56.98261 y=-0.01113 orient=0.00091], -0.00039461819754853895) ([x=57.98261 y=-0.01022 orient=0.00088], -0.0005491337667265562) ([x=58.98261 y=-0.00934 orient=0.00084], -0.0006709739292990705) ([x=59.98261 y=-0.00850 orient=0.00081], -0.0007641454231999689) ([x=60.98261 y=-0.00769 orient=0.00076], -0.000832331152651594) ([x=61.98261 y=-0.00693 orient=0.00072], -0.0008788996994089212) ([x=62.98261 y=-0.00621 orient=0.00068], -0.000906917068816359) ([x=63.98261 y=-0.00554 orient=0.00063], -0.0009191601521076076) ([x=64.98261 y=-0.00491 orient=0.00058], -0.0009181314524563649) ([x=65.98261 y=-0.00432 orient=0.00054], -0.0009060746828253301) ([x=66.98261 y=-0.00378 orient=0.00049], -0.0008849908988427996) ([x=67.98261 y=-0.00329 orient=0.00045], -0.0008566548799775771) ([x=68.98261 y=-0.00284 orient=0.00041], -0.0008226315174287078) ([x=69.98261 y=-0.00243 orient=0.00037], -0.0007842920076634441) ([x=70.98261 y=-0.00206 orient=0.00033], -0.00074282968670335) ([x=71.98261 y=-0.00173 orient=0.00030], -0.0006992753723618858) ([x=72.98261 y=-0.00143 orient=0.00027], -0.000654512109966008) ([x=73.98261 y=-0.00116 orient=0.00024], -0.0006092892419367608) ([x=74.98261 y=-0.00093 orient=0.00021], -0.0005642357432417142) ([x=75.98261 y=-0.00072 orient=0.00018], -0.0005198727834395689) ([x=76.98261 y=-0.00054 orient=0.00016], -0.0004766254920785352) ([x=77.98261 y=-0.00038 orient=0.00014], -0.00043483391783759236) ([x=78.98261 y=-0.00025 orient=0.00012], -0.00039476318325299705) ([x=79.98261 y=-0.00013 orient=0.00010], -0.0003566128463773044) ([x=80.98261 y=-0.00003 orient=0.00008], -0.00032052548848637114) ([x=81.98261 y=0.00005 orient=0.00007], -0.0002865945531785926) ([x=82.98261 y=0.00012 orient=0.00005], -0.00025487146708287655) ([x=83.98261 y=0.00017 orient=0.00004], -0.0002253720760762683) ([x=84.98261 y=0.00021 orient=0.00003], -0.0001980824335634833) ([x=85.98261 y=0.00025 orient=0.00002], -0.0001729639791302627) ([x=86.98261 y=0.00027 orient=0.00002], -0.00014995814687889376) ([x=87.98261 y=0.00029 orient=0.00001], -0.0001289904431036041) ([x=88.98261 y=0.00030 orient=0.00001], -0.0001099740327703729) ([x=89.98261 y=0.00031 orient=0.00000], -9.281287362357179e-05) ([x=90.98261 y=0.00031 orient=6.28318], -7.740443573406394e-05) ([x=91.98261 y=0.00030 orient=6.28318], -6.364204300371471e-05) ([x=92.98261 y=0.00030 orient=6.28318], -5.141687161511799e-05) ([x=93.98261 y=0.00029 orient=6.28317], -4.0619638715956026e-05) ([x=94.98261 y=0.00028 orient=6.28317], -3.114201281286436e-05) ([x=95.98261 y=0.00026 orient=6.28317], -2.2877775460569867e-05) ([x=96.98261 y=0.00025 orient=6.28317], -1.5723761867998605e-05) ([x=97.98261 y=0.00024 orient=6.28317], -9.580606125644955e-06) ([x=98.98261 y=0.00022 orient=6.28317], -4.35331480381655e-06) ([x=99.98261 y=0.00021 orient=6.28317], 4.830921768148619e-08)
