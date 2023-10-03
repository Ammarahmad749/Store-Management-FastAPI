# Store-Management-FastAPI

### Create Virtual env
* Create virtual env with following commands
```console
$ python -m venv .venv
```
* After the virtualenv is created, you can use the following
step to activate your virtualenv.:

```console
For Mac and Linux:

$ source .venv/bin/activate
```

```console

For Windows:

$ .venv\Scripts\activate
```

### Install Dependency Packages

Once the virtualenv is activated, you can install the required dependencies.

```console
$ pip install poetry
$ poetry install 
```

### Run it

Run the server with:
<div class="termy">

```console
// make sure you are at right directory before executing the command project root directory\src

$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>