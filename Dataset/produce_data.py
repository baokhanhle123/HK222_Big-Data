import random
import datetime
import time
import json

# Read JSON data from file and write it to a list
dataset = []
with open('dataset.json', 'r') as f:
    dataset= json.load(f)

if dataset:
    print("Dataset loaded successfully")
    
for i in range(len(dataset)):
    # Send JSON data to Kafka
    # producer.send('sensor', dataset[i])
    print(f"Sensor ID {dataset[i]['SensorId']} from household {dataset[i]['HomeId']} sent to Kafka at {datetime.datetime.fromtimestamp(dataset[i]['Timestamp'])}")
    time.sleep(1)