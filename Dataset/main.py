import time
import json
import datetime
# Read file dataset.json
#
"""
with open('dataset.json') as f:
     dataset = json.load(f)
     print(len(dataset))
"""

# Read JSON data from file and write it to a list
dataset = []
with open('dataset.json', 'r') as f:
    dataset= json.load(f)

if dataset:
    print("Dataset loaded successfully")
    
for i in range(len(dataset)):
    # Send JSON data to Kafka
    print(f"Sensor ID {dataset[i]['SensorId']} from household {dataset[i]['HomeId']} sent to Kafka at {datetime.datetime.fromtimestamp(dataset[i]['Timestamp'])}")
    print(type(dataset[i]['Timestamp']))
    time.sleep(1)
