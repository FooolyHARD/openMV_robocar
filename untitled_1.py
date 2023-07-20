# Untitled - By: shizlong - чт июл. 20 2023

import pyb, time
centerAngle = 7
leftAngle = -14
rightAngle = 24


servo1 = pyb.Servo(1)
servo1.angle(7)
time.sleep(1)

tim = pyb.Timer(2, freq = 50)
motorPin1 = tim.channel(3, pyb.Timer.PWM, pin=pyb.Pin('P4'))
motorPin2 = tim.channel(4, pyb.Timer.PWM, pin=pyb.Pin('P5'))

motorPin1.pulse_width_percent(0)
motorPin2.pulse_width_percent(10)
time.sleep(1)
motorPin1.pulse_width_percent(100)
motorPin2.pulse_width_percent(100)
time.sleep(1)
