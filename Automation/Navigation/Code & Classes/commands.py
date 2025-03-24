# 

import struct # used to create UDP Packet that contains commands

import time # used to get timestamp and pause key board input reciever

import socket  # used to communicate with UDP socket

import json # used for saving data as json file.

import os # used for saving the json file locally.


class Command:
    def __init__(self):
          
        self.scriptDir = os.path.dirname(os.path.abspath(__file__))  # Get the script’s directory
        self.targetDir = os.path.abspath(os.path.join(self.scriptDir, "../../../"))  # Move up two levels
        self.IP_address = " "     # TSS IP Address
        self.Port = 14141         # TSS UDP Port

        # initilizing UDP socket communication
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.telemetry_data = {
            "pr_telemetry": {
                "ac_heating": False,
                "ac_cooling": False,
                "co2_scrubber": False,
                "lights_on": False,
                "internal_lights_on": False,
                "brakes": False,
                "in_sunlight": False,
                "throttle": 0,
                "steering": 0,
                "current_pos_x": 0,
                "current_pos_y": 0,
                "current_pos_alt": 0,
                "heading": 0,
                "pitch": 0,
                "roll": 0,
                "distance_traveled": 0,
                "speed": 0,
                "surface_incline": 0,
                "oxygen_tank": 100,
                "oxygen_pressure": 0,
                "oxygen_levels": 0,
                "fan_pri": True,
                "ac_fan_pri": 0,
                "ac_fan_sec": 0,
                "cabin_pressure": 4,
                "cabin_temperature": 22,
                "battery_level": 100,
                "power_consumption_rate": 0,
                "solar_panel_efficiency": 0,
                "external_temp": 0,
                "pr_coolant_level": 44.5,
                "pr_coolant_pressure": 500,
                "pr_coolant_tank": 100,
                "radiator": 0,
                "motor_power_consumption": 0,
                "terrain_condition": 0,
                "solar_panel_dust_accum": 0,
                "mission_elapsed_time": 0,
                "mission_planned_time": 0,
                "point_of_no_return": 0,
                "distance_from_base": 0,
                "switch_dest": False,
                "dest_x": 0,
                "dest_y": 0,
                "dest_z": 0,
                "dust_wiper": False,
                "lidar": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            }
        }

    def setIPAdress(self, ip):
         self.IP_address = ip
    """
        Name: send_command
        
        INPUT: 
            command:        TSS command number
        
        RETURN: 
            N/A
        
        DESCRIPTION:
            This method will create a packet that will be sent to the TSS server
            in the given format (Timestamp|Command)
    """
    def send_command(self,command):
            # get timestamp
            timestamp = int(time.time())
            
            # creating packet that will be sent
            data = struct.pack(">II", timestamp, command)
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
            
            response = self.receive_command(command)

            return response

        
    """
        Name: receive_command
        
        INPUT: 
            command:        TSS command number
        
        RETURN: s
            N/A
        
        DESCRIPTION:
            This method will receive a packet from the TSS and unpack it, returning
            the unpacked data. For anything but lidar: (timestamp | command number | value) 
            For lidar: (timestamp | command number | 13 float values)
        """
    def receive_command(self,command):
        # get commands
            if command < 167 and command > 1:
            # recvfrom returns a tuple with the data and the address 
            # of the sender. Could use recv() if we dont need the address
                data, address = self.udp_socket.recvfrom(12)
                int_Timestamp, int_commandN, int_info = struct.unpack('>III', data)
                float_Timestamp, float_commandN, float_info = struct.unpack('>IIf', data)

                # unpacking the data. Assigning three variables since the
                # data is sent to us as a tuple of 3 items. The actual data
                # from the json files is the 3rd item so that is what is returned here.
                # if assigning the whole unpacked data to just one variable,
                # when printed, it would look like (120, 119, 2.9994838)
                # (random numbers for the example) meaning (timestamp, command number, valuefromfile).
                # by assigning all 3 we get rid of the tuple. 
                if(command >= 17 and command <= 47) or (command >= 58 and command <= 118) or (command >= 126 and command <= 139) or (command >= 141 and command <= 159) or (command >= 161 and command <= 163):
                    return float_info
                else:
                    return int_info

            # get lidar command
            elif command == 167:
                try:
                        dataR, address = self.udp_socket.recvfrom(60)

                        # Check if we received the expected amount of data
                        if len(dataR) != 60:
                            print(f"Warning: Received {len(dataR)} bytes for LIDAR data instead of expected 60 bytes")
                            # Return default values if data is incomplete
                            return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                            
                        info = struct.unpack('>II13f', dataR)
                        r_timestamp = info[0]
                        command_num = info[1]
                        list_of_lidar = info[2:]
                        return list_of_lidar
                except struct.error as e:
                        print(f"Error unpacking LIDAR data: {e}")
                        print(f"Received {len(dataR)} bytes instead of expected 60")
                        # Return default values if unpacking fails
                        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            # no command  
            else:
                return "command not found."

    """
        Name: getData
        
        INPUT: 
        N/A
        
        RETURN: 
            N/A
        
        DESCRIPTION:
            This Method will begin reading keystrokes and performing neccesary function
            based on key stroke entered
    """
    def getData(self):
        """
        Automatically fetches all telemetry data in sequence without requiring key input,
        then saves the collected data to a JSON file.
        """
        print("Starting automated telemetry data collection...")
        
        # Collecting AC and environmental system data
        print("Getting environmental control systems data...")
        self.telemetry_data["pr_telemetry"]["ac_heating"] = self.send_command(119)
        self.telemetry_data["pr_telemetry"]["ac_cooling"] = self.send_command(120)
        self.telemetry_data["pr_telemetry"]["co2_scrubber"] = self.send_command(121)
        self.telemetry_data["pr_telemetry"]["lights_on"] = self.send_command(122)
        self.telemetry_data["pr_telemetry"]["internal_lights_on"] = self.send_command(123)
        
        # Collecting rover control systems data
        print("Getting rover control systems data...")
        self.telemetry_data["pr_telemetry"]["brakes"] = self.send_command(124)
        self.telemetry_data["pr_telemetry"]["in_sunlight"] = self.send_command(125)
        self.telemetry_data["pr_telemetry"]["throttle"] = self.send_command(126)
        self.telemetry_data["pr_telemetry"]["steering"] = self.send_command(127)
        
        # Collecting position and orientation data
        print("Getting position and orientation data...")
        self.telemetry_data["pr_telemetry"]["current_pos_x"] = self.send_command(128)
        self.telemetry_data["pr_telemetry"]["current_pos_y"] = self.send_command(129)
        self.telemetry_data["pr_telemetry"]["current_pos_alt"] = self.send_command(130)
        self.telemetry_data["pr_telemetry"]["heading"] = self.send_command(131)
        self.telemetry_data["pr_telemetry"]["pitch"] = self.send_command(132)
        self.telemetry_data["pr_telemetry"]["roll"] = self.send_command(133)
        
        # Collecting movement and terrain data
        print("Getting movement and terrain data...")
        self.telemetry_data["pr_telemetry"]["distance_traveled"] = self.send_command(134)
        self.telemetry_data["pr_telemetry"]["speed"] = self.send_command(135)
        self.telemetry_data["pr_telemetry"]["surface_incline"] = self.send_command(136)
        
        # Collecting oxygen system data
        print("Getting oxygen system data...")
        self.telemetry_data["pr_telemetry"]["oxygen_tank"] = self.send_command(137)
        self.telemetry_data["pr_telemetry"]["oxygen_pressure"] = self.send_command(138)
        self.telemetry_data["pr_telemetry"]["oxygen_levels"] = self.send_command(139)
        
        # Collecting fan and cooling system data
        print("Getting fan and cooling system data...")
        self.telemetry_data["pr_telemetry"]["fan_pri"] = self.send_command(140)
        self.telemetry_data["pr_telemetry"]["ac_fan_pri"] = self.send_command(141)
        self.telemetry_data["pr_telemetry"]["ac_fan_sec"] = self.send_command(142)
        
        # Collecting cabin environment data
        print("Getting cabin environment data...")
        self.telemetry_data["pr_telemetry"]["cabin_pressure"] = self.send_command(143)
        self.telemetry_data["pr_telemetry"]["cabin_temperature"] = self.send_command(144)
        
        # Collecting power system data
        print("Getting power system data...")
        self.telemetry_data["pr_telemetry"]["battery_level"] = self.send_command(145)
        self.telemetry_data["pr_telemetry"]["power_consumption_rate"] = self.send_command(146)
        self.telemetry_data["pr_telemetry"]["solar_panel_efficiency"] = self.send_command(147)
        
        # Collecting external and coolant data
        print("Getting temperature and coolant data...")
        self.telemetry_data["pr_telemetry"]["external_temp"] = self.send_command(148)
        self.telemetry_data["pr_telemetry"]["pr_coolant_level"] = self.send_command(149)
        self.telemetry_data["pr_telemetry"]["pr_coolant_pressure"] = self.send_command(150)
        self.telemetry_data["pr_telemetry"]["pr_coolant_tank"] = self.send_command(151)
        self.telemetry_data["pr_telemetry"]["radiator"] = self.send_command(152)
        
        # Collecting power, terrain and solar data
        print("Getting motor, terrain, and solar panel data...")
        self.telemetry_data["pr_telemetry"]["motor_power_consumption"] = self.send_command(153)
        self.telemetry_data["pr_telemetry"]["terrain_condition"] = self.send_command(154)
        self.telemetry_data["pr_telemetry"]["solar_panel_dust_accum"] = self.send_command(155)
        
        # Collecting mission data
        print("Getting mission status data...")
        self.telemetry_data["pr_telemetry"]["mission_elapsed_time"] = self.send_command(156)
        self.telemetry_data["pr_telemetry"]["mission_planned_time"] = self.send_command(157)
        self.telemetry_data["pr_telemetry"]["point_of_no_return"] = self.send_command(158)
        self.telemetry_data["pr_telemetry"]["distance_from_base"] = self.send_command(159)
        
        # Collecting destination data
        print("Getting destination data...")
        self.telemetry_data["pr_telemetry"]["switch_dest"] = self.send_command(160)
        self.telemetry_data["pr_telemetry"]["dest_x"] = self.send_command(161)
        self.telemetry_data["pr_telemetry"]["dest_y"] = self.send_command(162)
        self.telemetry_data["pr_telemetry"]["dest_z"] = self.send_command(163)
        
        # Collecting maintenance and simulation data
        print("Getting maintenance and simulation data...")
        self.telemetry_data["pr_telemetry"]["dust_wiper"] = self.send_command(164)

        
        # Getting lidar data
        print("Getting lidar data...")
        self.telemetry_data["pr_telemetry"]["lidar"] = self.send_command(167)
        
        # Save collected data to JSON file
        print("Saving telemetry data to JSON file...")
        self.saveJson(self.targetDir)
        
        print("Data collection complete. Telemetry saved to ROVER_TELEMETRY.json")
        return self.telemetry_data


    # Saves the rover data to a specific directory as a json file.
    def saveJson(self, directory=None, filename="ROVER_TELEMETRY.json"):

        # If no directory is specified, use the current working directory
        if directory is None:
            filepath = filename
        else:
            # Create the directory if it doesn't exist
            if not os.path.exists(directory):
                os.makedirs(directory)
            
            # Combine directory and filename
            filepath = os.path.join(directory, filename)

        # Saves the rover telemetry data to ROVER_TELEMETRY.json if the file
        # does not exist then it is created. 
        # "w" indicates writing mode so the telemetry_data is being 
        # dumped into the file not read.
        with open(filepath, "w") as file:

            # json.dump indicates what is being written to the 
            # ROVER_TELEMETRY.json file indent=4 is just a format to make the 
            # json file easier to read.
            json.dump(self.telemetry_data, file, indent=4)


command = Command()
IPAdress = input("Please enter IP address: ")

command.setIPAdress(IPAdress)

while True:
    command.getData()



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
