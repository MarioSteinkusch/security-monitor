from kafka import KafkaConsumer  # Importiere KafkaConsumer aus dem kafka Modul
from elasticsearch import Elasticsearch  # Importiere Elasticsearch aus dem elasticsearch Modul
import json  # Importiere das json Modul

# Verbindung zu Elasticsearch
es = Elasticsearch("http://localhost:9200")  # Erstelle eine Verbindung zu einem Elasticsearch-Server, der auf localhost:9200 läuft

# Kafka Consumer einrichten
consumer = KafkaConsumer(  # Erstelle einen KafkaConsumer
    "server-logs",  # Abonniere das Kafka-Topic "server-logs"
    bootstrap_servers="localhost:9092",  # Verbinde dich mit dem Kafka-Server auf localhost:9092
    auto_offset_reset="earliest",  # Setze den Offset auf den frühesten verfügbaren, wenn kein Offset gefunden wird
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))  # Deserialisiere die Nachrichtenwerte von JSON
)

for message in consumer:  # Iteriere über die Nachrichten im Kafka-Topic
    log_entry = message.value  # Extrahiere den Nachrichtenwert
    print(f"Received log: {log_entry}")  # Gib das empfangene Log im Terminal aus

    # Log in Elasticsearch speichern
    es.index(index="logs", document=log_entry)  # Speichere das Log in Elasticsearch im Index "logs"
    print(f"Saved to Elasticsearch: {log_entry}")  # Gib aus, dass das Log in Elasticsearch gespeichert wurde
