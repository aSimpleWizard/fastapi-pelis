from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

peliculas = Table("peliculas", meta,
                  Column("pelicula_id", Integer, primary_key=True),
                  Column("nombre", String(255)),
                  Column("fecha", String(255)),
                  Column("comentario", String(255))
                  )

meta.create_all(engine)
