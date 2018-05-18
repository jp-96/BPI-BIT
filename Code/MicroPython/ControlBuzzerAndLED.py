
from machine import Pin, PWM
import random

LED0 = Pin(18, Pin.OUT)
pwm0 = PWM(Pin(25))      # create PWM object from a pin

print("bpibit LED0 And Buzzer")

while True:
	LED0.value(0) # 低电平 熄灯
	print('pwm0.freq ' + str(pwm0.freq()))            # get current frequency
	pwm0.freq(int(random.randint(0, 5000)))         # set frequency
	print('pwm0.duty ' + str(pwm0.duty()))             # get current duty cycle
	pwm0.duty(int(random.randint(0, 1024)))         # set duty cycle
	# pwm0.deinit()           # turn off PWM on the pin
	LED0.value(1) # 高电平 亮灯
