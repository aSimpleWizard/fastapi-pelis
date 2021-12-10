from fastapi import FastAPI
from routes.pelicula import pelicula

app = FastAPI()


app.include_router(pelicula)