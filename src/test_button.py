import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
# GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
while True: # Run forever
    if GPIO.input(5) == True:
        print("Button 5 was pushed!")       
    if GPIO.input(6) == True:
        print("Button 6 was pushed!")       
    if GPIO.input(7) == True:
        print("Button 7 was pushed!")       
    if GPIO.input(8) == True:
        print("Button 8 was pushed!")        
    if GPIO.input(9) == True:
        print("Button 9 was pushed!")                
    # if GPIO.input(10) == False:
        # print("Button 10 was pushed!")                
    if GPIO.input(11) == True:
        print("Button 11 was pushed!")           
    if GPIO.input(12) == True:
        print("Button 12 was pushed!")        
    if GPIO.input(13) == True:
        print("Button 13 was pushed!")        
    if GPIO.input(14) == True:
        print("Button 14 was pushed!")        
    if GPIO.input(15) == True:
        print("Button 15 was pushed!")        
    if GPIO.input(16) == True:
        print("Button 16 was pushed!")        
    if GPIO.input(17) == True:
        print("Button 17 was pushed!")        
    if GPIO.input(18) == True:
        print("Button 18 was pushed!")        
    if GPIO.input(19) == True:
        print("Button 19 was pushed!")        
    if GPIO.input(20) == True:
        print("Button 20 was pushed!")        
    if GPIO.input(21) == True:
        print("Button 21 was pushed!")        
    if GPIO.input(22) == True:
        print("Button 22 was pushed!")        
    if GPIO.input(23) == True:
        print("Button 23 was pushed!")        
    if GPIO.input(24) == True:
        print("Button 24 was pushed!")        
    if GPIO.input(25) == True:
        print("Button 25 was pushed!")        
    if GPIO.input(26) == True:
        print("Button 26 was pushed!")        
    