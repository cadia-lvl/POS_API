docker stop pos
docker container rm pos
docker build . -t pos:v1
docker run -d -p 8080:8080 --name=pos pos:v1
