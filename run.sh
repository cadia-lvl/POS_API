docker stop pos
docker container rm pos
docker build . -t glaciersg/pos_api:v1.0.0
docker run -d -p 8080:8080 --name=pos glaciersg/pos_api:v1.0.0
