COMPOSE_FILE = docker/docker-compose.simple_rtsp.yaml
SERVICE = stream-publisher

.PHONY: init rebuild attach reattach down

init:
	docker-compose -f $(COMPOSE_FILE) up -d

rebuild:
	docker-compose -f $(COMPOSE_FILE) up --build -d

attach:
	docker-compose -f $(COMPOSE_FILE) exec $(SERVICE) bash

down:
	docker-compose -f $(COMPOSE_FILE) down

reattach: down init attach
