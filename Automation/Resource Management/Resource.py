
# Gets the monitored values for resources and stores and processes them here.
class Resource:

    def __init__(self, oxygen, battery, water, co2):
        self.oxygen = oxygen
        self.battery = battery
        self.water = water
        self.co2 = co2

    def update(self, oxygen, battery, water, co2):
        self.oxygen = oxygen
        self.battery = battery
        self.water = water
        self.co2 = co2

    def getOxygen(self):
        return self.oxygen
    
    def getBattery(self):
        return self.battery
    
    def getWater(self):
        return self.water
    
    def getCo2(self):
        return self.co2