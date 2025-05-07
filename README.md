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

# 🚀 How to Get Started
1. Install flyctl
    
    Follow the official guide to install flyctl:
    
    👉 Install flyctl

2. Pick a Name for Your App
    
    Choose a name for your app, then update that name in the following places:

    - Rename the src/ folder to match your app name.

    - In fly.toml, update the app name.

    - In pyproject.toml, change the project name.

    - In the Dockerfile, update any references to the old name.

3. Deploy Your App
    Run this command in your terminal:

    ```sh
    $ fly launch
    ```

    Follow the prompts to complete the setup.

4. To automate the deploy with each push, you have to add a token to the secrets of the repo.