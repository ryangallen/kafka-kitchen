#!/bin/bash

docker run --network=kafka-kitchen_default --rm confluentinc/cp-kafka:7.5.0 \
  kafka-topics --create \
  --bootstrap-server kafka:9092 \
  --replication-factor 1 \
  --partitions 1 \
  --topic orders.incoming
