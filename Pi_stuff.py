import RPi.GPIO as GPIO
import time
# use P1 header pin numbering convention
GPIO.setmode(GPIO.BOARD)

# Set up the GPIO channels - one input and one output
GPIO.setup(4, GPIO.IN)
while True:
    input_value = GPIO.input(4)
    print(input_value)
    time.sleep(3)
