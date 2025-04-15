# Creamos la conexión con SQLAlchemy y AsyncMySQL:
# La funcion a importer desde los otros modulos => get_db()
# Version 1.1.0 WilsonGuillermo

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://majo:WilsonMemo_1964@localhost/Cali"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# La funcion a importer desde los otros modulos => get_db()
def get_db():
    db = SessionLocal()
    try:
        yield  db
    finally:
        db.close()
