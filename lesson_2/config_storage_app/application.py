from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from storage import Storage
from .settings import get_storage

app = FastAPI()


class Config(BaseModel):
    runtime: str
    version: str


@app.post("/configs/")
def post_config(config: Config, storage: Storage = Depends(get_storage)):
    key = storage.generate_key(config.dict())

    storage.write(key=key, obj=config.dict())
    return JSONResponse(status_code=200, content={"config-key": key})


@app.get("/configs/{config_id}")
def get_config(config_id: str, storage: Storage = Depends(get_storage)):
    try:
        return storage.read(config_id)
    except FileNotFoundError:  # TODO this exception is implementation specific, needs refactoring
        return JSONResponse(status_code=404, content={"message": "Config not found"})


# TODO add an endpoint to get a list of all keys
@app.get("/configs/")
def get_config(storage: Storage = Depends(get_storage)):
    return JSONResponse(
        status_code=404, content={"message": "Coming soon. Data42 is 24h on it"}
    )
