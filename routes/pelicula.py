from fastapi import APIRouter
from config.db import conn
from models.pelicula import peliculas
from schemas.pelicula import Pelicula

pelicula = APIRouter()

@pelicula.get("/", tags=["Pelicula"])
def get_peliculas():
    return conn.execute(peliculas.select()).fetchall()

@pelicula.get("/peliculas", tags=["Pelicula"])
def get_peliculas():
    return conn.execute(peliculas.select()).fetchall()

@pelicula.post("/peliculas", tags=["Pelicula"])
def create_pelicula(pelicula : Pelicula):
    new_pelicula = {
        "nombre" : pelicula.nombre,
        "fecha" : pelicula.fecha,
        "comentario" : pelicula.comentario
    }
    result = conn.execute(peliculas.insert().values(new_pelicula))
    return conn.execute(peliculas.select().where(peliculas.c.pelicula_id == result.lastrowid)).first()

@pelicula.get("/peliculas/{id}",tags=["Pelicula"])
def get_pelicula(id:int):
    return conn.execute(peliculas.select().where(peliculas.c.pelicula_id == id)).first()

@pelicula.put("/peliculas/{id}",tags=["Pelicula"])
def update_pelicula(pelicula: Pelicula, id : int):
    conn.execute(
        peliculas.update()
        .values(nombre = pelicula.nombre, fecha = pelicula.fecha, comentario = pelicula.comentario)
        .where(peliculas.c.pelicula_id == id)
    )
    return conn.execute(peliculas.select().where(peliculas.c.pelicula_id == id)).first()

@pelicula.delete("/peliculas/{id}",tags=["Pelicula"])
def delete_pelicula(id : int):
    conn.execute(peliculas.delete().where(peliculas.c.pelicula_id == id))
    return conn.execute(peliculas.select().where(peliculas.c.pelicula_id == id)).first()

