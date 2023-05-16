"""
This program generates a dataset of 1000 records with the following characteristics:
• SensorId: Randomly generated between 1 and 100.
• HomeId: Randomly generated between 1 and 100.
• Timestamp: Randomly generated between 1/1/2020 and 1/1/2023.
• Payload fields:
– Volume: Randomly generated between 0.1 and 100.
– Velocity: Randomly generated between 1 and 10.
– Pressure: Randomly generated between 0 and 14.
– pH: Randomly generated between 6.5 and 8.5.
– Temperature: Randomly generated between 4 and 60.
– Turbidity: Randomly generated between 0 and 1.
– Pollution level: Randomly generated between 0 and 15.


The trend of the data for a single household can vary depending on several factors such as water usage patterns, weather conditions, water source and treatment, etc. However, here are some possible trends for each of the measured parameters:

- One sensor per household: Each household should have one sensor that measures all the parameters

- All sensor should have the same sampling rate: All sensors should have the same sampling rate

- The sensor records data every 10 minutes: The sensor should record data every 10 minutes

- Volume: The volume of water used in a household should increase constantly with random variation

- Velocity: The water flow rate in a household should remain constant with random variation

- Pressure: The water pressure in a household should remain constant with random variation

- pH: The pH level of water in a household should remain constant with random variation

- Temperature: The water temperature in a household should remain constant with random variation

- Turbidity: The turbidity of water in a household should remain constant with random variation

- Pollution level: The pollution level of water in a household should remain constant with random variation
"""

import random
import datetime
import json

# Generate a dataset of 1 month records
records_per_household = 4320 * 24 # 1 month * 24 = 2 years
households = 10

delta_volume_constant = random.uniform(0.05, 0.1)

dataset = []
dataset1month = []

sensor_id = 0
home_id = 0
# time_origin = random.uniform(datetime.datetime(2020, 1, 1).timestamp(), datetime.datetime(2023, 1, 1).timestamp())
time_origin = datetime.datetime(2020, 1, 1).timestamp()

# Generate data for each household
for i in range(households):
    sensor_id += 1
    home_id += 1
    timestamp = time_origin 

    volume = random.uniform(0.1, 100)
    velocity = random.uniform(1, 10)
    pressure = random.uniform(0, 14)
    pH = random.uniform(6.5, 8.5)
    temperature = random.uniform(4, 60)
    turbidity = random.uniform(0, 1)
    pollution_level = random.uniform(0, 15)
    
    for j in range(records_per_household):    
        # Generate random delta values for each parameter
        delta_volume = delta_volume_constant + delta_volume_constant*random.uniform(-0.1, 0.1)
        delta_velocity = velocity*random.uniform(-0.1, 0.1)
        delta_pressure = pressure*random.uniform(-0.1, 0.1)
        delta_pH = pH*random.uniform(-0.1, 0.1)
        delta_temperature = temperature*random.uniform(-0.1, 0.1)
        delta_turbidity = turbidity*random.uniform(-0.1, 0.1)
        delta_pollution_level = pollution_level*random.uniform(-0.1, 0.1)

        timestamp += 600
        volume += delta_volume
        velocity += delta_velocity
        pressure += delta_pressure
        pH += delta_pH
        temperature += delta_temperature
        turbidity += delta_turbidity
        pollution_level += delta_pollution_level

         
        record = {
            "SensorId": sensor_id,
            "HomeId": home_id,
            "Timestamp": timestamp,
            "Volume": volume,
            "Velocity": velocity,
            "Pressure": pressure,
            "pH": pH,
            "Temperature": temperature,
            "Turbidity": turbidity,
            "Pollution level": pollution_level
        }
        dataset.append(record)    

# print(dataset)

# Write the dataset to a JSON file
with open('dataset.json', 'w') as f:
    json.dump(dataset, f, indent=4)

# Create in 1 month interval
for i in range(len(dataset)):
    if (i % 4320 == 0):
        dataset1month.append(dataset[i])
        
with open('dataset1month.json', 'w') as f:
    json.dump(dataset1month, f, indent=4)

    


