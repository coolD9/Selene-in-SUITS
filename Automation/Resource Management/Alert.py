from datetime import datetime
from Prediction import Prediction
class Alert:
    def __init__(self):
        # 3 - Critical, 2 - Warning, 1 - Caution, 0 - Safe 
        self.criticality = 3

        # 1 - Is 100% (Float)
        self.resourceLevel = {"oxygen": 0, "battery": 0, "water": 0, "co2": 0}

        # Time of alert
        self.timestamp = None

        # Alert message
        self.alertmessage = ""
        
        # Steps taken to resolve the alert
        self.steps = {}
        
    # Update the criticality, resource level, and timestamp continually
    def update(self, criticality, resourceLevel):
        self.criticality = criticality
        self.resourceLevel = resourceLevel
        self.timestamp = datetime.now()
    
    # Send an alert for various reasons including:
    # - Prediction to turn back
    # - Criticality is 3
    def sendAlert(self):
        if(Prediction.turnBack() == True):
            self.alertmessage = "Alert: Turn back"
            return True
        elif(self.criticality == 3):
            self.alertmessage = "Alert: Critical"
            return True
        else:
            return False