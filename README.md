# Kafka Kitchen

A lightweight prototype simulating a restaurant-style order processing system using Kafka.

## Components

- `backend/` – FastAPI service for receiving orders (Kafka producer)
- `processor/` – Background service that consumes and processes Kafka messages
- `php-dashboard/` – Simple PHP web UI to display order status (mimicking legacy systems)
- `docker-compose.yml` – Unified local development setup
- Zookeeper + Kafka – Event streaming backbone

## Getting Started

1. Clone the repo and enter the directory:
   ```bash
   git clone github.com/ryangallen/kafka-kitchen
   cd kafka-kitchen
   ```
