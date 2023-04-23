'''
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bash_profile
source ~/.bash_profile

'''

import board
import digitalio
import time

import pwmio
from adafruit_motor import servo

# laser = digitalio.DigitalInOut(board.GPIO_P31)  # pin 31
# laser.direction = digitalio.Direction.OUTPUT

# def toggle_laser():
#     laser.value = True
#     time.sleep(2)
#     laser.value = False
#     print('done')

# toggle_laser()
# print('end script')

v_angle_change = 0
v_current_angle = 0
v_next_angle = 180
h_angle_change = 0
h_current_angle = 0
h_next_angle = 180

pmw_h = pwmio.PWMOut(board.PWM1, duty_cycle=2 ** 15, frequency=50)
pmw_v = pwmio.PWMOut(board.PWM2, duty_cycle=2 ** 15, frequency=50)

servo_h = servo.Servo(pmw_h)
servo_v = servo.Servo(pmw_v)

def servo_h_move():
    for angle in range(h_current_angle, h_next_angle, 5):  # 0 - 180 degrees, 5 degrees at a time.
        servo_h.angle = angle
        time.sleep(0.05)
    for angle in range(h_next_angle, h_current_angle, -5): # 180 - 0 degrees, 5 degrees at a time.
        servo_h.angle = angle
        time.sleep(0.05)

def servo_v_move():
    for angle in range(v_current_angle, v_next_angle, 5):  # 0 - 180 degrees, 5 degrees at a time.
        servo_h.angle = angle
        time.sleep(0.05)
    for angle in range(v_next_angle, v_current_angle, -5): # 180 - 0 degrees, 5 degrees at a time.
        servo_h.angle = angle
        time.sleep(0.05)

servo_h_move()
# servo_v_move()
