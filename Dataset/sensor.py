import random
import datetime
import time

# Generate a dataset of N records
records = 10
time_interval = 5

sensor_id = random.randint(1, 100)
home_id = random.randint(1, 100)
timestamp = random.uniform(datetime.datetime(2020, 1, 1).timestamp(), datetime.datetime(2023, 1, 1).timestamp())
# timestamp = datetime.datetime.fromtimestamp(timestamp)
delta_volume_constant = random.uniform(0.05, 0.1)
volume = random.uniform(0.1, 100)
velocity = random.uniform(1, 10)
pressure = random.uniform(0, 14)
pH = random.uniform(6.5, 8.5)
temperature = random.uniform(4, 60)
turbidity = random.uniform(0, 1)
pollution_level = random.uniform(0, 15)

# Generate data
for j in range(records):    
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

    # Add the values to a dictionary
    record = {
        "SensorId": sensor_id,
        "HomeId": home_id,
        "Timestamp": timestamp,
        "Payload": {
            "Volume": volume,
            "Velocity": velocity,
            "Pressure": pressure,
            "pH": pH,
            "Temperature": temperature,
            "Turbidity": turbidity,
            "Pollution level": pollution_level
        }
    }
    print(record)
    time.sleep(time_interval)
