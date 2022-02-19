## Lesson 2, The good, the gad, and the ugly

We write an object-storage library and a config-storage web app. We learn to tell good code from bad code using OOP design principles called SOLID.

## Object-storage library

#### Install the object-storage library

`pip install lesson_2_raw/storage`

#### Install the object-storage library in dev mode

`pip install -e lesson_2_raw/storage`

#### Test the library

`pip install -r lesson_2_raw/storage/requirements_dev.pip`
`pytest lesson_2_raw/storage -v`

## Config-storage web app

#### Install the web app and server

`pip install -r lesson_2_raw/config_storage_app/requirements.pip`

#### Run the web app

`uvicorn lesson_2_raw.config_storage_app.application:app --reload`

## New stuff 

#### Principal

- SOLID
- unittests/pytest

#### Good to know

- decorators
- packaging a library
- dependency injection (DI)
- REDIS
