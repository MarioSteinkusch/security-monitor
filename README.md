# 📌 Intelligenter Security-Monitor für Serverlogs

## **🚀 Projektübersicht**
Ein Kafka-gestützter Sicherheitsmonitor, der Server-Logs in Echtzeit verarbeitet, mit **Llama 2** auf Anomalien scannt und in **Elasticsearch** speichert.

### **🔹 Technologien**
✅ **Apache Kafka** → Log-Streaming in Echtzeit  
✅ **Elasticsearch** → Speicherung & Suche von Logs  
✅ **Llama 2** → KI-gestützte Anomalie-Erkennung  
✅ **Kubernetes** → Skalierbares Deployment  
✅ **GitHub Copilot** → Unterstützung beim Entwickeln  

---
## **📂 Projektstruktur**
```
/security-monitor
 ├── /kafka            # Kafka Producer & Consumer
 │    ├── producer.py  # Sendet Logs an Kafka
 │    ├── consumer.py  # Verarbeitet Logs & speichert in Elasticsearch
 │
 ├── /ai               # Llama 2 Modell für Anomalie-Erkennung
 │    ├── anomaly_detector.py  # Erkennung verdächtiger Logs
 │
 ├── /kubernetes       # Kubernetes YAML-Files für Deployment
 │    ├── kafka-deployment.yaml
 │    ├── elasticsearch-deployment.yaml
 │    ├── llama2-deployment.yaml
 │
 ├── /dashboard        # Web-Dashboard für Monitoring (z. B. Flask / React)
 │    ├── app.py       # REST API für Log-Abfragen
 │    ├── templates/   # Web-Oberfläche
 │
 ├── /config           # Konfigurationsdateien für Kafka & Elasticsearch
 │    ├── settings.json
 │
 ├── docker-compose.yml  # Docker-Setup für lokale Entwicklung
 ├── README.md         # Dokumentation & Setup-Anleitung
 ├── LICENSE           # MIT License
```

---
## **📌 Geplante Features**
🔹 **Echtzeit-Log-Streaming** mit Kafka  
🔹 **KI-gestützte Anomalie-Erkennung** mit Llama 2  
🔹 **Elasticsearch & Kibana für Suche & Visualisierung**  
🔹 **Web-Dashboard für Security-Monitoring**  
🔹 **REST API für Abfragen & Automatisierung**  

---
## **📌 Setup-Anleitung**
### **1️⃣ Starten von Kafka & Elasticsearch mit Docker**
```sh
docker-compose up -d
```

### **2️⃣ Kafka-Producer starten (Logs simulieren)**
```sh
python kafka/producer.py
```

### **3️⃣ Kafka-Consumer starten (Logs verarbeiten & speichern)**
```sh
python kafka/consumer.py
```

### **4️⃣ Kibana öffnen (Elasticsearch-Visualisierung)**
🔗 [http://localhost:5601](http://localhost:5601)
