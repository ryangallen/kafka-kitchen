from confluent_kafka import Producer
from fastapi import FastAPI, Request
import json

app = FastAPI()

KAFKA_CONFIG = {
    "bootstrap.servers": "kafka:9092",
    "client.id": "kitchen-backend",
}

producer = Producer(KAFKA_CONFIG)
TOPIC = 'orders.incoming'


@app.get("/")
def read_root():
    return {"status": "backend is up"}


@app.post("/orders")
async def create_order(request: Request):
    payload = await request.json()

    try:
        producer.produce(TOPIC, json.dumps(payload).encode('utf-8'))
        producer.flush()
        return {"status": "✓ order sent to the kitchen", "order": payload}
    except Exception as exc:
        return {"error": str(exc)}
