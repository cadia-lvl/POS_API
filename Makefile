build:
	docker build . -t pos_api
run:
	docker run -d -p 8080:8080 --name=pos pos_api
