import RPi.GPIO as GPIO
import time

class Distance_Sensor:

    def __init__(self):
        
        GPIO.setmode(GPIO.BCM)
 
        self.GPIO_TRIGGER = 23
        self.GPIO_ECHO = 24
                
        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)

    def get_distance(self):
        GPIO.output(self.GPIO_TRIGGER, True)
    
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)
    
        StartTime = time.time()
        StopTime = time.time()
    
        while GPIO.input(self.GPIO_ECHO) == 0:
            StartTime = time.time()
    
        # save time of arrival
        while GPIO.input(self.GPIO_ECHO) == 1:
            StopTime = time.time()
    
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
    
        return distance

if __name__ == "__main__":
    
    mySensor = Distance_Sensor()

    while (True):
        distance = mySensor.get_distance()
        print("Distance in cm: %0.1f", distance)
        
