import json
import time
from datetime import datetime, timezone
from confluent_kafka import Consumer, Producer, KafkaError

# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Ensure this matches your Kafka broker address
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
}

def consume_message(topic, next_topic):
    consumer = Consumer(conf)
    producer = Producer(conf)
    consumer.subscribe([topic])
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
        message = json.loads(msg.value().decode('utf-8'))
        print(f"Consumed message from {topic}: {message}")  # Log the consumed message and topic
        if message['counter'] >= 999:
            print("Counter reached 999. Stopping.")
            break
        message['counter'] += 1
        message['current_dt'] = datetime.now(timezone.utc).strftime("%Y-%m-%d at %H:%M:%S.%f UTC")
        producer.produce(next_topic, json.dumps(message).encode('utf-8'))
        producer.flush()
        print(f"Produced message to {next_topic}: {message}")  # Log the produced message and next topic
    consumer.close()
    producer.close()

if __name__ == "__main__":
    consume_message('topic1', 'topic2')
