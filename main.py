import subprocess
import time
import RPi.GPIO as GPIO
import json

with open('config.json') as json_data_file:
	data = json.load(json_data_file)
	on_temp = data['on-temp']
	off_temp = data['off-temp']
	gpio = data['gpio']
	print(on_temp, off_temp, gpio)

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio, GPIO.OUT)
fan_on = False
while True:
	temp = subprocess.check_output("vcgencmd measure_temp", shell=True).decode('utf-8')
	temp_value = float(temp[5:9])
	
	if temp_value > on_temp:
		fan_on = True
	elif temp_value < off_temp:
		fan_on = False
	
	if fan_on:
		GPIO.output(gpio, GPIO.HIGH)
		print("Fan on: ", temp_value)
	else:
		GPIO.output(gpio, GPIO.LOW)
		print("Fan off", temp_value)
		
	# if temp_value > on_temp:
	# 	GPIO.output(17, GPIO.HIGH)
	# 	print("Fan on: ", temp_value)
	# else:
	# 	GPIO.output(gpio, GPIO.LOW)
	# 	print("Fan off", temp_value)
	
	time.sleep(1)
