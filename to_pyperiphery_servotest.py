from periphery import PWM

pwm = PWM(0,0)
pwm.frequency = 50
pwm.duty_cycle= 0.75
pwm.enable()

print(pwm.period)
print(pwm.frequency)
print(pwm.enabled)
pwm.duty_cycle = 0.50
pwm.close()
print("done")
