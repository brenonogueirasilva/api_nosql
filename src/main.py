from fastapi import FastAPI

from src.routes.imdb import router_imdb
from src.ingestion.data_ingestion import router_ingestion

app = FastAPI()

app.include_router(router_imdb)
app.include_router(router_ingestion)








