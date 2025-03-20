import csv
from datetime import datetime
from Alert import Alert


class LogAlert:

    def __init__(self, alert):
        self.alert = alert

        self.file1 = open("Log.txt")

    def logData(self):
        # Unimplemented.
        self.file1.write(self.alert.timestamp, ": ", self.alert.resource,", ", self.alert.criticality, self.alert.alertmessage)

class LogData:
    def __init__(self, o2, battery, water, co2, coolant_storage, temp):
        self.o2 = o2
        self.battery = battery
        self.water = water
        self.co2 = co2
        self.coolant = coolant_storage
        self.temp = temp


        self.index = 0

        self.log_file = 'log_data.csv'
        self._log_values()

    def _log_values(self):
        #Log the current values to a CSV file.
        with open(self.log_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), self.o2, self.battery, self.water, self.co2, self.coolant, self.temp])

    def retrieve_past_data(self, variable, limit=None):
        #Retrieve past data for a specific variable.
        data = []
        with open(self.log_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:  
                timestamp = row[0]

                if variable == 'o2_pri_storage':
                    value = row[1]
                
                elif variable == 'o2_sec_storage':
                    value = row[2]

                elif variable == 'o2_pri_pressure':
                    value = row[3]

                elif variable == 'o2_sec_pressure':
                    value = row[4]

                elif variable == 'battery':
                    value = row[5]

                elif variable == 'water':
                    value = row[6]

                elif variable == 'co2':
                    value = row[7]

                elif variable == 'coolant':
                    value = row[8]
                
                elif variable == 'temp':
                    value = row[9]

                else:
                    raise ValueError("Invalid variable specified.")
                data.append((timestamp, value))

        if limit is not None:    # Gets all data from a variable 
            data = data[-limit:] # If user does not specify a limit

        return data
