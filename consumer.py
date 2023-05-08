import logging
from kafka import KafkaConsumer

# logging.basicConfig(level=logging.DEBUG)
logging.getLogger("kafka").setLevel(logging.WARNING)

consumer = KafkaConsumer(
    's-fog',
    bootstrap_servers=['localhost:9092'],
    group_id='my_group',
    enable_auto_commit=False,
    value_deserializer=lambda x: x.decode('utf-8'),
    auto_offset_reset='earliest'
)

for message in consumer:
    print(f'Received message: {message.value}')