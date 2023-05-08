# from periphery import I2C

# # Open i2c-0 controller
# i2c = I2C("/dev/i2c-1")

# # Read byte at address 0x100 of EEPROM at 0x50
# msgs = [I2C.Message([0x01, 0x00]), I2C.Message([0x00], read=True)]
# i2c.transfer(0x40, msgs)
# print("0x100: 0x{:02x}".format(msgs[1].data[0]))

# i2c.close()


from periphery import I2C

print(" Read 3 bytes starting at register address 0x1001 of EEPROM at I2C address 0x51 ")


# Open i2c-0 controller
i2c = I2C("/dev/i2c-1")

# create array to hold received data ( 3 bytes in my case )
dataRX = [0,0,0]

# create message to place 16 bits in memory register of eeprom
msgWritePointer = I2C.Message([0x10,0x01],read=False)

# create message to read data according to length of array 'dataRX'
msgRead = I2C.Message(dataRX,read=True)

# messages are assembled, order is important 
msgs = [msgWritePointer, msgRead]

# call transfer function 
i2c.transfer(0x40, msgs)

# print received bytes
for i in range(0,len(msgs[1].data)):
    print(hex(msgs[1].data[i]))

i2c.close()