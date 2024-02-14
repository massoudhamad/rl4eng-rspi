import time
import RPi.GPIO as GPIO

# use pin numbers RPi.GPIO Layout
GPIO.setmode(GPIO.BOARD)

# Pin 11 (GPIO 17) Output 
GPIO.setup(11, GPIO.OUT)

# Pin 13 (GPIO 27) Output 
GPIO.setup(13, GPIO.OUT)

# Pin 15 (GPIO 22)  Output 
GPIO.setup(15, GPIO.OUT)


# switch off LEDs
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.LOW)

# test all LEDs
GPIO.output(11, GPIO.HIGH)
time.sleep(5)
GPIO.output(11, GPIO.LOW)
time.sleep(2)
GPIO.output(13, GPIO.HIGH)
time.sleep(5)
GPIO.output(13, GPIO.LOW)
time.sleep(2)
GPIO.output(15, GPIO.HIGH)
time.sleep(5)
GPIO.output(15, GPIO.LOW)

# release GPIOs before leaving program
GPIO.cleanup()
