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
devices = [hex(i) for i in i2c.scan()]
print('i2c devices',devices)

# for x,device in enumerate(devices):
#     try:
hex = 0x68
pca = PCA9685(i2c,address=hex)

for n,channel in enumerate(pca.channels):
    serv = servo.Servo(pca.channels[n])
    print(f'channel {n} - {serv.angle}')
    # except:
    #     print(f'errored out with device {device}')

# pca = PCA9685(i2c, address = 0x68)
pca.frequency = 60

for x, channel in enumerate(pca.channels):
    pca.channels[x].duty_cycle = 0x7FFF
