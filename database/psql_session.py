from sqlalchemy import create_engine, select, MetaData, Table, Column, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os



SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password_here@localhost:5432/pokemon_pocket_tcg'
SQLALCHEMY_DATABASE_URL = 'postgres_connection'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session(engine)

conn = engine.connect()

meta = MetaData()
Base = declarative_base()
