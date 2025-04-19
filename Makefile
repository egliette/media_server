COMPOSE_FILE = docker-compose.yaml
SERVICE = stream-publisher

up:
	docker-compose -f $(COMPOSE_FILE) up -d

rebuild:
	docker-compose -f $(COMPOSE_FILE) up --build -d

attach:
	docker-compose -f $(COMPOSE_FILE) exec $(SERVICE) bash

down:
	docker-compose -f $(COMPOSE_FILE) down

restart:
	docker-compose -f $(COMPOSE_FILE) restart

hard-restart:
	make down
	make up

reattach: down up attach
