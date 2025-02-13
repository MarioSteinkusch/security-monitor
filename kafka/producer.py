from kafka import KafkaProducer  # Importiert die KafkaProducer-Klasse aus der kafka-Bibliothek
import json  # Importiert das json-Modul zum Arbeiten mit JSON-Daten
import time  # Importiert das time-Modul zum Arbeiten mit Zeitfunktionen

# Kafka Producer einrichten
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",  # Gibt den Kafka-Broker an, mit dem sich der Producer verbinden soll
    value_serializer=lambda v: json.dumps(v).encode("utf-8")  # Serialisiert die Nachrichten als JSON und kodiert sie als UTF-8
)

# Beispielhafte Logs erzeugen
logs = [
    {"timestamp": "2025-02-04T12:00:00", "message": "User login attempt", "level": "info"},  # Ein Info-Log für einen Benutzeranmeldeversuch
    {"timestamp": "2025-02-04T12:05:00", "message": "Failed SSH login", "level": "warning"},  # Ein Warn-Log für einen fehlgeschlagenen SSH-Anmeldeversuch
    {"timestamp": "2025-02-04T12:10:00", "message": "Multiple failed logins detected", "level": "critical"},  # Ein kritisches Log für mehrere fehlgeschlagene Anmeldeversuche
]

for log in logs:  # Iteriert über jedes Log in der logs-Liste
    producer.send("server-logs", value=log)  # Sendet das Log an das Kafka-Topic "server-logs"
    print(f"Sent: {log}")  # Gibt das gesendete Log auf der Konsole aus
    time.sleep(2)  # Simuliert Logs in Echtzeit, indem es 2 Sekunden wartet

producer.close()  # Schließt den Kafka-Producer
