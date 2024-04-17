import pifacedigitalio
import time
pf = pifacedigitalio.PiFaceDigital()
while True:
    input_state = pf.input_pins[1].value
    print(input_state)
    time.sleep(3)