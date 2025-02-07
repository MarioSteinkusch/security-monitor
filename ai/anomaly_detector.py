from elasticsearch import Elasticsearch
from transformers import AutoModelForCausalLM, AutoTokenizer
import json

# Verbindung zu Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Llama 2 Modell laden
model_name = "meta-llama/Llama-2-7b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def detect_anomaly(log_text):
    inputs = tokenizer(f"Is this log suspicious? {log_text}", return_tensors="pt")
    output = model.generate(**inputs, max_length=50)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return "anomaly" if "suspicious" in response.lower() else "normal"

# Logs aus Elasticsearch abrufen
response = es.search(index="logs", query={"match_all": {}})
for hit in response["hits"]["hits"]:
    log_text = hit["_source"]["message"]
    status = detect_anomaly(log_text)

    # Log mit KI-Bewertung updaten
    es.update(index="logs", id=hit["_id"], doc={"status": status})
    print(f"Log updated: {log_text} ? {status}")
