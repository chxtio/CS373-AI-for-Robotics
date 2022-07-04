# -----------
# User Instructions
#
# Implement a P controller by running 100 iterations
# of robot motion. The desired trajectory for the 
# robot is the x-axis. The steering angle should be set
# by the parameter tau so that:
#
# steering = -tau * crosstrack_error
#
# You'll only need to modify the `run` function at the bottom.
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
robot = Robot()
robot.set(0.0, 1.0, 0.0)

def run(robot, tau, n=100, speed=1.0):
    x_trajectory = []
    y_trajectory = []
    # TODO: your code here
    

    for i in range(n):
        # print(robot.x, robot.y)
        cte = robot.y
        steer_angle = -tau * cte
        robot.move(steer_angle, speed)
        print(robot, steer_angle)
        print("\n")
        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)
        
    return x_trajectory, y_trajectory
    
x_trajectory, y_trajectory = run(robot, 0.1)
n = len(x_trajectory)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
ax1.plot(x_trajectory, y_trajectory, 'g', label='P controller')
ax1.plot(x_trajectory, np.zeros(n), 'r', label='reference')


# Output
# ([x=1.00000 y=0.99749 orient=6.27817], -0.1)

# ([x=1.99997 y=0.98997 orient=6.27316], -0.0997491638458655)

# ([x=2.99989 y=0.97747 orient=6.26820], -0.09899729506124687)

# ([x=3.99973 y=0.96003 orient=6.26330], -0.0977469440459231)

# ([x=4.99948 y=0.93774 orient=6.25848], -0.0960031957433074)

# ([x=5.99912 y=0.91068 orient=6.25378], -0.09377364753807171)

# ([x=6.99861 y=0.87900 orient=6.24921], -0.09106837322063087)

# ([x=7.99796 y=0.84283 orient=6.24481], -0.08789987335156867)

# ([x=8.99714 y=0.80235 orient=6.24058], -0.08428301247961656)

# ([x=9.99614 y=0.75775 orient=6.23656], -0.08023494377461873)

# ([x=10.99497 y=0.70925 orient=6.23277], -0.07577502172916582)

# ([x=11.99360 y=0.65707 orient=6.22921], -0.07092470365780627)

# ([x=12.99206 y=0.60149 orient=6.22592], -0.06570744077966993)

# ([x=13.99033 y=0.54275 orient=6.22291], -0.06014855970898907)

# ([x=14.98843 y=0.48116 orient=6.22020], -0.05427513519858849)

# ([x=15.98637 y=0.41701 orient=6.21779], -0.04811585498565592)

# ([x=16.98416 y=0.35062 orient=6.21570], -0.04170087757827332)

# ([x=17.98183 y=0.28231 orient=6.21395], -0.03506168379843757)

# ([x=18.97938 y=0.21242 orient=6.21254], -0.028230922864679542)

# ([x=19.97685 y=0.14130 orient=6.21147], -0.02124225375861215)

# ([x=20.97428 y=0.06965 orient=6.21077], -0.014130182577480355)

# ([x=21.97166 y=-0.00270 orient=6.21042], -0.006965132942895698)

# ([x=22.96901 y=-0.07541 orient=6.21043], 0.00027038891366995137)

# ([x=23.96637 y=-0.14810 orient=6.21081], 0.007540645276524681)

# ([x=24.96375 y=-0.22041 orient=6.21155], 0.014809553271809207)

# ([x=25.96122 y=-0.29143 orient=6.21265], 0.022040856550422525)

# ([x=26.95879 y=-0.36118 orient=6.21411], 0.029143327380779738)

# ([x=27.95647 y=-0.42930 orient=6.21592], 0.036118125383825375)

# ([x=28.95428 y=-0.49545 orient=6.21806], 0.042930097792873316)

# ([x=29.95224 y=-0.55929 orient=6.22054], 0.04954479013212563)

# ([x=30.95036 y=-0.62049 orient=6.22334], 0.05592861665386977)

# ([x=31.94866 y=-0.67875 orient=6.22645], 0.062049028300293685)

# ([x=32.94715 y=-0.73376 orient=6.22985], 0.0678746774674778)

# ([x=33.94582 y=-0.78523 orient=6.23352], 0.07337557879527594)

# ([x=34.94468 y=-0.83291 orient=6.23746], 0.07852326515236428)

# ([x=35.94373 y=-0.87654 orient=6.24163], 0.08329093793538789)

# ([x=36.94296 y=-0.91588 orient=6.24603], 0.08765361075776071)

# ([x=37.94235 y=-0.95074 orient=6.25062], 0.09158824557055995)

# ([x=38.94189 y=-0.98092 orient=6.25539], 0.09507388023884573)

# ([x=39.94157 y=-1.00625 orient=6.26031], 0.0980917465937722)

# ([x=40.94136 y=-1.02661 orient=6.26535], 0.10062537799705923)

# ([x=41.94124 y=-1.04186 orient=6.27051], 0.10266070549062078)

# ([x=42.94119 y=-1.05193 orient=6.27573], 0.1041861416619156)

# ([x=43.94118 y=-1.05674 orient=6.28101], 0.10519265143439327)

