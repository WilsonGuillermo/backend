# Creamos la conexión con SQLAlchemy y AsyncMySQL:
# Version 1.0.0 WilsonGuillermo

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://majo:WilsonMemo_1964@localhost/Cali"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
