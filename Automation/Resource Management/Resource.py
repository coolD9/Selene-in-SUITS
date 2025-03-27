
import json
import os
import time

# Gets the monitored values for resources and stores and processes them here.
class Resource:

# oxygen has primary storage, secondary storage, primary partial pressure, and secondary partial pressure
# battery has time left
# water has amount left
# co2 has amount left
# coolant_storage has amount left
    def __init__(self, oxygen=0, battery=0, water=0, co2=0, coolant_storage=0, temp=0):
        self.oxygen = {
            "pri_storage": oxygen,
            "sec_storage": oxygen,
            "pri_pressure": 0,
            "sec_pressure": 0
        }
        self.battery = battery
        self.water = water
        self.co2 = co2
        self.coolant_storage = coolant_storage
        self.temp = temp
        self.path = "User_Interface/UI_Main/client/src/telemetry_json/TELEMETRY.json"

        self.currentData = None
        self.oldDataFile = None

    def loadJson(self):
         
        try:
            with open(self.path, 'r') as file:
                print(f"Loading telemetry data from {self.path}")
                return json.load(file)

        except FileNotFoundError:
            print(f"Error: File {self.path} not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {self.path}")
            return None
        
    def monitorData(self):
        print(f"Monitoring file: {self.path}")

        # Stores the old version of the Json file.
        self.oldDataFile = os.path.getmtime(self.path)


        try: 
            while True:
                self.currentData = os.path.getmtime(self.path)

                # Checks if the JSON file has been updated.
                # If so, the new Json file will be processed instead.
                if self.currentData != self.oldDataFile:
                    print("\n--- File Updated ---")
                    data = self.loadJson(self.path)

                    if data is not None:
                        print("Updated JSON Data:")

                    self.oldDataFile = self.currentData

                # Checks the JSON file every second.
                time.sleep(1)
                

        except:
            pass


    def update(self, pri_oxygen, sec_oxygen, pri_pressure, sec_pressure, battery, water, co2, coolant_storage, temp):
        

        self.oxygen['pri_storage'] = pri_oxygen
        self.oxygen['sec_storage'] = sec_oxygen
        self.oxygen['pri_pressure'] = pri_pressure
        self.oxygen['sec_pressure'] = sec_pressure

        
        self.battery = battery
        self.water = water
        self.co2 = co2
        self.coolant_storage = coolant_storage
        self.temp = temp



    def getOxygen(self):
        return self.oxygen
    
    def getBattery(self):
        return self.battery
    
    def getWater(self):
        return self.water
    
    def getCo2(self):
        return self.co2
    
    def getCoolantStorage(self):
        return self.coolant_storage
    
    def getTemp(self):
        return self.temp
    

resource = Resource()
resource.loadJson()
resource.monitorData()
    



