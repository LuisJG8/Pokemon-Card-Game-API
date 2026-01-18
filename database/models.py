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
# from fapi_app_backend.dq_checks import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy_utils import database_exists, create_database 
from pydantic import BaseModel

# from dataframe import ptcg_df, df_length
# from psql_session import Base, session, engine, meta, Table, insert

try:
    from psql_session import Base, session, engine, meta, Table, insert
    from dataframe import ptcg_df, df_length
except ImportError:
    from .psql_session import Base, session, engine, meta, Table, insert
    from .dataframe import ptcg_df, df_length


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')



class Pokemon_cards(Base):
   
    __tablename__ = 'pocket_tcg'
        
    id_value = Column('id', Integer, primary_key=True, autoincrement=True)
    p_id = Column('p_id', String)
    name = Column('name', String(50))
    type_p = Column('type_p', Text, nullable=True)
    hp = Column('hp', String, nullable=True, default=0)  # should be an integer
    card_type = Column('card_type', String(30))
    sub_type = Column('sub_type', Text, nullable=True)
    evolves_from = Column('evolves_from', String, nullable=True)
    attacks = Column('attacks', Text, nullable=True)
    ex_rule = Column('ex_rule', Text, nullable=True)
    weaknesses = Column('weaknesses', Text, nullable=True)
    retreat_cost = Column('retreat_cost', String, nullable=True, default=0) # should be an integer
    artist = Column('artist', String(50))
    card_description = Column('card_description', Text, nullable=True)
    set_p = Column('set_p', Text)
    rarity = Column('rarity', Text, nullable=True)
    pack = Column('pack', Text, nullable=True)
    versions = Column('versions',Text)
    image = Column('image', Text)
    ability = Column('ability', Text, nullable=True)





if __name__ == "__main__":
    # drops table
    Pokemon_cards.__table__.drop(bind=engine)

    # creates and adds the table to the database
    Pokemon_cards.__table__.create(engine)   

    for number in range(len(df_length)):
        print('the number going up\n', number)
        p_ids = df_length.iloc[number]["id"]
        print(p_ids)
        name = df_length.iloc[number]["name"]
        print(name)
        print()
        type_p = df_length.iloc[number]["type"]

        hp = df_length.iloc[number]["hp"]
        # hp = raw_hp.item() 
        
        card_types = df_length.iloc[number]["card_type"]
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


        inserting = insert(Pokemon_cards).values(
            p_id = p_ids,
            name = name,
            type_p = type_p,
            hp = hp,
            card_type = card_types,
            sub_type = sub_type,
            evolves_from = evolves_from,
            attacks = attacks,
            ex_rule = ex_rule,
            weaknesses = weaknesses,
            retreat_cost = retreat_cost,
            artist = artist,
            card_description = card_description,
            set_p = set_p,
            rarity = rarity,
            pack = pack,
            versions = versions,
            image = image,
            ability = ability
        )

        with engine.connect() as connecting:
            result = connecting.execute(inserting)
            connecting.commit()
            
        # pokemon_info =  Pokemon_cards(
        #                 p_id=p_ids, name=name, type_p=type_p,
        #                 hp=hp, card_type=card_type, sub_type=sub_type,
        #                 evolves_from=evolves_from, attacks=attacks,
        #                 ex_rule=ex_rule, retreat_cost=retreat_cost, weaknesses=weaknesses, 
        #                 artist=artist, card_description=card_description,
        #                 set_p=set_p, rarity=rarity, pack=pack, versions=versions,
        #                 image=image, ability=ability)
        
        # session.add(pokemon_info)
    
session.commit()