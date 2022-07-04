# -----------
# User Instructions
#
# Implement a P controller by running 100 iterations
# of robot motion. The steering angle should be set
# by the parameter tau so that:
#
# steering = -tau_p * CTE - tau_d * diff_CTE - tau_i * int_CTE
#
# where the integrated crosstrack error (int_CTE) is
# the sum of all the previous crosstrack errors.
# This term works to cancel out steering drift.
#
# Only modify code at the bottom! Look for the TODO.
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
robot.set(0, 1, 0)


def run(robot, tau_p, tau_d, tau_i, n=100, speed=1.0):
    x_trajectory = []
    y_trajectory = []
    # TODO: your code here
    prev_CTE = robot.y
    int_CTE = 0
    
    for i in range(n):
        CTE = robot.y
        diff_CTE = CTE - prev_CTE
        int_CTE += CTE
        steering = -tau_p * CTE - tau_d * diff_CTE - tau_i * int_CTE
        robot.move(steering, speed)
        print(robot, steering)
        print("\n")
        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)
        prev_CTE = CTE
    
    return x_trajectory, y_trajectory


x_trajectory, y_trajectory = run(robot, 0.2, 3.0, 0.004)
n = len(x_trajectory)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,8))
ax1.plot(x_trajectory, y_trajectory, 'g', label='PID controller')
ax1.plot(x_trajectory, np.zeros(n), 'r', label='reference')

# Output
# ([x=0.99998 y=0.99483 orient=6.27284], -0.20400000000000001)

# ([x=1.99986 y=0.97964 orient=6.26315], -0.19142923576598847)

# ([x=2.99957 y=0.95552 orient=6.25497], -0.1622609148137744)

# ([x=3.99907 y=0.92392 orient=6.24820], -0.13445076656467847)

# ([x=4.99836 y=0.88620 orient=6.24271], -0.1094135896512779)

# ([x=5.99744 y=0.84356 orient=6.23835], -0.08704155997177565)

# ([x=6.99636 y=0.79706 orient=6.23499], -0.0671154160273751)

# ([x=7.99514 y=0.74764 orient=6.23251], -0.04942890613023965)

# ([x=8.99381 y=0.69615 orient=6.23082], -0.033794998608896905)

# ([x=9.99242 y=0.64331 orient=6.22982], -0.020042784916327383)

# ([x=10.99099 y=0.58997 orient=6.22942], -0.008014644580754425)

# ([x=11.98955 y=0.53623 orient=6.22951], 0.0017947252970616084)

# ([x=12.98811 y=0.48258 orient=6.23009], 0.01159828926778493)

# ([x=13.98672 y=0.43001 orient=6.23110], 0.020129214047619574)

# ([x=14.98540 y=0.37858 orient=6.23238], 0.025677754692896883)

# ([x=15.98415 y=0.32857 orient=6.23393], 0.03101685817970573)

# ([x=16.98298 y=0.28023 orient=6.23570], 0.03545651976581493)

# ([x=17.98190 y=0.23374 orient=6.23766], 0.039023948615115926)

# ([x=18.98091 y=0.18927 orient=6.23975], 0.041804151499698336)

# ([x=19.98001 y=0.14694 orient=6.24194], 0.04388148769562539)

# ([x=20.97921 y=0.10685 orient=6.24421], 0.04533468311811233)

# ([x=21.97849 y=0.06904 orient=6.24653], 0.04623660412460057)

# ([x=22.97786 y=0.03356 orient=6.24886], 0.04665446066775539)

# ([x=23.97731 y=0.00040 orient=6.25119], 0.0466500543421915)

# ([x=24.97684 y=-0.03042 orient=6.25351], 0.04628003655083338)

# ([x=25.97643 y=-0.05896 orient=6.25579], 0.04559617219416336)

# ([x=26.97609 y=-0.08523 orient=6.25803], 0.044645606487083885)

# ([x=27.97580 y=-0.10930 orient=6.26020], 0.04347113252235485)

# ([x=28.97556 y=-0.13123 orient=6.26231], 0.04211145725736568)

# ([x=29.97536 y=-0.15109 orient=6.26434], 0.0406014637753752)

# ([x=30.97520 y=-0.16896 orient=6.26629], 0.03897246793766689)

# ([x=31.97507 y=-0.18493 orient=6.26815], 0.037252467860220885)

# ([x=32.97497 y=-0.19907 orient=6.26993], 0.03546638493846066)

# ([x=33.97489 y=-0.21149 orient=6.27161], 0.0336362954641655)

# ([x=34.97483 y=-0.22228 orient=6.27320], 0.031781652130033845)

# ([x=35.97479 y=-0.23151 orient=6.27469], 0.029919494954392202)

# ([x=36.97476 y=-0.23930 orient=6.27610], 0.02806465136997084)

# ([x=37.97474 y=-0.24574 orient=6.27741], 0.02622992537225636)

# ([x=38.97473 y=-0.25090 orient=6.27863], 0.02442627577009862)

# ([x=39.97472 y=-0.25489 orient=6.27976], 0.02266298367958243)

# ([x=40.97472 y=-0.25779 orient=6.28081], 0.020947809489275736)

# ([x=41.97471 y=-0.26016 orient=6.28178], 0.019287139591502724)

# ([x=42.97471 y=-0.26157 orient=6.28274], 0.01923121138782622)

