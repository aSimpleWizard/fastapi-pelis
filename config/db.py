from sqlalchemy import create_engine,MetaData, engine
from sqlalchemy.sql.expression import false

engine = create_engine("sqlite:///./storedb.db", connect_args ={"check_same_thread": False})

meta = MetaData()

conn = engine.connect()