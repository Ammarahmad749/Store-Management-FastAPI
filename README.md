# Store-Management-FastAPI

### Create Virtual env
* Create virtual env with following commands
```console
python -m venv .venv
```
* After the virtualenv is created, you can use the following
step to activate your virtualenv

For Mac and Linux:
```console

source .venv/bin/activate

```
For Windows:
```console

.venv\Scripts\activate
```

### Install Dependency Packages

Once the virtualenv is activated, you can install the required dependencies.

```console
pip install poetry
```
```console
poetry install 
```
### Setup Database and run migrations

Once dependencies installed , go to settings.py in src and replace database_url with your db and run following commands.

```console
alembic upgrade head
```
Once migrations are run successfully, all tables must be appearing in the tables with sample data as well.
### Run it

Run the server with:
<div class="termy">

```console
// make sure you are at right directory before executing the command project root directory\src

$ uvicorn app:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>

### Access Swagger and Documentation

* Once application is running successfully, you can use following links.
For swagger:

```console
http://localhost:8000/docs
```
For documentation:

```console
http://localhost:8000/redoc
```
