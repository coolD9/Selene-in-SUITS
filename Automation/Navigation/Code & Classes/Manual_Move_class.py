# NECCESARY PACKAGES

import struct # used to create UDP Packet that contains commands

import time # used to get timestamp and pause key board input reciever

import keyboard # type: ignore | used to read keystrokes

import socket  # used to communicate with UDP socket

"""
CLASS: Manual_Move

ATTRIBUTES: 
    float throttle:     stores % of throttle the Rover currently has 
    float steering:     stores the degree of turn the Rover currently has 
    int braking:        stores if the brake is engaged or not (1 or 0)
    string IP_address:  stores the IP address of the TSS server 
    int Port:           stores the UDP port used by TSS server
    socket udp_socket:  socket communicator 

METHODS: 

    __init__:                   Constructor
    set_forward_throttle():     increases throttle of Rover
    set_backward_throttle():    decreases throttle of Rover
    right_turn():               increases steering to allow for right turn
    left_turn():                decrease steering to allow for left turn
    toggle_brakes               turns brake on and off
    send_command                sends UDP packet to the TSS with movement commands
    Move_Rover                  updates the attributes based on keyboard stroke
    __del__                     Destructor

PACKAGES:
    import struct       creates UDP packet
    import time         to create time stamps and pause input reciever
    import keyboard     used to accept keystrokes
    import socket       used to communicate with UDP socket
    
DESCRIPTION:

    Manual_Move class is used to manually controll the movement of DUST simulation of 
    NASA Pressurized Rover by allowing the use of wsadb key strokes to control Acceleration,
    Deceleration/Reverse, left turn, right turn and braking respectively 
    
"""
class Manual_Move:
    throttle = 0.0       # current throttle
    steering = 0.0       # current steering
    braking = 0          # current brake status
    IP_address = " "     # TSS IP Address
    Port = 14141         # TSS UDP Port
    
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
        # asking user of TSS IP address
        self.IP_address = input("Please enter IP address: ")

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
        if self.braking == 0:
            self.braking == 1
        # switch to off if on 
        elif self.braking == 1:
            self.braking == 0

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
    
    # Joystick Movement 
               
    """
    Name: __init__ (DECONSTRUCTOR)
    
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
Move.Move_Rover()


    
    
        