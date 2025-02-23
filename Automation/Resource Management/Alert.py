from Prediction import Prediction
class Alert:
    def __init__(self):
        # 1 - Warning, 2 - Caution, 3 - Safe 
        self.criticality = 3

        # 1 - Is 100% (Float)
        self.resourceLevel = {"oxygen": 1,
                               "battery": 1,
                                "water": 1,
                                "co2": 1}
        
        self.steps = {}
        
    def update(self, criticality, resourceLevel):
        self.criticality = criticality
        self.resourceLevel = resourceLevel
    
    def sendAlert(self):
        pass
        