import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pinData = 16
pinLatch = 20
pinClock = 21
GPIO.setup(pinData, GPIO.OUT)
GPIO.setup(pinLatch, GPIO.OUT)
GPIO.setup(pinClock, GPIO.OUT)

def setShiftRegister(value):
    bitValues = [128, 64, 32, 16, 8, 4, 2, 1]
    for x in range(8):
        hasBit = bitValues[x] == value & bitValues[x]
        GPIO.output(pinData, 1 if hasBit else 0)
        GPIO.output(pinClock, 1)
        GPIO.output(pinClock, 0)

for i in range(256):
    GPIO.output(pinLatch, 0)
    setShiftRegister(i)
    GPIO.output(pinLatch, 1)
    time.sleep(0.5) # Wait for 1 second


