### redis

- redis-cli
  - KEYS *
  - SET key value
  - GET key
- redis


serializer=json persistence=redis uvicorn lesson_2.storage_app.application:app --reload


todo

add tests to the fast api
