import RPi.GPIO as GPIO
import time

mpin=18
tpin=27
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, False)#LED output pin
GPIO.setup(17, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(22, GPIO.IN)         #Read output from PIR motion sensor
cap=0.000001
adj=2.130620985
i=0
t=0

while True:
    GPIO.setup(mpin, GPIO.OUT)
    GPIO.setup(tpin, GPIO.OUT)
    GPIO.output(mpin, False)
    GPIO.output(tpin, False)
    time.sleep(0.05)
    GPIO.setup(mpin, GPIO.IN)
    time.sleep(0.05)
    GPIO.output(tpin, True)
    starttime=time.time()
    endtime=time.time()
    while (GPIO.input(mpin) == GPIO.LOW):
        endtime=time.time()
    measureresistance=endtime-starttime
    
    res=(measureresistance/cap)*adj
    i=i+1
    t=t+res
    darkness = 600    # this value determines at what 'darkness level' the surrounding environment
                      # will allow the light to turn on
    
    if i==10:
        t=t/i
        if t>=darkness:            #Threshold that turns the whole system on.
                                   #Value is initialized on the top of the code for easy adjustment
            
            p=GPIO.input(17)       #Reads input from first sensor
            q=GPIO.input(22)       #Reads input from second sensor
            if p==0 and q==0:      #When output from both motion sensor is LOW
                print( "No one detected")
                GPIO.output(2, 0)  #Turn OFF LED
                time.sleep(0.25)   #Short pause before redetection
            elif p==1:             #When output from first sensor is HIGH
                print ("Intruder detected")
                print("Resistance is",t, "(LED ON)")
                GPIO.output(2, 1)  #Turn ON LED
                time.sleep(5)      #Light remains on for longer
            elif q==1:               #When output from second sensor is HIGH
                print ("Intruder detected (2)")
                print("Resistance is",t, "(LED ON)")
                GPIO.output(2, 1)  #Turn ON LED
                time.sleep(5)
        else:                      #if it is still bright out, the lights remains off 
            print ("Resistance is",t, "(LED OFF)")
            GPIO.output(2, 0)      #Turn OFF LED
            time.sleep(1)
        i=0
        t=0