import random
import datetime
import time
import json
import pandas as pd
import numpy as np
import logging
from kafka import KafkaProducer # pip install kafka-python
# from time import time, sleep

# Read JSON data from file and write it to a list
dataset = []
with open('dataset.json', 'r') as f:
    dataset= json.load(f)

logger = logging.getLogger("kafka")
logger.setLevel(logging.WARNING)
producer = KafkaProducer(bootstrap_servers='localhost:9092')

if dataset:
    print("Dataset loaded successfully")
    
for i in range(len(dataset)):
    # Send JSON data to Kafka
    msg = str(dataset[i])
    producer.send('s-fog', bytes(msg, encoding='utf8'))
    print(f"Sensor ID {dataset[i]['SensorId']} from household {dataset[i]['HomeId']} sent to Kafka at {datetime.datetime.fromtimestamp(dataset[i]['Timestamp'])}")
    time.sleep(0.1)