# ([x=43.97471 y=-0.26202 orient=0.00044], 0.017665910322467226)

# ([x=44.97471 y=-0.26158 orient=0.00123], 0.01591845207415389)

# ([x=45.97471 y=-0.26035 orient=0.00194], 0.014227446811876189)

# ([x=46.97471 y=-0.25841 orient=0.00258], 0.012634509812938483)

# ([x=47.97471 y=-0.25583 orient=0.00313], 0.0111452262127495)

# ([x=48.97470 y=-0.25270 orient=0.00362], 0.009758276884906138)

# ([x=49.97469 y=-0.24908 orient=0.00404], 0.008470768060203741)

# ([x=50.97469 y=-0.24504 orient=0.00441], 0.007279259708242676)

# ([x=51.97468 y=-0.24063 orient=0.00472], 0.00618001055965333)

# ([x=52.97466 y=-0.23591 orient=0.00498], 0.0051690749997274875)

# ([x=53.97465 y=-0.23094 orient=0.00519], 0.004242366984839357)

# ([x=54.97464 y=-0.22575 orient=0.00536], 0.0033957122811194285)

# ([x=55.97462 y=-0.22039 orient=0.00549], 0.002624893363026997)

# ([x=56.97461 y=-0.21490 orient=0.00558], 0.0019256882186672389)

# ([x=57.97459 y=-0.20932 orient=0.00565], 0.001293903721260252)

# ([x=58.97458 y=-0.20367 orient=0.00569], 0.0007254040915871153)

# ([x=59.97456 y=-0.19798 orient=0.00570], 0.00021613492459422387)

# ([x=60.97455 y=-0.19229 orient=0.00568], -0.00023785678213844239)

# ([x=61.97453 y=-0.18660 orient=0.00565], -0.0006404061917737319)

# ([x=62.97451 y=-0.18095 orient=0.00560], -0.0009952174066890085)

# ([x=63.97450 y=-0.17535 orient=0.00554], -0.0013058531134111373)

# ([x=64.97448 y=-0.16981 orient=0.00546], -0.0015757267721407675)

# ([x=65.97447 y=-0.16435 orient=0.00537], -0.0018080970544438954)

# ([x=66.97445 y=-0.15898 orient=0.00527], -0.0020060642568301146)

# ([x=67.97444 y=-0.15372 orient=0.00516], -0.002172568440792711)

# ([x=68.97443 y=-0.14856 orient=0.00504], -0.0023103890714703985)

# ([x=69.97441 y=-0.14351 orient=0.00492], -0.0024221459474174194)

# ([x=70.97440 y=-0.13859 orient=0.00480], -0.002510301233063776)

# ([x=71.97439 y=-0.13379 orient=0.00467], -0.002577162423334483)

# ([x=72.97438 y=-0.12912 orient=0.00454], -0.0026248860866099864)

# ([x=73.97437 y=-0.12459 orient=0.00440], -0.0026554822477752524)

# ([x=74.97436 y=-0.12018 orient=0.00427], -0.002670819287571114)

# ([x=75.97435 y=-0.11591 orient=0.00414], -0.0026726292478571126)

# ([x=76.97434 y=-0.11177 orient=0.00400], -0.002662513444776207)

# ([x=77.97433 y=-0.10777 orient=0.00387], -0.0026419483032105017)

# ([x=78.97433 y=-0.10390 orient=0.00374], -0.0026122913363933672)

# ([x=79.97432 y=-0.10016 orient=0.00361], -0.0025747872041331533)

# ([x=80.97431 y=-0.09654 orient=0.00349], -0.0025305737918651407)

# ([x=81.97431 y=-0.09306 orient=0.00336], -0.002480688260722024)

# ([x=82.97430 y=-0.08970 orient=0.00324], -0.0024260730260516564)

# ([x=83.97430 y=-0.08646 orient=0.00312], -0.0023675816283590546)

# ([x=84.97429 y=-0.08333 orient=0.00301], -0.002305984466553319)

# ([x=85.97429 y=-0.08033 orient=0.00289], -0.00224197436868653)

# ([x=86.97428 y=-0.07743 orient=0.00279], -0.002176171980118805)

# ([x=87.97428 y=-0.07465 orient=0.00268], -0.00210913095327909)

# ([x=88.97427 y=-0.07197 orient=0.00258], -0.0020413429269508093)

# ([x=89.97427 y=-0.06939 orient=0.00248], -0.0019732422863327752)

# ([x=90.97427 y=-0.06691 orient=0.00238], -0.001905210698048089)

# ([x=91.97426 y=-0.06452 orient=0.00229], -0.001837581416826539)

# ([x=92.97426 y=-0.06223 orient=0.00220], -0.001770643362806806)

# ([x=93.97426 y=-0.06003 orient=0.00212], -0.001704644970316799)

# ([x=94.97426 y=-0.05791 orient=0.00204], -0.0016397978106300233)

# ([x=95.97426 y=-0.05587 orient=0.00196], -0.0015762799925819393)

# ([x=96.97425 y=-0.05391 orient=0.00188], -0.001514239346092884)

# ([x=97.97425 y=-0.05203 orient=0.00181], -0.0014537963946028637)

# ([x=98.97425 y=-0.05022 orient=0.00174], -0.0013950471232017482)

# ([x=99.97425 y=-0.04848 orient=0.00167], -0.0013380655498537062)


