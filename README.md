# flyio-fastapi-poetry-template
Template to run fast api in fly.io with poetry as env manager 


# How to run in local

Use this
```sh
poetry run uvicorn flyio_fastapi_poetry_template.main:app     
```

The structure of the folder is inspire on [this](https://fastapi.tiangolo.com/tutorial/bigger-applications/)



# How to start docker

```sh
$ docker build -t poetry-demo:latest .   
$ docker run -p 3001:8000 --rm --name prueba  -d poetry-demo:latest
$ curl http://localhost:3001 
```

