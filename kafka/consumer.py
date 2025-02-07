from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json

# Verbindung zu Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Kafka Consumer einrichten
consumer = KafkaConsumer(
    "server-logs",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

for message in consumer:
    log_entry = message.value
    print(f"Received log: {log_entry}")

    # Log in Elasticsearch speichern
    es.index(index="logs", document=log_entry)
    print(f"Saved to Elasticsearch: {log_entry}")
