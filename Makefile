up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose build

migrate:
	docker-compose exec web python manage.py migrate

logs:
	docker-compose logs -f

shell:
	docker-compose exec web python manage.py shell