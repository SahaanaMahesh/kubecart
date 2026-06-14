from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092"
)

print("CONNECTED")

def publish_event(event_type: str, data: dict):

    producer.send(
        event_type,
        value=data
    )

    producer.flush()

    print(f"Kafka Event Sent -> {event_type}")