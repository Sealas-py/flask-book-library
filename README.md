# Book Library REST API

REST API for online library. It supports authors of books and books resources including authentication (JWT Token).

The documentation can be found [here](https://documenter.getpostman.com/view/27068309/2s93sXcaBx#8a3b4476-a979-486d-b60b-630adba634b0) and
[dbdiagram.io](https://dbdiagram.io/d/64613a0edca9fb07c40f66e7)

## Setup

- Clone repository
- Create database and user
- Rename .env.example to `.env` and set your values
```buildoutcfg
# SQLALCHEMY_DATABASE_URI MySQL template
SQLALCHEMY_DATABASE_URI=mysql+pymysql://<db_user>:<db_password>@<db_host>/<db_name>?charset=utf8mb4
```
- Create a virtual environment
```buildoutcfg
python -m venv venv
```
- Install packages from `requirements.txt`
```buildoutcfg
pip install -r requirements.txt
```
- Migrate database
```buildoutcfg
flask db upgrade
```
- Run command
```buildoutcfg
flask run
```


**NOTE**

Import / delete example data from `book_library_app/samples`:

```buildoutcfg
# import
flask db-manage add-data

# remove
flask db-manage remove-data
```

## Tests

In order to execute tests located in `tests/` run the command:

```buildoutcfg
python -m pytest tests/
```

## Technologies / Tools

- Python 3.9.0
- Flask 2.2.3
- Alembic 1.10.4
- SQLAlchemy 2.0.10
- Pytest 7.3.1
- MySQL
- AWS
- Postman