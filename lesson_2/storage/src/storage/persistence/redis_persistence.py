# import uuid
#
# from redis import Redis
#
# from .persistence import Persistence
#
#
# class RedisPersistence(Persistence):
#     def __init__(self, host: str, port: int):
#         self._redis = Redis(host, port)
#
#     def write(self, data: str) -> uuid.UUID:
#         stored_id = self._generate_id()
#         self._redis.set(str(stored_id), data)
#         return stored_id
#
#     def read(self, stored_id: uuid.UUID):
#         return self._redis.get(str(stored_id))
