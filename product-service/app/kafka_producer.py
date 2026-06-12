from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v:
        json.dumps(v).encode("utf-8")
)

def publish_event(event_type: str, data: dict):

    producer.send(
        event_type,
        value=data
    )

    producer.flush()

    print(f"Kafka Event Sent -> {event_type}")