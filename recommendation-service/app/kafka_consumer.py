from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "PRODUCT_CREATED",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x:
        json.loads(x.decode("utf-8"))
)


def consume():

    print("Listening for Kafka events...")

    for message in consumer:

        print("Received Event")

        print(message.value)