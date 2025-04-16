# Kafka Kitchen

A lightweight prototype simulating a restaurant-style order processing system using Kafka.

## Components

- `backend/` – FastAPI service for receiving orders (Kafka producer)
- `processor/` – Background service that consumes and processes Kafka messages
- `php-dashboard/` – Simple PHP web UI to display order status (mimicking legacy systems)
- `docker-compose.yml` – Unified local development setup
- Zookeeper + Kafka – Event streaming backbone

## Prerequisites

- Git + terminal
- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running

## Getting Started

1. Clone the repo and enter the directory:
   ```bash
   git clone github.com/ryangallen/kafka-kitchen
   cd kafka-kitchen
   ```
2. Run the development environment:
   ```bash
   docker-compose up --build
   ```
3. Visit the services in your browser:
   - Backend API (FastAPI): http://localhost:8000
   - PHP Dashboard: http://localhost:8080