# ([x=44.94118 y=-1.05626 orient=0.00313], 0.10567380909136831)

# ([x=45.94116 y=-1.05048 orient=0.00843], 0.10562584095915782)

# ([x=46.94110 y=-1.03941 orient=0.01370], 0.10504765330828719)

# ([x=47.94096 y=-1.02310 orient=0.01892], 0.10394084517668034)

# ([x=48.94073 y=-1.00161 orient=0.02405], 0.10230970597212946)

# ([x=49.94038 y=-0.97505 orient=0.02908], 0.10016119786812681)

# ([x=50.93988 y=-0.94353 orient=0.03397], 0.09750492316309477)

# ([x=51.93922 y=-0.90720 orient=0.03870], 0.09435307692322965)

# ([x=52.93838 y=-0.86624 orient=0.04325], 0.09072038536945969)

# ([x=53.93735 y=-0.82084 orient=0.04759], 0.08662403059544772)

# ([x=54.93611 y=-0.77121 orient=0.05170], 0.08208356231274366)

# ([x=55.93467 y=-0.71760 orient=0.05557], 0.07712079740921354)

# ([x=56.93303 y=-0.66026 orient=0.05916], 0.07175970817544908)

# ([x=57.93118 y=-0.59948 orient=0.06247], 0.06602630010119129)

# ([x=58.92913 y=-0.53556 orient=0.06547], 0.0599484801696292)

# ([x=59.92690 y=-0.46880 orient=0.06815], 0.05355591658336607)

# ([x=60.92450 y=-0.39953 orient=0.07050], 0.04687989084377478)

# ([x=61.92195 y=-0.32810 orient=0.07249], 0.03995314307781542)

# ([x=62.91926 y=-0.25485 orient=0.07414], 0.03280971146716638)

# ([x=63.91646 y=-0.18014 orient=0.07541], 0.025484766586009757)

# ([x=64.91362 y=-0.10481 orient=0.07631], 0.018014441401032855)

# ([x=65.91071 y=-0.02857 orient=0.07684], 0.010480569580342894)

# ([x=66.90776 y=0.04819 orient=0.07698], 0.002856874889775428)

# ([x=67.90480 y=0.12509 orient=0.07674], -0.004819071006171856)

# ([x=68.90186 y=0.20175 orient=0.07611], -0.012509259092914088)

# ([x=69.89900 y=0.27729 orient=0.07510], -0.020175422770042084)

# ([x=70.89623 y=0.35163 orient=0.07372], -0.02772891882232216)

# ([x=71.89358 y=0.42440 orient=0.07196], -0.03516296594604001)

# ([x=72.89107 y=0.49524 orient=0.06983], -0.042440155080760184)

# ([x=73.88872 y=0.56378 orient=0.06736], -0.04952373709194831)

# ([x=74.88654 y=0.62967 orient=0.06453], -0.05637780328932536)

# ([x=75.88456 y=0.69259 orient=0.06138], -0.06296746381467529)

# ([x=76.88278 y=0.75220 orient=0.05791], -0.06925902317998976)

# ([x=77.88121 y=0.80820 orient=0.05414], -0.07522015217126068)

# ([x=78.87986 y=0.86030 orient=0.05009], -0.08082005526579224)

# ([x=79.87871 y=0.90822 orient=0.04578], -0.08602963264552842)

# ([x=80.87776 y=0.95171 orient=0.04123], -0.09082163582916394)

# ([x=81.87700 y=0.99054 orient=0.03646], -0.09517081589671933)

# ([x=82.87643 y=1.02451 orient=0.03149], -0.099054063244742)

# ([x=83.87601 y=1.05342 orient=0.02635], -0.10245053779285627)

# ([x=84.87572 y=1.07712 orient=0.02106], -0.10534178856535165)

# ([x=85.87555 y=1.09547 orient=0.01565], -0.10771186159780939)

# ([x=86.87547 y=1.10838 orient=0.01015], -0.10954739516936059)

# ([x=87.87544 y=1.11575 orient=0.00459], -0.11083770143698929)

# ([x=88.87544 y=1.11754 orient=6.28217], -0.11157483364821985)

# ([x=89.87543 y=1.11372 orient=6.27656], -0.11175363823138298)

# ([x=90.87538 y=1.10430 orient=6.27097], -0.1113717912050447)

# ([x=91.87527 y=1.08931 orient=6.26543], -0.11042981850702348)

# ([x=92.87506 y=1.06882 orient=6.25996], -0.10893110001356945)

# ([x=93.87472 y=1.04291 orient=6.25459], -0.1068818571960975)

# ([x=94.87423 y=1.01171 orient=6.24936], -0.104291124540498)

# ([x=95.87357 y=0.97535 orient=6.24428], -0.10117070502734862)

# ([x=96.87272 y=0.93401 orient=6.23939], -0.0975351101346206)

# ([x=97.87165 y=0.88790 orient=6.23471], -0.09340148497322787)

# ([x=98.87037 y=0.83721 orient=6.23026], -0.08878951929553125)

# ([x=99.86885 y=0.78221 orient=6.22606], -0.08372134522491592)
