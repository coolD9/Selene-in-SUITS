# 

import struct # used to create UDP Packet that contains commands

import time # used to get timestamp and pause key board input reciever

import keyboard # type: ignore | used to read keystrokes

import socket  # used to communicate with UDP socket


"""
    Name: send_command
    
    INPUT: 
        command:        TSS command number
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This function will create a packet that will be sent to the TSS server
        in the given format (Timestamp|Command)
"""
def send_command(command):
        # get timestamp
        timestamp = int(time.time())
        
        # creating packet that will be sent
        data = struct.pack(">II", timestamp, command)
        try: 
            # sending UDP packet
            udp_socket.sendto(data, (IP_address, Port))
             
        # error checking, ending program if error occurs in sending
        except socket.error as err:
            print(f"Command was unsuccesfully sent: {err}")
            print("Exiting program")
            # closing UDP socket
            udp_socket.close()
            exit()
        
        response = receive_command(command)

        return response

       
"""
    Name: receive_command
    
    INPUT: 
        command:        TSS command number
    
    RETURN: s
        N/A
    
    DESCRIPTION:
        This function will receive a packet from the TSS and unpack it, returning
        the unpacked data. For everything but lidar: (timestamp | command number | value) 
        For lidar: (timestamp | command number | 13 float values)
    """
def receive_command(command):
      # get commands
        if command < 167 and command > 1:
          
          # recvfrom returns a tuple with the data and the address 
          # of the sender. Could use recv() if we dont need the address
           data, address = udp_socket.recvfrom(12)
          
           # unpacking the data. Assigning three variables since the
           # data is sent to us as a tuple of 3 items. The actual data
           # from the json files is the 3rd item so that is what is going
           # to be returned here.
           # if assigning the whole unpacked data to just one variable,
           # when printed, it would look like (120, 119, 2.9994838)
           # (random numbers for the example) meaning 
           # (timestamp, command number, valuefromfile).
           # by assigning all 3 we get rid of the tuple. 
           # unpacking twice, one for ints one for floats. If there's a
           # better way then please communicate about it. 
           int_Timestamp, int_commandN, int_info = struct.unpack('>III', data)
           float_Timestamp, float_commandN, float_info = struct.unpack('>IIf', data)

           
           # all the commands that return a float. Can have more if 
           # statements so its not a big line.
           if(command >= 17 and command <= 47) or (command >= 58 and command <= 118) or (command >= 126 and command <= 139) or (command >= 141 and command <= 159) or (command >= 161 and command <= 163):
               return float_info
           # everything else is an int or a bool so just return an int. (bool will be 0 or 1)
           else:
                 return int_info

        # get lidar command
        elif command == 167:
                # recvfrom returns a tuple with the data and the address 
                # of the sender. Could use recv() if we dont need the address
                # size of 60 in this case since we receive 13 floats,
                # command number and timestamp.
               dataR, address = udp_socket.recvfrom(60)

          # unpacking the data on a tuple this time. We receive a tuple of
          # 15 values in this case. 
               info = struct.unpack('>II13f', dataR)
        
          # timestamp is the first element of the tuple,
          # command number is the second, then the remaining
          # values are the lidar values.
               r_timestamp = info[0]
               command_num = info[1]
               list_of_lidar = info[2:]
        
          # just returning lidar values for example sake. If we were to need 
          # timestamp and command number then the example above is how to get them.
          # we could return the whole tuple and then get each value outside the 
          # function for whatever purposes.
               return list_of_lidar

        # no command  
        else:
               return "command not found."

"""
    Name: get_commands
    
    INPUT: 
       N/A
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This function will begin reading keystrokes and performing neccesary function
        based on key stroke entered
"""
def get_commands():
     # using keys just for example purposes, doesnt mean this is how we will 
     # implement it. Feel free to change the values for testing.
        while True:
           # reading real time keystrokes
           key = keyboard.read_event().name
           if key == 'h':
                print("getting rover ac_heating status...")
                time.sleep(0.1)
                print(send_command(119))

           elif key == 'c':
                print("getting rover ac_cooling status...")
                time.sleep(0.1)
                print(send_command(120))
            
           elif key == 'r':
                print("getting rover co2_scrubber status...")
                time.sleep(0.1)
                print(send_command(121))

           elif key == 'l':
                print("getting rover lights status...")
                time.sleep(0.1)
                print(send_command(122))
            
           elif key == 't':
                print("getting oxygen levels...")
                time.sleep(0.1)
                print(send_command(151))

           elif key == 'p':
                print("getting oxygen pressure levels...")
                time.sleep(0.1)
                print(send_command(138))
                    
           elif key == 'i':
                print("getting lidar...")
                time.sleep(0.1)
                print(send_command(167))

            #end program and close packet 
           elif key == "q":
               print("Exiting program")
               udp_socket.close()
               exit()
        

IP_address = " "     # TSS IP Address
Port = 14141         # TSS UDP Port
IP_address = input("Please enter IP address: ")

# initilizing UDP socket communication
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
get_commands()