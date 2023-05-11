# # SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# # SPDX-License-Identifier: MIT

# # This simple test outputs a 50% duty cycle PWM single on the 0th channel. Connect an LED and
# # resistor in series to the pin to visualize duty cycle changes and its impact on brightness.

# from board import SCL, SDA
# import busio

# # Import the PCA9685 module.
# from adafruit_pca9685 import PCA9685

# # Create the I2C bus interface.
# i2c_bus = busio.I2C(SCL, SDA)

# # Create a simple PCA9685 class instance.
# pca = PCA9685(i2c_bus)

# # Set the PWM frequency to 60hz.
# pca.frequency = 60

# # Set the PWM duty cycle for channel zero to 50%. duty_cycle is 16 bits to match other PWM objects
# # but the PCA9685 will only actually give 12 bits of resolution.
# pca.channels[0].duty_cycle = 0x7FFF


from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685

from adafruit_motor import servo
i2c = busio.I2C(SCL, SDA)
print('i2c scan',i2c.scan())
pca = PCA9685(i2c,address=0x68)

for n,channel in enumerate(pca.channels):
    servo = servo.Servo(channel)
    print(f'channel {n} - {servo.angle}')

# pca = PCA9685(i2c, address = 0x68)
# pca.frequency = 60
# pca.channels[0].duty_cycle = 0x7FFF