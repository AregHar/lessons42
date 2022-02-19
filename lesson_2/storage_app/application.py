import uuid

from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from storage.storage import Storage

from lesson_2.storage_app.settings import get_storage

app = FastAPI()


class Config(BaseModel):
    version: str
    runtime: str


@app.post("/configs/")
def read_root(config: Config, storage: Storage = Depends(get_storage, use_cache=True)):
    id_ = storage.store(config.dict())
    return {"config-id": id_}


@app.get("/configs/{config_id}")
def read_item(
    config_id: uuid.UUID, storage: Storage = Depends(get_storage, use_cache=True)
):
    try:
        obj = storage.restore(config_id)
    except Exception:  # Why not FileNotFoundError
        return JSONResponse(status_code=404, content={"message": "Config not found"})

    return Config(**obj)
