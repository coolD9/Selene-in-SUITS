from sklearn import tree
import numpy as pd
from sklearn.ensemble import RandomForestClassifier



class Prediction:

    def __init__(self, resource):

        self.resource = resource

    # Will use training data to improve Prediction system.
    def train(self, trainingData):
        pass

    def determineCriticality(self):
        pass

    def checkResourceLevels(self, resource):
        self.resource = resource

    def predictResources(self):
        pass
    

    # Returns a bool
    def turnBack(self):
        pass



    
