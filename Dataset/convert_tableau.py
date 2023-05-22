import time
import json
import datetime
# Read file dataset.json


# Read JSON data from file and write it to a list
dataset = []
with open('dataset.json', 'r') as f:
    dataset= json.load(f)

if dataset:
    print("Dataset loaded successfully")
    
for i in range(len(dataset)):
    dataset[i]['Timestamp'] = datetime.datetime.fromtimestamp(dataset[i]['Timestamp']).strftime("%Y-%m-%d %H:%M:%S")
    
# Write the dataset to a JSON file
with open('dataset_converted.json', 'w') as f:
    json.dump(dataset, f, indent=4)

if dataset:
    print("Dataset transformed successfully")



# Read JSON data from file and write it to a list
dataset = []
with open('dataset1month.json', 'r') as f:
    dataset= json.load(f)

if dataset:
    print("Dataset loaded successfully")
    
for i in range(len(dataset)):
    dataset[i]['Timestamp'] = datetime.datetime.fromtimestamp(dataset[i]['Timestamp']).strftime("%Y-%m-%d %H:%M:%S")
    
# Write the dataset to a JSON file
with open('dataset1month_converted.json', 'w') as f:
    json.dump(dataset, f, indent=4)

if dataset:
    print("Dataset transformed successfully")
