'''
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bash_profile
source ~/.bash_profile

'''

import board
import digitalio
import time

import pwmio
from adafruit_motor import servo

laser = digitalio.DigitalInOut(board.GPIO_P31)  # pin 31
laser.direction = digitalio.Direction.OUTPUT

def toggle_laser():
  laser.value = True
  time.sleep(2)
  laser.value = False
  print('done')

toggle_laser()
print('end script')
