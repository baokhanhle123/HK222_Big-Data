import json
import datetime
# Read file dataset.json
#
"""
with open('dataset.json') as f:
     dataset = json.load(f)
     print(len(dataset))
"""

with open('dataset1month.json') as f:
     dataset = json.load(f)
     print(len(dataset))
     time_inter = (dataset[1]['Timestamp'] - dataset[0]['Timestamp'])
     print((time_inter))
