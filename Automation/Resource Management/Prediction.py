from sklearn import tree
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from Resource import Resource

class Prediction:
    def __init__(self, resource):
        # Store the resource object instead of inheriting from it
        self.resource = resource
        # 3 is critical, 2 is warning, 1 is caution, 0 is safe
        self.resourceLevels = {"oxygen": 0, "battery": 0, "water": 0, "co2": 0, "coolant_storage": 0, "temp": 0}
        
    # Will use training data to improve Prediction system.
    def train(self, trainingData):
        pass
    
    # Checking resources to determine criticality
    def checkResourceLevels(self):
        # Oxygen checks
        primary_oxygen = self.resource.getOxygen()["pri_storage"]
        if primary_oxygen > 0.7:
            self.resourceLevels["oxygen"] = 3
        elif primary_oxygen > 0.4:
            self.resourceLevels["oxygen"] = 2
        else:
            self.resourceLevels["oxygen"] = 1
            
        # max function used to keep highest criticality level
        secondary_oxygen = self.resource.getOxygen()["sec_storage"]
        if secondary_oxygen > 0.7:
            self.resourceLevels["oxygen"] = max(self.resourceLevels["oxygen"], 3)
        elif secondary_oxygen > 0.4:
            self.resourceLevels["oxygen"] = max(self.resourceLevels["oxygen"], 2)
        else:
            self.resourceLevels["oxygen"] = max(self.resourceLevels["oxygen"], 1)
            
        primary_pressure = self.resource.getOxygen()["pri_pressure"]
        if primary_pressure > 0.7:
            self.resourceLevels["oxygen"] = max(self.resourceLevels["oxygen"], 3)
        elif primary_pressure > 0.4:
            self.resourceLevels["oxygen"] = max(self.resourceLevels["oxygen"], 2)
        else:
            self.resourceLevels["oxygen"] = max(self.resourceLevels["oxygen"], 1)
    
        secondary_pressure = self.resource.getOxygen()["sec_pressure"]
        if secondary_pressure > 0.7:
            self.resourceLevels["oxygen"] = max(self.resourceLevels["oxygen"], 3)
        elif secondary_pressure > 0.4:
            self.resourceLevels["oxygen"] = max(self.resourceLevels["oxygen"], 2)
        else:
            self.resourceLevels["oxygen"] = max(self.resourceLevels["oxygen"], 1)
    
        # Battery check
        battery = self.resource.getBattery()
        if battery > 0.7:
            self.resourceLevels["battery"] = 3
        elif battery > 0.4:
            self.resourceLevels["battery"] = 2
        else:
            self.resourceLevels["battery"] = 1
    
        # Water check
        water = self.resource.getWater()
        if water > 0.7:
            self.resourceLevels["water"] = 3
        elif water > 0.4:
            self.resourceLevels["water"] = 2
        else:
            self.resourceLevels["water"] = 1
            
        # CO2 check
        co2 = self.resource.getCo2()
        if co2 > 0.7:
            self.resourceLevels["co2"] = 3
        elif co2 > 0.4:
            self.resourceLevels["co2"] = 2
        else:
            self.resourceLevels["co2"] = 1
    
        # Coolant storage check
        coolant = self.resource.getCoolantStorage()
        if coolant > 0.7:
            self.resourceLevels["coolant_storage"] = 3
        elif coolant > 0.4:
            self.resourceLevels["coolant_storage"] = 2
        else:
            self.resourceLevels["coolant_storage"] = 1
    
        # Temperature check
        temp = self.resource.getTemp()
        if temp > 0.7:
            self.resourceLevels["temp"] = 3
        elif temp > 0.4:
            self.resourceLevels["temp"] = 2
        else:  
            self.resourceLevels["temp"] = 1
    
    def predictResources(self):
        pass
    
    # Returns a bool
    def turnBack(self):
        # Check if any critical resources are below threshold
        if (self.resourceLevels["oxygen"] < 3 or 
            self.resourceLevels["battery"] < 3 or 
            self.resourceLevels["water"] < 3 or 
            self.resourceLevels["co2"] < 3 or
            self.resourceLevels["coolant_storage"] < 3 or
            self.resourceLevels["temp"] < 3):
            return True
        else:
            return False