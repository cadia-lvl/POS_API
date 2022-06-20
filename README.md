# POS API
This is an API for [POS](https://github.com/cadia-lvl/POS) using the [ELG specification](https://european-language-grid.readthedocs.io/en/stable/all/A3_API/LTInternalAPI.html#basic-api-pattern).
The API is wrapped in a [docker container](https://www.docker.com/) and is implemented using [fastapi](https://github.com/tiangolo/fastapi).

# Getting started
```bash
make build
make run
```

# API calls
All the API calls use post and input/outputs are in a json format.
Further details about the api calls are automatically generated when the container is run and can be found in /docs or /redoc

| HTTP METHOD | Description |
| ----------- | --------------- |
| /tagger | Takes in icelandic text and returns that text along with pos tags for each token in that text |

# Testing
test files can be found in `tests/`. There are two tests that can be performed.
1. Normal api tests: this is where you test the api from the running docker image
2. ELG api tests: this is where you run `docker-compose up` and get an instance as if you where running the docker image on ELG. To submit a api call you then need to send a post request to `/process/service`.

# Acknowledgements
[Reykjavik University](https://lvl.ru.is)

This ELG API was developed in EU's CEF project: [Microservices at your service](https://www.lingsoft.fi/en/microservices-at-your-service-bridging-gap-between-nlp-research-and-industry)

# Underlying tool
The underlying tool is [POS](https://github.com/cadia-lvl/POS) by [Haukur Páll Jónsson](https://github.com/HaukurPall), Örvar Kárason and Steinþór Steingrímsson](https://github.com/steinst), which is licensed under this [Apache License 2.0](https://github.com/cadia-lvl/POS/blob/master/LICENSE). [POS](https://github.com/cadia-lvl/POS) is pip installed from a GitHub repository when the POS_API docker image is built. The [Tokenizer](https://github.com/mideind/Tokenizer) PyPi package is pip installed when the POS_API docker image is built. 
