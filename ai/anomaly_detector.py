from elasticsearch import Elasticsearch  # Importiere die Elasticsearch-Bibliothek
from transformers import AutoModelForCausalLM, AutoTokenizer  # Importiere die notwendigen Klassen von Transformers
import json  # Importiere die JSON-Bibliothek

# Verbindung zu Elasticsearch
es = Elasticsearch("http://localhost:9200")  # Stelle eine Verbindung zu einem lokalen Elasticsearch-Server her

# Llama 2 Modell laden
model_name = "meta-llama/Llama-2-7b-chat-hf"  # Definiere den Namen des zu ladenden Modells
tokenizer = AutoTokenizer.from_pretrained(model_name)  # Lade den Tokenizer für das Modell
model = AutoModelForCausalLM.from_pretrained(model_name)  # Lade das Modell selbst

def detect_anomaly(log_text):
    # Funktion zur Anomalieerkennung in Logs
    inputs = tokenizer(f"Is this log suspicious? {log_text}", return_tensors="pt")  # Tokenisiere den Eingabetext
    output = model.generate(**inputs, max_length=50)  # Generiere eine Antwort mit dem Modell, dabei gibt "max_length=50" die maximale Länge der generierten Antwort in Token an
    response = tokenizer.decode(output[0], skip_special_tokens=True)  # Dekodiere die Antwort
    return "anomaly" if "suspicious" in response.lower() else "normal"  # Gib "anomaly" zurück, wenn "suspicious" in der Antwort enthalten ist, sonst "normal"

# Logs aus Elasticsearch abrufen
response = es.search(index="logs", query={"match_all": {}})  # Suche alle Logs im "logs"-Index
for hit in response["hits"]["hits"]: # Zugriff auf jedes einzelne Suchergebnis, in diesem Fall "logs"
    log_text = hit["_source"]["message"]  # Extrahiere den Log-Text aus dem Treffer
    status = detect_anomaly(log_text)  # Erkenne Anomalien im Log-Text

    # Log mit KI-Bewertung updaten
    es.update(index="logs", id=hit["_id"], doc={"status": status})  # Aktualisiere den Log-Eintrag mit dem Anomalie-Status
    print(f"Log updated: {log_text} ? {status}")  # Drucke eine Bestätigung der Aktualisierung
