import json
import time
from datetime import datetime, timezone
from confluent_kafka import Producer

# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092'  # Update this to match your Kafka broker address
}

# Initial message
message = {
    "cust_id": 1313131,
    "month": 12,
    "expenses": 1313.13,
    "counter": 1,
    "current_dt": datetime.now(timezone.utc).strftime("%Y-%m-%d at %H:%M:%S.%f UTC")
}

def produce_message(topic, message):
    producer = Producer(conf)
    while message['counter'] <= 999:
        producer.produce(topic, json.dumps(message).encode('utf-8'))
        producer.flush()
        message['counter'] += 1
        message['current_dt'] = datetime.now(timezone.utc).strftime("%Y-%m-%d at %H:%M:%S.%f UTC")
        time.sleep(1)  # Simulate some delay
    producer.close()

if __name__ == "__main__":
    produce_message('topic1', message)
