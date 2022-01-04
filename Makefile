build:
	@sudo docker-compose up --build -d

run:
	gunicorn --bind 0.0.0.0:5000 wsgi:app

stop:
	@docker stop $$(sudo docker ps -a -q)

kill:
	@echo "Killing container..."
	@docker kill $$(docker ps -a -q)