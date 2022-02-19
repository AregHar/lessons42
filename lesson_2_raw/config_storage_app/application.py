from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from storage import Storage

app = FastAPI()


class Config(BaseModel):
    runtime: str
    version: str


@app.post("/configs/")
def post_config(config: Config):
    storage = Storage(Path('local-storage'))

    key = storage.generate_key(config.dict())

    storage.write(
        key=key,
        obj=config.dict()
    )
    return JSONResponse(status_code=200, content={"config-key": key})


@app.get("/configs/{config_id}")
def get_config(config_id: str):
    storage = Storage(Path('local-storage'))

    try:
        return storage.read(config_id)
    except FileNotFoundError:
        return JSONResponse(status_code=404, content={"message": "Config not found"})
