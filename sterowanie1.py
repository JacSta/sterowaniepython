import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import time


#GPIO.setmode(GPIO.BCM)
#SleepTimeL = 0.2

while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.IN)
    h,t = dht.read_retry(dht.DHT11, 2)

    if h<43.0:
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18, GPIO.LOW)
        time.sleep(5)
        GPIO.output(18, GPIO.LOW)
        print "ON"
        print 'Temp={0:0.1f}*C Humidity={1:0.1f}%' .format(t, h)
        #GPIO.cleanup()
        time.sleep(1)

    if h>43.0:
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(18, GPIO.HIGH)
        time.sleep(5)
        print "off"
        print 'Temp={0:0.1f}*C Humidity={1:0.1f}%' .format(t, h)
        #GPIO.cleanup()
        time.sleep(1)
        #dupa


#except KeyboardInterrupt:
   # print "Quit"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            