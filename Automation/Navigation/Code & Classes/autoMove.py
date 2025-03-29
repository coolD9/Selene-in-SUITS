# WORK IN PROGRESS.

import struct # used to create UDP Packet that contains commands

import time # used to get timestamp and pauses

import socket  # used to communicate with UDP socket

"""
CLASS: AutoMove
    AutoMove class is used to allow the movement of the DUST simulation
    NASA Pressurized Rover to be done autonomously. By having methods 
    that increase and decrease throttle, steering and toggle brakes to 
    move forward, backwards, turn or stop.
    
"""
class AutoMove:
# Command number	Command	Data input
# 1107	          Brakes	float: 0 or 1
# 1109	          Throttle	float: -100, 100
# 1110	          Steering	float: -1.0, 1.0

     """
    Name: __init__ (CONSTRUCTOR)
    
    INPUT: 
        N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        Constructor that initializes the class attributes. 
    """
     def __init__(self):
          # These values are subject to change.
          # All of these can be found on the tss files, cardinal directions are
          # found as "heading" and go from 0 to 180 and 0 to -180.
          self.throttle = 0.0
          self.brakes = 0
          self.steering = 0.0
          self.optimalSpeed = 3.6
          self.minT = 30
          self.maxT = 100
          self.TIR = 3
          self.SIR = 0.4
          self.speed = 0.0
          self.north = (-22.5, 22.4)
          self.south = (157.5, -157.6)
          self.east = (67.5, 112.4)
          self.west = (-112.5, -67.6)
          self.northeast = (22.5, 67.4)
          self.northwest = (-67.5, -22.6)
          self.southeast = (112.5, 157.4)
          self.southwest = (-157.5, -112.6)
          
     """
    Name: send_command
    
    INPUT: 
        command:        TSS command number
        value:          input data to be sent to TSS 
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This method will create a packet that will be sent to the TSS server
        in the given format (Timestamp|Command|Input) for movement, and 
        (Timestamp|Command) for everything else.
    """
     def sendCommand(self, command,value):
          # checking if the commands are movement commands, get speed or get heading
          # other commands are not needed for this.
          if (command == 135 or command == 1109 or command == 1107 
          or command == 1110 or command == 131):
               # get timestamp
               timestamp = int(time.time())
          
               # creating packet that will be sent 
               # rover movement commands are sent in a 12 byte packet
               # while the rest in a 8 byte. 
               if command == 135 or command == 131:
                    data = struct.pack(">II", timestamp, command)
               else:
                    data = struct.pack(">IIf", timestamp, command, value)
          
               try: 
                    # sending UDP packet
                    udpSocket.sendto(data, (ipAdress, Port))
               
               # error checking, ending program if error occurs in sending
               except socket.error as err:
                    print(f"Command was unsuccesfully sent: {err}")
                    print("Exiting program")
                    # closing UDP socket
                    udpSocket.close()
                    exit()
          else:
               print("command not found or not needed")

     """
    Name: send_command
    
    INPUT: 
        command:        TSS command number
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This method will create a packet that will be sent to the TSS server
        in the given format (Timestamp|Command|Input) for movement, and 
        (Timestamp|Command) for everything else.
    """
     def receiveCommand(self, command):
          # call sendCommand to ask for data or move the rover.
          self.sendCommand(command, 0)

          # receiving speed or heading
          if command == 135 or command == 131:
               try:
                    data = udpSocket.recv(12)

                    # using indexing to just assign the third element of the
                    # tuple since that is what we need. timestamp and command
                    # number are not needed for now, but if we were to need 
                    # them we would just create 2 other variables.
                    rData = struct.unpack('>IIf', data)[2]
                    return rData
               
               # checking for errors
               except socket.error as err1:
                    print(f"data was not received: {err2}")

               except struct.error as err2:
                    print(f"Error when unpacking data: {err2}")

          # no command  
          else:
               print("command not found or not needed")
               return None

     """
    Name: increaseThrottle
    
    INPUT: 
        N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This method will increase the throttle by TIR and also check
        to ensure that throttle does not surpass maximum potential throttle
     """
     def increaseThrottle(self):
        
        # check to ensure throotle does overflow
        if self.throttle + self.TIR > 100.0:  
            #if yes sets to maximum  
            self.throttle = 100.0
        else:
            # if no overflow then simply increment 
            self.throttle = self.throttle + self.TIR

     """
    Name: decreaseThrottle
    
    INPUT: 
        N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This method will decrease the throttle by TIR and also check
        to ensure that throttle does not surpass minimum potential throttle
    """
     def decreaseThrottle(self):
        # check to ensure throotle does underflow
        if self.throttle - self.TIR < -100.0:
            #if yes sets to minimum
            self.throttle = -100.0
        else:
            # if no underflow then simply decrement 
            self.throttle = self.throttle - self.TIR


     """
    Name: maintainSpeed
    
    INPUT: 
       N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This Method will ensure that the rover is moving at the desired speed.
    """
     def maintainSpeed(self):
          # if the speed is positive, that means the rover is moving
          # forward. If it's less than the desired speed, increase the throttle
          self.speed = self.receiveCommand(135)

          if self.speed >= 0 and self.speed < 3.4:
               self.increaseThrottle()
          
          # if the speed is negative, rover moving backwards. decrease the throttle
          # if the speed is negative but greater than the desired speed.
          elif self.speed <= 0 and self.speed > -3.4:
               self.decreaseThrottle()
          self.sendCommand(1109, self.throttle)

     """
    Name: steerRight
    
    INPUT: 
       N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This Method will increase the steering to turn right.
     """
     def steerRight(self):
          # adjust the steering to be that of the SIR
          while self.SIR > self.steering:
               self.steering += self.SIR  
               self.sendCommand(1110, self.steering)

     """
    Name: steerHalfRight
    
    INPUT: 
       N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This Method will increase the steering to turn diagonally 
        to the right.
     """
     def steerHalfRight(self):
          # adjust the steering to be that of the SIR /2 (diagonal SIR) 
          while self.SIR > self.steering:
               self.steering += (self.SIR / 2)
               self.sendCommand(1110, self.steering)

     """
    Name: stopRight
    
    INPUT: 
       N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This Method will decrease the steering to stop turning right
     """
     def stopRight(self, turning):
          # adjust the steering so that it's equal to 0 decreasing it
          # by SIR
          if self.steering != 0:
               self.steering -= self.SIR
               self.sendCommand(1110,self.steering)
          else:
          # make turning = false to stop the loop in the right function
               turning = False

     """
    Name: stopHalfRight
    
    INPUT: 
       N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This Method will decrease the steering to stop turning 
        diagonally right
     """
     def stopHalfRight(self, turning):
          # adjust the steering so that it's equal to 0. 
          # decreasing it by SIR /2 (diagonal SIR)
          if self.steering != 0:
               self.steering -= (self.SIR / 2)
               self.sendCommand(1110,self.steering)
          else:
               turning = False

     """
    Name: steerLeft
    
    INPUT: 
       N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This Method will decrease the steering to turn left.
        (negative steering means turning left)
     """
     def steerLeft(self):
           # adjust the steering to be that of negative SIR
           # negative steering means turning left
          while -self.SIR < self.steering:
               self.steering -= self.SIR
               self.sendCommand(1110, self.steering)

     """
    Name: steerHalfLeft
    
    INPUT: 
       N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This Method will decrease the steering to turn diagonally
        to the left.
     """
     def steerHalfLeft(self):
           # adjust the steering to be that of negative SIR /2
          while -self.SIR < self.steering:
               self.steering -= (self.SIR / 2)
               self.sendCommand(1110, self.steering)

     """
    Name: stopLeft
    
    INPUT: 
       N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This Method will increase the steering to 
        stop turning left.
     """
     def stopLeft(self, turning):
          # adjust the steering so that it's equal to 0 increasing it
          # by SIR
          if self.steering != 0:
               self.steering += self.SIR
               self.sendCommand(1110,self.steering)
          else:
               turning = False

     """
    Name: stopHalfLeft
    
    INPUT: 
       N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This Method will increase the steering to stop
        turning diagonally to the left
     """
     def stopHalfLeft(self, turning):
          # adjust the steering so that it's equal to 0. 
          # increasing it by SIR /2 (diagonal SIR)
          if self.steering != 0:
               self.steering += (self.SIR / 2)
               self.sendCommand(1110,self.steering)
          else:
               turning = False

     """
    Name: stop
    
    INPUT: 
       N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This Method will decrease or increase throttle depending on
        if the rover is going forward or backwards. Then toggles the 
        breaks to stop.
     """
     def stop(self):
          self.speed = self.receiveCommand(135)
          # check if the speed is positive or negative.
          # decrease or increase speed to get it to be 
          while self.speed < -1 or self.speed > 1:
               if self.speed < 0:
                    self.increaseThrottle()
                    self.sendCommand(1109, self.throttle)
               else:
                    self.decreaseThrottle()
                    self.sendCommand(1109, self.throttle)
               self.speed = self.receiveCommand(135)
          
          # toggle brakes
          self.brakes = 1
          self.sendCommand(1107, self.brakes)


          # decrease or increase the throttle to 0
          while self.throttle != 0:
               if self.throttle < 0:
                    self.increaseThrottle()
               else:
                    self.decreaseThrottle()

     """
    Name: forward
    
    INPUT: 
       N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This Method will move the rover forward and ensure it is moving
        at the desired speed.
     """
     def forward(self):
          # increase the throttle to min_T (minimum throttle to move)
          # if it's not already
          while self.throttle < 30:
               self.increaseThrottle()
               self.sendCommand(1109, self.throttle)
          
          # maintain optimal speed
          while self.speed < 3.4 or self.speed > 3.8:
               if self.speed < 3.4:
                    self.increaseThrottle()
                    self.sendCommand(1109, self.throttle)
               else:
                    self.decreaseThrottle()
                    self.sendCommand(1109, self.throttle)

     """
    Name: forward
    
    INPUT: 
       N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This Method will move the rover backwards and ensure it is moving
        at the desired speed.
     """
     def backward(self):
          # increase the throttle to -min_T (minimum throttle to move)
          # if it's not already. Negative since moving backwards is negative
          while self.throttle > -30:
               self.decreaseThrottle()
               self.sendCommand(1109, self.throttle)
          
          # maintaining negative optimal speed
          while self.speed > -3.4 or self.speed < -3.8:
               if self.speed > -3.4:
                    self.decreaseThrottle()
                    self.sendCommand(1109, self.throttle)
               else:
                    self.increaseThrottle()
                    self.sendCommand(1109, self.throttle)

     """
    Name: right
    
    INPUT: 
       N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This is the main turn right method that will enable the rover to turn
        in that direction. Checks for heading to know where to head next.

     """
     def right(self):
          turning = True
          facing = self.receiveCommand(131)

          # if facing between north and northeast, turn to east 
          # (right of north)
          if facing > self.north[0] and facing < self.northeast[1]:
               self.steerRight()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.east[0] and facing < self.east[1]):
                         self.stopRight(turning)
          
           # if facing between east and southeast, turn to south
           # (right of east)
          elif facing > self.east[0] and facing < self.southeast[1]:
               self.steerRight()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing < self.south[0] or facing > self.south[1]):
                         self.stopRight(turning)

          # if facing between south and southwest, turn to west
          # (right of south)
          elif facing > self.south[1] or facing < self.southwest[0]:
               self.steerRight()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131) 
                    if(facing < self.west[0] and facing > self.west[1]):
                         self.stopRight(turning)
          
          # if facing between west and northwest, turn to north
          # (right of west)
          elif facing > self.west[1] and facing < self.northwest[0]:
               self.steerRight()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.north[0] and facing < self.north[1]):
                         self.stopRight(turning)

     """
    Name: diagonal Right
    
    INPUT: 
       N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This is the main turn diagonal right method that will enable the rover to turn
        in that direction. Checks for heading to know where to head next.
     """
     def diagonalRight(self):
          turning = True
          facing = self.receiveCommand(131)

          # if facing north turn northeast
          if facing > self.north[0] and facing < self.north[1]:
               self.steerHalfRight()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.northeast[0] and facing < self.northeast[1]):
                         self.stopHalfRight(turning)
          
          # if facing northeast turn east
          elif facing > self.northeast[0] and facing < self.northeast[1]:
               self.steerHalfRight()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.east[0] or facing < self.east[1]):
                         self.stopHalfRight(turning)

          # if facing east turn southeast
          elif facing > self.east[0] or facing < self.east[1]:
               self.steerHalfRight()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.southeast[0] and facing < self.southeast[1]):
                         self.stopHalfRight(turning)
          
          # if facing southeast turn south
          elif facing > self.southeast[0] and facing < self.southeast[1]:
               self.steerHalfRight()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing < self.south[0] or facing > self.south[1]):
                         self.stopHalfRight(turning)

          # if facing south turn southwest
          elif facing < self.south[0] or facing > self.south[1]:
               self.steerHalfRight()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.southwest[0] and facing < self.southwest[1]):
                         self.stopHalfRight(turning)
          
          # if facing southwest turn west
          elif facing > self.southwest[0] and facing < self.southwest[1]:
               self.steerHalfRight()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.west[0] or facing < self.west[1]):
                         self.stopHalfRight(turning)

          # if facing west turn northwest
          elif facing > self.west[0] or facing < self.west[1]:
               self.steerHalfRight()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.northwest[0] and facing < self.northwest[1]):
                         self.stopHalfRight(turning)
          
          # if facing northwest turn north
          elif facing > self.northwest[0] and facing < self.northwest[1]:
               self.steerHalfRight()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.north[0] and facing < self.north[1]):
                         self.stopHalfRight(turning)

     
     """
    Name: left
    
    INPUT: 
       N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This is the main turn left method that will enable the rover to turn
        in that direction. Checks for heading to know where to head next.
     """
     def left(self):
          turning = True
          facing = self.receiveCommand(131)

          # if facing between north and northwest, turn to west
          # (left of north)
          if facing < self.north[1] and facing > self.northwest[0]:
               self.steerLeft()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.west[0] and facing < self.west[1]):
                         self.stopLeft(turning)
          
          # if facing between west and southwest, turn to south
          # (left of west)
          elif facing < self.west[0] and facing > self.southwest[0]:
               self.steerLeft()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.south[0] or facing < self.south[1]):
                         self.stopLeft(turning)

          # if facing between south and southeast, turn to east
          # (left of south)
          elif facing < self.south[1] or facing > self.southeast[0]:
               self.steerLeft()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.east[0] and facing < self.east[1]):
                         self.stopLeft(turning)
          
          # if facing between east and northeast, turn to north
          # (left of east)
          elif facing < self.east[1] and facing > self.northeast[0]:
               self.steerLeft()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.north[0] and facing < self.north[1]):
                         self.stopLeft(turning)

     """
    Name: diagonalLeft
    
    INPUT: 
       N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This is the main turn diagonal left method that will enable the rover to turn
        in that direction. Checks for heading to know where to head next.
     """
     def diagonalLeft(self):
          turning = True
          facing = self.receiveCommand(131)

          # if facing north turn northwest
          if facing > self.north[0] and facing < self.north[1]:
               self.steerHalfLeft()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.northwest[0] and facing < self.northwest[1]):
                         self.stopHalfLeft(turning)
          
          # if facing northwest turn west
          elif facing > self.northwest[0] and facing < self.northwest[1]:
               self.steerHalfLeft()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.west[0] or facing < self.west[1]):
                         self.stopHalfLeft(turning)

          # if facing west turn southwest
          elif facing > self.west[0] or facing < self.west[1]:
               self.steerHalfLeft()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.southwest[0] and facing < self.southwest[1]):
                         self.stopHalfLeft(turning)
          
          # if facing southwest turn south
          elif facing > self.southwest[0] and facing < self.southwest[1]:
               self.steerHalfLeft()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing < self.south[0] or facing > self.south[1]):
                         self.stopHalfLeft(turning)

          # if facing south turn southeast
          elif facing < self.south[0] or facing > self.south[1]:
               self.steerHalfLeft()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.southeast[0] and facing < self.southeast[1]):
                         self.stopHalfLeft(turning)
          
          # if facing southeast turn east
          elif facing > self.southeast[0] and facing < self.southeast[1]:
               self.steerHalfLeft()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.east[0] or facing < self.east[1]):
                         self.stopHalfLeft(turning)

          # if facing east turn northeast
          elif facing > self.east[0] or facing < self.east[1]:
               self.steerHalfLeft()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.northeast[0] and facing < self.northeast[1]):
                         self.stopHalfLeft(turning)
          
          # if facing northeast turn north
          elif facing > self.northeast[0] and facing < self.northeast[1]:
               self.steerHalfLeft()
               while turning:
                    self.maintainSpeed()
                    facing = self.receiveCommand(131)
                    if(facing > self.north[0] and facing < self.north[1]):
                         self.stopHalfLeft(turning)

     def __del__(self):
          print("deleting instance of class")



ipAdress = " "     # TSS IP Address
Port = 14141         # TSS UDP Port
ipAdress = input("Please enter IP address: ")

# initilizing UDP socket communication
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

moving = AutoMove()

#moving.forward()
#time.sleep(.2)
moving.diagonalRight()
moving.right()
moving.left()