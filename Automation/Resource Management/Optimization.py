
from Prediction import Prediction

# Get values from resource class and optimizes the usage of resouces accordingly.
class Optimize:
    def __init__(self, Prediction):
        self.prediction = Prediction
        self.resource = self.prediction.resource

        self.resourceLevels = self.prediction.resourceLevels
    
    # Tracking the rate of usage of resources to identify problems.
    def trackConsumption(self):
        pass
    # Return the new values of usage for resources.
    def optimize(self, resource, hazardLevel=0, missionDuration=None, priorityOverride=None):
        if(self.resourceLevels["oxygen"] == 3):
            # If the criticality is 3, then return the resource levels as they are.
            print("Oxygen criticality is 3")
            return self.resourceLevels
        elif(self.resourceLevels["battery"] == 3):
            # If the criticality is 3, then return the resource levels as they are.
            print("Battery criticality is 3")
            return self.resourceLevels
        elif(self.resourceLevels["water"] == 3):
            # If the criticality is 3, then return the resource levels as they are.
            print("Water criticality is 3")
            return self.resourceLevels
        elif(self.resourceLevels["co2"] == 3):
            # If the criticality is 3, then return the resource levels as they are.
            print("CO2 criticality is 3")
            return self.resourceLevels
        elif(self.resourceLevels["coolant_storage"] == 3):
            # If the criticality is 3, then return the resource levels as they are.
            print("Coolant storage criticality is 3")
            return self.resourceLevels
        elif(self.resourceLevels["temp"] == 3):
            # If the criticality is 3, then return the resource levels as they are.
            print("Temperature criticality is 3")
            return self.resourceLevels
        else:
            # If the criticality is not 3, then optimize the resource levels.
            pass
