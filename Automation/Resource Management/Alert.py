from Prediction import Prediction
class Alert:
    def __init__(self):
        # 3 - Critical, 2 - Warning, 1 - Caution, 0 - Safe 
        self.criticality = 3

        # 1 - Is 100% (Float)
        self.resourceLevel = {"oxygen": 0, "battery": 0, "water": 0, "co2": 0}
        
        self.steps = {}
        
    def update(self, criticality, resourceLevel):
        self.criticality = criticality
        self.resourceLevel = resourceLevel
    
    def sendAlert(self):
        if(Prediction.turnBack() == True):
            print("Alert: Turn back")
            return True
        elif(self.criticality == 3):
            print("Alert: Critical")
            return True
        else:
            return False
        
        pass