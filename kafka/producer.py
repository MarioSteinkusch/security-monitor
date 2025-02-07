from kafka import KafkaProducer
import json
import time

# Kafka Producer einrichten
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Beispielhafte Logs erzeugen
logs = [
    {"timestamp": "2025-02-04T12:00:00", "message": "User login attempt", "level": "info"},
    {"timestamp": "2025-02-04T12:05:00", "message": "Failed SSH login", "level": "warning"},
    {"timestamp": "2025-02-04T12:10:00", "message": "Multiple failed logins detected", "level": "critical"},
]

for log in logs:
    producer.send("server-logs", value=log)
    print(f"Sent: {log}")
    time.sleep(2)  # Simuliert Logs in Echtzeit

producer.close()
