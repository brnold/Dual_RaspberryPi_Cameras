#First, this was copied from,  https://learn.sparkfun.com/tutorials/raspberry-gpio/python-rpigpio-example, then modified
#
# Authored by Benjamin Nold
#
#This script should be launched at startup. Print somthing to screen for fun.
# Logic,
# Turn on LED for operation
# wait till button press
# Take Picture
# Flash LED
# Go untill other button is pressed, then shut down.
# Sould be simple, ya?

# Limitation, the Raspberry Pi has NO RTC, need I say more about file naming??

# External module imports
import RPi.GPIO as GPIO
import time
import os

#Camera Command line


#Make a new dir command
#Thanks, http://stackoverflow.com/questions/273192/in-python-check-if-a-directory-exists-and-create-it-if-necessary
def ensure_dir_cd_in(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
    os.chdir(d)

# Pin Definitons:
pwmPin = 18 # Broadcom pin 18 (P1 pin 12)
ledPin = 19 # Broadcom pin 19 (P1 pin 35)
cameraButton = 26 # Broadcom pin 26 (P1 pin 37)
shutdownButton # Broadcom pin ?

dc = 95 # duty cycle (0-100) for PWM pin

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output
GPIO.setup(pwmPin, GPIO.OUT) # PWM pin set as output
pwm = GPIO.PWM(pwmPin, 50)  # Initialize PWM on pwmPin 100Hz frequency
GPIO.setup(cameraButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(shutdownButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

# Initial state for LEDs:
GPIO.output(ledPin, GPIO.LOW)
pwm.start(dc)

##Setup done
print("Here we go! Press CTRL+C to exit, button shuts down the Pi (maybe")
try:
    while not GPIO.input(cameraButton): #wait for button depress

    currentTime = 'pic_' + time.strftime("%M_%S")
    ensure_dir_cd_in(currentTime) #hopefully in the directory now

    for x in range(0,3):  #Blick da LED
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(0.075)
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(0.075)

 #   while 1:
 #       if not GPIO.input(cameraButton): # camera button is pressed
 #           pwm.ChangeDutyCycle(dc)
 #           GPIO.output(ledPin, GPIO.LOW)
 #       elif not GPIO.input(shutdownButton): # shutdown button is pressed
 #           pwm.stop() # stop PWM
 #           GPIO.cleanup() # cleanup all GPIO
 #           os.system("sudo shutdown -h now") #this will abruptly halt now
 #       else: # button is pressed:
 #           pwm.ChangeDutyCycle(100-dc)
 #           GPIO.output(ledPin, GPIO.HIGH)
 #           time.sleep(0.075)
 #           GPIO.output(ledPin, GPIO.LOW)
 #           time.sleep(0.075)
>>>>>>> 8ad8b84504bffb07c06b633dbb1372e39bf8f384
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    pwm.stop() # stop PWM
    GPIO.cleanup() # cleanup all GPIO
