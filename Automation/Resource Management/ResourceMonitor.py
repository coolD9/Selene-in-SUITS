from sklearn.datasets import load_iris
from sklearn import tree
# from PredictiveAnalysis.py import PredictiveAnalysis
# from AlertSystem.py import AlertSystem
# from Alert.py import Alert

# Load the iris dataset
iris = load_iris()
x, y = iris.data, iris.target   
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

# Resource values
oxygenL, batteryL, co2L, waterL = 0.1, 0.3, 0.2, 0.4

# ResourceMonitor class
class ResourceMonitor:
    def __init__(self, oxygenL, batteryL, co2L, waterL):
        self.oxygenL = oxygenL
        self.batteryL = batteryL
        self.co2L = co2L
        self.waterL = waterL

    # readSensors method (Needs resources from outside file)
    def readSensors(self):
        oxygen = self.oxygenL
        battery = self.batteryL
        co2 = self.co2L
        water = self.waterL
        # get_tree_stats() should be considered
        print("Oxygen level: ", oxygen, "Battery level: ", battery, "CO2 level: ", co2, "Water level: ", water)

    # logData method (Needs to be trained)
    def logData(self):
        print("Data logged")

# Training is needed to perform plot_tree function
# tree.plot_tree(clf)
