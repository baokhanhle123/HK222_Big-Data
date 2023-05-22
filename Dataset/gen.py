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

# Generate a dataset of N records
records_per_household = 6 * 24 * 30 # 1 month of data with 10 minute intervals 
households = 2

delta_volume_constant = random.uniform(0.05, 0.1)

dataset = []

sensor_id = 0
home_id = 0
# time_origin = random.uniform(datetime.datetime(2020, 1, 1).timestamp(), datetime.datetime(2023, 1, 1).timestamp())
time_origin = datetime.datetime(2020, 1, 1).timestamp()

# Generate data for each household
for i in range(households):
    sensor_id += 1
    home_id += 1
    timestamp = time_origin 

    volume_lower_bound = 0.1
    volume_upper_bound = 100
    volume = random.uniform(volume_lower_bound, volume_upper_bound)

    velocity_lower_bound = 1
    velocity_upper_bound = 10
    velocity = random.uniform(velocity_lower_bound, velocity_upper_bound)
    
    pressure_lower_bound = 0
    pressure_upper_bound = 14
    pressure = random.uniform(pressure_lower_bound, pressure_upper_bound)
    
    pH_lower_bound = 6.5
    pH_upper_bound = 8.5
    pH = random.uniform(pH_lower_bound, pH_upper_bound)
    
    temperature_lower_bound = 4
    temperature_upper_bound = 60
    temperature = random.uniform(temperature_lower_bound, temperature_upper_bound)
    
    turbidity_lower_bound = 0
    turbidity_upper_bound = 1
    turbidity = random.uniform(0, 1)
    turbidity = random.uniform(turbidity_lower_bound, turbidity_upper_bound)
    
    pollution_level_lower_bound = 0
    pollution_level_upper_bound = 15
    pollution_level = random.uniform(pollution_level_lower_bound, pollution_level_upper_bound)
    
    for j in range(records_per_household):    
        # Generate random delta values for each parameter
        delta_volume = (delta_volume_constant * (1 + random.uniform(-0.05, 0.05))) + (delta_volume_constant * 100) if random.random() < 0.005 else 0
        delta_velocity = velocity*random.uniform(-0.05, 0.05)
        delta_pressure = pressure*random.uniform(-0.05, 0.05)
        delta_pH = pH*random.uniform(-0.05, 0.05)
        delta_temperature = temperature*random.uniform(-0.05, 0.05)
        delta_turbidity = turbidity*random.uniform(-0.05, 0.05)
        delta_pollution_level = pollution_level*random.uniform(-0.05, 0.05)

        timestamp += 600
        volume += delta_volume
        
        velocity += delta_velocity
        if velocity < velocity_lower_bound:
            velocity = velocity_lower_bound + random.uniform(1, 2)*abs(delta_velocity)
        elif velocity > velocity_upper_bound:
            velocity = velocity_upper_bound - random.uniform(1, 2)*abs(delta_velocity)

        pressure += delta_pressure
        if pressure < pressure_lower_bound:
            pressure = pressure_lower_bound + random.uniform(1, 2)*abs(delta_pressure)
        elif pressure > pressure_upper_bound:
            pressure = pressure_upper_bound - random.uniform(1, 2)*abs(delta_pressure)

        pH += delta_pH
        if pH < pH_lower_bound:
            pH = pH_lower_bound + random.uniform(1, 2)*abs(delta_pH)
        elif pH > pH_upper_bound:
            pH = pH_upper_bound - random.uniform(1, 2)*abs(delta_pH)

        temperature += delta_temperature
        if temperature < temperature_lower_bound:
            temperature = temperature_lower_bound + random.uniform(1, 2)*abs(delta_temperature)
        elif temperature > temperature_upper_bound:
            temperature = temperature_upper_bound - random.uniform(1, 2)*abs(delta_temperature)

        turbidity += delta_turbidity
        if turbidity < turbidity_lower_bound:
            turbidity = turbidity_lower_bound + random.uniform(1, 2)*abs(delta_turbidity)
        elif turbidity > turbidity_upper_bound:
            turbidity = turbidity_upper_bound - random.uniform(1, 2)*abs(delta_turbidity)

        pollution_level += delta_pollution_level
        if pollution_level < pollution_level_lower_bound:
            pollution_level = pollution_level_lower_bound + random.uniform(1, 2)*abs(delta_pollution_level)
        elif pollution_level > pollution_level_upper_bound:
            pollution_level = pollution_level_upper_bound - random.uniform(1, 2)*abs(delta_pollution_level)
         
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
    


