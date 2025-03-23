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
        

        self.evaTelemetry = {
             "telemetry": 
             {
                "eva_time": 0,
                "eva1": {
                    "batt_time_left": 5077.148926,
                    "oxy_pri_storage": 23.755802,
                    "oxy_sec_storage": 15.489529,
                    "oxy_pri_pressure": 0.000000,
                    "oxy_sec_pressure": 0.000000,
                    "oxy_time_left": 4238,
                    "heart_rate": 90.000000,
                    "oxy_consumption": 0.000000,
                    "co2_production": 0.000000,
                    "suit_pressure_oxy": 3.072300,
                    "suit_pressure_co2": 0.005900,
                    "suit_pressure_other": 11.554200,
                    "suit_pressure_total": 14.632401,
                    "fan_pri_rpm": 0.000000,
                    "fan_sec_rpm": 0.000000,
                    "helmet_pressure_co2": 0.000000,
                    "scrubber_a_co2_storage": 0.000000,
                    "scrubber_b_co2_storage": 0.000000,
                    "temperature": 70.000000,
                    "coolant_ml": 20.508068,
                    "coolant_gas_pressure": 0.000000,
                    "coolant_liquid_pressure": 0.000000
                },
                "eva2": {
                    "batt_time_left": 3384.893799,
                    "oxy_pri_storage": 24.231962,
                    "oxy_sec_storage": 19.419136,
                    "oxy_pri_pressure": 0.000000,
                    "oxy_sec_pressure": 0.000000,
                    "oxy_time_left": 4714,
                    "heart_rate": 90.000000,
                    "oxy_consumption": 0.000000,
                    "co2_production": 0.000000,
                    "suit_pressure_oxy": 3.072300,
                    "suit_pressure_cO2": 0.005900,
                    "suit_pressure_other": 11.554200,
                    "suit_pressure_total": 14.632401,
                    "fan_pri_rpm": 0.000000,
                    "fan_sec_rpm": 0.000000,
                    "helmet_pressure_co2": 0.000000,
                    "scrubber_a_co2_storage": 0.000000,
                    "scrubber_b_co2_storage": 0.000000,
                    "temperature": 70.000000,
                    "coolant_ml": 22.034748,
                    "coolant_gas_pressure": 0.000000,
                    "coolant_liquid_pressure": 0.000000
                }
            }
        }
        
        self.uia = {
             "uia": 
             {
                "eva1_power":        False,
                "eva1_oxy":          False,
                "eva1_water_supply": False,
                "eva1_water_waste":  False,
                "eva2_power":        False,
                "eva2_oxy":          False,
                "eva2_water_supply": False,
                "eva2_water_waste":  False,
                "oxy_vent":          False,
                "depress":           False
            }
        }
        self.rover = {
             "rover": 
                {
                "posx": 0.000000,
                "posy": 0.000000,
                "poi_1_x": 0.000000,
                "poi_1_y": 0.000000,
                "poi_2_x": 0.000000,
                "poi_2_y": 0.000000,
                "poi_3_x": 0.000000,
                "poi_3_y": 0.000000
                }
        }
        self.dcu = {
             "dcu": 
             {
                "eva1": {
                    "batt": False,
                    "oxy": False,
                    "comm": False,
                    "fan": False,
                    "pump": False,
                    "co2": False
                },
                "eva2": {
                    "batt": False,
                    "oxy": False,
                    "comm": False,
                    "fan": False,
                    "pump": False,
                    "co2": False
                }
            }
        }


        # Stores positon fo the EVA.
        self.imu = {
             "imu": 
             {
                "eva1": {
                    "posx": 0.000000,
                    "posy": 0.000000,
                    "heading": 0.000000
                },
                "eva2": {
                    "posx": 0.000000,
                    "posy": 0.000000,
                    "heading": 0.000000
                }
            }
        }
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


