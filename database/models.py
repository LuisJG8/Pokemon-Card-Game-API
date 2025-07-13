import psycopg2
import pandas as pd
import sys 
import io
import os 
import numpy as np
from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    create_engine,
    Integer,
    MetaData,
    NVARCHAR,
    Numeric,
    String,
    Table,
    Text,
    TIMESTAMP,
    text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy_utils import database_exists, create_database 
from pydantic import BaseModel
from dataframe import ptcg_df, df_length, column_names
from psql_session import engine, SessionLocal, Base
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')




meta = MetaData()
conn = engine.connect()
session = Session(engine)


pokemon_cards = Table(
   'pocket_tcg',
    meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('p_id', String),
    Column('name', String(50)),
    Column('type_p', Text, nullable=True),
    Column('hp', String, nullable=True),  # should be an integer
    Column('card_type', String(30)),
    Column('sub_type', Text, nullable=True),
    Column('evolves_from', String, nullable=True),
    Column('attacks', Text, nullable=True),
    Column('ex_rule', Text, nullable=True),
    Column('weaknesses', Text, nullable=True),
    Column('retreat_cost', String, nullable=True), # should be an integer
    Column('artist', String(50)),
    Column('card_description', Text, nullable=True),
    Column('set_p', Text),
    Column('rarity', Text, nullable=True),
    Column('pack', Text, nullable=True),
    Column('versions',Text),
    Column('image', Text),
    Column('ability', Text, nullable=True)
)

pokemon_cards.drop(engine, checkfirst=True)
pokemon_cards.create(engine)

for number in range(len(df_length)):
    print('the number going up\n', number)
    p_ids = df_length.iloc[number]["id"]
    name = df_length.iloc[number]["name"]
    type_p = df_length.iloc[number]["type"]

    hp = df_length.iloc[number]["hp"]
    # hp = raw_hp.item() 
    
    card_type = df_length.iloc[number]["card_type"]
    sub_type = df_length.iloc[number]["sub_type"]
    evolves_from = df_length.iloc[number]["evolves_from"]
    attacks = df_length.iloc[number]["attacks"]
    ex_rule = df_length.iloc[number]["ex_rule"]
    weaknesses = df_length.iloc[number]["weaknesses"]

    # converting pandas numpy.int64 to python int so that python can use the value
    # without getting a type error 
    retreat_cost = df_length.iloc[number]["retreat_cost"]
    # retreat_cost = raw_retreat_cost.item()

    artist = df_length.iloc[number]["artist"]
    card_description = df_length.iloc[number]["card_description"]
    set_p = df_length.iloc[number]["set"]
    rarity = df_length.iloc[number]["rarity"]
    pack = df_length.iloc[number]["pack"]
    versions = df_length.iloc[number]["versions"]
    image = df_length.iloc[number]["image"]
    ability = df_length.iloc[number]["ability"]


    
    insert_statement = pokemon_cards.insert().values(id=number,
                                  p_id=p_ids, name=name, type_p=type_p,
                                  hp=hp, card_type=card_type, sub_type=sub_type,
                                  evolves_from=evolves_from, attacks=attacks,
                                  ex_rule=ex_rule, retreat_cost=retreat_cost, weaknesses=weaknesses, 
                                  artist=artist, card_description=card_description,
                                  set_p=set_p, rarity=rarity, pack=pack, versions=versions,
                                  image=image, ability=ability)
    

    with engine.connect() as connecting:
        result = connecting.execute(insert_statement)
        connecting.commit()


session.commit()
conn.close()
