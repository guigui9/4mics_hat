import time
import signal
import sys
from pixels import Pixels, pixels
from alexa_led_pattern import AlexaLedPattern
from google_home_led_pattern import GoogleHomeLedPattern

def handler_stop_signals(_signo, _stack_frame):
    # Raises SystemExit(0):
    pixels.off()
    time.sleep(3)
    sys.exit(0)



if __name__ == '__main__':

    signal.signal(signal.SIGINT, handler_stop_signals)
    signal.signal(signal.SIGTERM, handler_stop_signals)
    pixels.pattern = GoogleHomeLedPattern(show=pixels.show)

    while True:
        try:
            pixels.wakeup()
            time.sleep(3)
            pixels.think()
            time.sleep(3)
            pixels.speak()
            time.sleep(6)
            pixels.off()
            time.sleep(3)
        except KeyboardInterrupt:
            break


    pixels.off()
    time.sleep(1)
