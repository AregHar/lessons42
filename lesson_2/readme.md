## Lesson 2, The good, the bad, and the ugly

We write an object-storage library and a config-storage web app. We learn to tell good code from bad code using OOP design principles called SOLID.

## Object-storage library

#### Install the object-storage library

`pip install lesson_2/storage`

#### Install the object-storage library in dev mode

`pip install -e lesson_2/storage`

#### Test the library

`pip install -r lesson_2/storage/requirements_dev.pip`
`pytest lesson_2/storage -v`

## Config-storage web app

#### Install the web app and server

`pip install -r lesson_2/config_storage_app/requirements.pip`

#### Setup Redis

- install the Redis server
- run the Redis server. On linux/mac it's `redis-server`

#### Run the web app

`persistence=file serializer=yaml uvicorn lesson_2.config_storage_app.application:app --reload`

#### Use the web app

In the browser, open `http://127.0.0.1:8000/docs` (or whatever path the server runs on)

persistence options
- file
- redis

serializer options
- json
- yaml

## New stuff 

#### Principal

- SOLID
- composition

#### Good to know

- unittests/pytest
- decorators
- packaging a library
- dependency injection (DI)
- REDIS
