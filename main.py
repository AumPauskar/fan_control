import subprocess
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

while True:
	temp = subprocess.check_output("vcgencmd measure_temp", shell=True).decode('utf-8')
	temp_value = float(temp[5:9])
	temp_value
	
	if temp_value > 50:
		GPIO.output(17, GPIO.HIGH)
		print("Fan on: ", temp_value)
	else:
		GPIO.output(17, GPIO.LOW)
		print("Fan off", temp_value)
	
	time.sleep(1)
