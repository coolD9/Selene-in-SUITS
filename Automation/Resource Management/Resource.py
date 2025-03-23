
# Gets the monitored values for resources and stores and processes them here.
class Resource:

# oxygen has primary storage, secondary storage, primary partial pressure, and secondary partial pressure
# battery has time left
# water has amount left
# co2 has amount left
# coolant_storage has amount left
    def __init__(self, oxygen, battery, water, co2, coolant_storage, temp):
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


