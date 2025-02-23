from sklearn import tree
import numpy as pd
from sklearn.ensemble import RandomForestClassifier



class Prediction:


    def __init__(self, resource):

        self.resource = resource
        # 1 is warning, 2 is caution, 3 is safe
        self.resourceLevels = {"oxygen":0, "battery":0, "water":0, "co2":0}

        
    # Will use training data to improve Prediction system.
    def train(self, trainingData):
        pass

    # Checking resources to determine criticality
    def checkResourceLevels(self, resource):
        if(self.resource.getOxygen() > 0.7):
            self.resourceLevels["oxygen"] = 3
        elif(self.resource.getOxygen() > 0.4):
            self.resourceLevels["oxygen"] = 2
        else:
            self.resourceLevels["oxygen"] = 1

        if(self.resource.getBattery() > 0.7):
            self.resourceLevels["battery"] = 3
        elif(self.resource.getBattery() > 0.4):
            self.resourceLevels["battery"] = 2
        else:
            self.resourceLevels["battery"] = 1

        if(self.resource.getWater() > 0.7):
            self.resourceLevels["water"] = 3
        elif(self.resource.getWater() > 0.4):
            self.resourceLevels["water"] = 2
        else:
            self.resourceLevels["water"] = 1
        
        if(self.resource.getCo2() > 0.7):
            self.resourceLevels["co2"] = 3
        elif(self.resource.getCo2() > 0.4):
            self.resourceLevels["co2"] = 2
        else:
            self.resourceLevels["co2"] = 1
            

    def predictResources(self):
        pass


    # Returns a bool
    def turnBack(self):
        pass



    
