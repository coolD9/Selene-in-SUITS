# NECCESARY PACKAGES

import struct # used to create UDP Packet that contains commands

import time # used to get timestamp and pause key board input reciever

import keyboard # type: ignore | used to read keystrokes

import socket  # used to communicate with UDP socket

import pygame   # used to read inputs from the Joystick 

"""
CLASS: Manual_Move

ATTRIBUTES: 
    float throttle:     stores % of throttle the Rover currently has 
    float steering:     stores the degree of turn the Rover currently has 
    int braking:        stores if the brake is engaged or not (1 or 0)
    string IP_address:  stores the IP address of the TSS server 
    int Port:           stores the UDP port used by TSS server
    roverStick:         stores the joystick object 
    toggle_control      stores the flag to indicate whether using keyboard controls or joystick control
    socket udp_socket:  socket communicator 

METHODS: 

    __init__:                   Constructor
    set_forward_throttle():     increases throttle of Rover when using keyboard controls
    set_backward_throttle():    decreases throttle of Rover when using keyboard controls
    right_turn():               increases steering to allow for right turn whne using keyboard controls
    left_turn():                decrease steering to allow for left turn when using keyoard controls
    toggle_brakes               turns brake on and off
    send_command                sends UDP packet to the TSS with movement commands
    Move_Rover                  updates the attributes based on keyboard stroke
    verticalJoystickmove()      controlling vertical movement when using joystick controls (y axis control)
    horizontalJoystickmove()    control horizontal movement when using joystick controls (x axis control)
    moveRoverjoystick()         controls the PR rover based on joystick input 
    Modes()                     Toggles between keyboard movement and joystick movement 
    __del__                     Destructor

PACKAGES:
    import struct       creates UDP packet
    import time         to create time stamps and pause input reciever
    import keyboard     used to accept keystrokes
    import socket       used to communicate with UDP socket
    import pygame       used to read input from joystick
    
DESCRIPTION:

    Manual_Move class is used to manually controll the movement of DUST simulation of 
    NASA Pressurized Rover by allowing the user to control the rover by using the keyboard 
    or a joystick. The Joystick controls allows the user to push the stick foward, pull back, 
    move left or right, to accelerate, decelarate and turn rover respectively and allows the
    user to press button 2 to brake, button 7 to switch controll modes and 8 to quit exit the program.
    For the keyboard controlls the user will use wasd to accelerate, turn left, decelerate and right turn 
    respectivley then press b for brake, t for switching modes and q for quiting the entire program
    
"""
class Manual_Move:
    throttle = 0.0       # current throttle
    steering = 0.0       # current steering
    braking = 0          # current brake status
    IP_address = " "     # TSS IP Address
    Port = 14141         # TSS UDP Port
    roverStick = 0.0     # storing the joystick object
    toggle_controls = False # flag to check control moce
    
    # initilizing UDP socket communication
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    """
    Name: __init__ (CONSTRUCTOR)
    
    INPUT: 
        N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        Constructor that is used to obtain the TSS Ip Address needed for 
        Communication to TSS
    """
    def __init__(self):
        # setting flag to default start in Joystick mode
        self.toggle_controls = False
         # asking user of TSS IP address
        self.IP_address = input("Please enter IP address: ")
        
        #initializing the joystick object
        pygame.init()
        pygame.joystick.init()
        count = pygame.joystick.get_count()
        
        #checking of joystick is connected
        if count == 0:
            print("Joystick not connected")
             # if joystick is not connected set the default mode to keyboard mode
            self.toggle_controls = True
            pygame.quit()
        else:
            self.roverStick = pygame.joystick.Joystick(0)
        

    """
    Name: Set_forward_throttle
    
    INPUT: 
        N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This method will increase the throttle by 10% and also check
        to ensure that throttle does not surpass maximum potential throttle
    """
    def set_forward_throttle(self):
        
        # check to ensure throotle does overflow
        if self.throttle + 10 > 100.0:  
            #if yes sets to maximum  
            self.throttle = 100.0
        else:
            # if no overflow then simply increment 
            self.throttle = self.throttle + 10
            
    """
    Name: Set_backward_throttle
    
    INPUT: 
        N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This method will decrease the throttle by 10% and also check
        to ensure that throttle does not surpass minimum potential throttle
    """
    def set_backward_throttle(self):
        # check to ensure throotle does underflow
        if self.throttle - 10 < -100.0:
            #if yes sets to minimum
            self.throttle = -100.0
        else:
            # if no underflow then simply decrement 
            self.throttle = self.throttle - 10
            
    """
    Name: right_turn
    
    INPUT: 
        N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This method will increase the steering that will cause a right
        turn and also ensures steering does not surpass maximum turn value
    """
    def right_turn(self):
        # check if steering is overflowing 
        if self.steering + 0.10 > 1.0:
            # if yes then just set to maximum
            self.steering = 1.0
        else: 
            #if not then just increment 
            self.steering = self.steering + 0.10

    """
    Name: left_turn
    
    INPUT: 
        N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This method will decrease the steering that will cause a left
        turn and also ensures steering does not surpass minimum turn value
    """
    def left_turn(self):
        # check if steering is underflowing 
        if self.steering - 0.10 < -1.0:
             # if yes then just set to minimum
            self.steering = -1.0
        else:
            #if not then just decrement 
            self.steering = self.steering - 0.10

    """
    Name: toggle_breakes
    
    INPUT: 
        N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        Will turn toggle the breaks between on an off
    """
    def toggle_brakes(self):
        # switch to on if off
        if self.braking == 0.0:
            self.braking == 1.0
        # switch to off if on 
        elif self.braking == 1.0:
            self.braking == 0.0

    """
    Name: send_command
    
    INPUT: 
        command:        TSS command number
        value:          input data to be sent to TSS 
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This method will create a packet that will be sent to the TSS server
        in the given format (Timestamp|Command|Input)
    """
    def send_command(self,command,value):
        # get timestamp
        timestamp = int(time.time())
        
        # creating packet that will be sent
        data = struct.pack(">IIf", timestamp, command, value)
        try: 
            # sending UDP packet
            self.udp_socket.sendto(data, (self.IP_address, self.Port))
            
        # error checking, ending program if error occurs in sending
        except socket.error as err:
            print(f"Command was unsuccesfully sent: {err}")
            print("Exiting program")
            # closing UDP socket
            self.udp_socket.close()
            exit()
    
    """
    Name: send_command
    
    INPUT: 
       N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This Method will begin reading keystrokes and performing neccesary function
        based on key stroke entered
    """
    def Move_Rover(self):
        while True:
            # reading real time keystrokes
           key = keyboard.read_event().name
           
           # accelerating the rover
           if key == "w":
               self.set_forward_throttle()
               self.send_command(1109,self.throttle)
               print("Accelerating...")
               # pausing input reading to make sure you get one at a time
               time.sleep(0.1)
            
            # decelerating the rover
           elif key == "s":
               self.set_backward_throttle()
               self.send_command(1109,self.throttle)
               print("Decelerating...")
               time.sleep(0.1)
               
            # turn the rover left 
           elif key == "a":
               self.left_turn()
               self.send_command(1110,self.steering)
               print("Turning Left...")
               time.sleep(0.1)
            
            # turn the rover right
           elif key == "d":
               self.right_turn()
               self.send_command(1110,self.steering)
               print("Turing Right...")
               time.sleep(0.1)
               
            # toggle brake on and off
           elif key == "b":
               self.toggle_brakes()
               self.send_command(1107,self.braking)
               print("Toggling Brake")
               time.sleep(0.1)
            #end program and close packet 
           elif key == "q":
               print("Exiting program")
               self.udp_socket.close()
               exit()
            # switching to joystick mode
           elif key == "t":
               print("Switching modes")
               self.toggle_controls = False
               break
    
    # JOYSTICK MOVEMENT  
    """
    Name: verticalJoystickmove
    
    INPUT: 
       axis:   value from the y axis of 
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This method will accept the y axis values from the Joystick then
        update the throttle function which will allow the rover to accelerate 
        and decelarate (move forward and move backward)
    """
    def verticalJoystickmove(self, axis):
        # the throttle from the last check
        prevThrottlepercent = 0
        
        # converting the axis movement to percentage
        throttlePercent = axis * 100
        
        #flipping the sign so + means forward and - means backward
        throttlePercent *= -1
        
        # if the current axis percent is positive moving forward
        if throttlePercent > 0:
            #if the throttle is decreasing decelerating else accelerating 
            if throttlePercent < prevThrottlepercent:
                print("Decelerating...")
            else: 
                print("Accelerating...")
        else:
            if throttlePercent > prevThrottlepercent:
                print("Decelerating...")
            else: 
                print("Accelerating...")
                
        # updating previous throttle percent
        prevThrottlepercent = throttlePercent
        # finding the difference between the current throttle and the new throttle
        diff = throttlePercent - self.throttle
        # updating the stored throrrle 
        self.throttle += diff
        
        # if the throttle is negative the rover is reversing else it is moving forward (advancing)
        if self.throttle < 0:
            print("Reversing...")
        else:
            print("Advancing...")
        
        # sending the new throttle to the TSS to start movement 
        self.send_command(1109,self.throttle)
    """
    Name: horizontalJoystickmove
    
    INPUT: 
       axis:   value from the x axis of 
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This method will accept the x axis values from the Joystick then
        update the throttle function which will allow the rover to move 
        left and right
    """
    def horizontalJoystickmove(self,axis):
        # if checking the difference between current steering and the x axis of the controller
        diff = axis - self.steering
        
        # updating the steering based on the distance
        self.steering += diff
        
        # if the steering is negative that is a left turn and positive turn is a right tuen 
        if self.steering < 0:
            print("Turning Left....")
        else:
            print("Turning Right....")
        
        # sending updated steering to the TSS and the Rover
        self.send_command(1110,self.steering)
    """
    Name: moveRoverjoystick
    
    INPUT: 
        N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This method will read the input from the Joystick and based on the input recieve
        perform different functions. 
    """   
    def moveRoverjoystick(self):
        moving = True
        while moving:
            # getting the input from Joystick
            for event in pygame.event.get():
                # base case for checking if recieveing input from Joystick
                if event.type == pygame.QUIT:
                    break
                # checking for axis motion of the stick on the joystick
                elif event.type == pygame.JOYAXISMOTION:
                    # moving the rover vertically 
                    self.verticalJoystickmove(self.roverStick.get_axis(1))
                    # moving the rover horizonatally 
                    self.horizontalJoystickmove(self.roverStick.get_axis(0))
                
                # checking for buttons on the joystick being pushed
                elif event.type == pygame.JOYBUTTONDOWN:
                    
                    #press button 2 to toggle brakes
                    if self.roverStick.get_button(1):
                        self.toggle_brakes()
                        self.send_command(1107,self.braking)
                        print("Braking...")
                    
                    # press button 7 to toggle between modes
                    elif self.roverStick.get_button(6):
                        moving = False
                        self.toggle_controls = True
                        
                    # press button 8 to exit the program 
                    elif self.roverStick.get_button(7):
                        self.udp_socket.close()
                        pygame.quit()
                        print("Exiting Program")
                        exit()
                    
    """
    Name: Modes
    
    INPUT: 
        N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This method will allow the user to switch between the keyboard movement and 
        joystick Movement
    """  
    def Modes(self):
        while True:
            # if the flag is true allow for keyboard movement 
            if self.toggle_controls == True: 
                self.Move_Rover()
            # if false allow for the joystick movement 
            else:
                self.moveRoverjoystick()
                
                
                    
               
    """
    Name: __del__ (DECONSTRUCTOR)
    
    INPUT: 
        N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        Deconstructor that closes the UDP socket
    """
    def __del__(self):
        self.udp_socket.close()
        
        
        
          
## MAIN Driver::

# initalize the Manual Move Class using constructor
Move = Manual_Move()

# begin moving the rover
Move.Modes()


    
    
        