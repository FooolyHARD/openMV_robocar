tim = pyb.Timer(2, freq = 50)
motorPin1 = tim.channel(3, pyb.Timer.PWM, pin=pyb.Pin('P4'))
motorPin2 = tim.channel(4, pyb.Timer.PWM, pin=pyb.Pin('P5'))

def drive(x):
    if x > 0:
        motorPin1.pulse_width_percent(x)
        motorPin2.pulse_width_percent(0)
    elif x < 0:
        motorPin1.pulse_width_percent(0)
        motorPin2.pulse_width_percent(-x)
    else:
        motorPin1.pulse_width_percent(100)
        motorPin2.pulse_width_percent(100)

