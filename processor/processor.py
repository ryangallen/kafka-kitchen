from confluent_kafka import Consumer
import json

KAFKA_CONFIG = {
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'kitchen-processor',
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(KAFKA_CONFIG)
consumer.subscribe(['orders.incoming'])

print('Processor is running and awaiting orders...')

try:
    while True:
        msg = consumer.poll(1.0)  # timeout seconds
        if msg is None:
            continue
        if msg.error():
            print(f'Order received: {data}')
except KeyboardInterrupt:
    print('Shutting down processor.')
finally:
    consumer.close()

