import psycopg2
import pandas as pd
import sys 
import io
import os 
from sqlalchemy import create_engine, text, Column, Integer, String, TIMESTAMP, Boolean, Text, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy_utils import database_exists, create_database 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


ptcg_df = pd.read_csv('./database/data/pokemon_ptcg_data.csv', encoding='utf-8')
ptcg_df_lenght = len(ptcg_df)
print(ptcg_df_lenght)
print(ptcg_df)
first_t = ptcg_df.head(ptcg_df_lenght)

print(ptcg_df.columns.tolist())
column_names = ptcg_df.columns



SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:HelloWorld12@localhost:5432/pokemon_pocket_tcg'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

if not database_exists(engine.url):
    create_database(engine.url)
print(database_exists(engine.url))


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

conn = engine.connect()

session = Session(engine)

class Pokemon_Cards(Base):
    __tablename__ = 'pocket_tcg'

    id_p = Column(Integer, primary_key=True, autoincrement=True) 
    name = Column(String(100))
    type_p = Column(Text)
    card_type = Column(Text)
    sub_type = Column(Text)
    evolves_from = Column(Text)
    hp = Column(Numeric(300))
    ability = Column(Text)
    attacks = Column(Text)
    ex_rule = Column(Text)
    weaknesses = Column(Text)
    retreat_cost = Column(Numeric(10))
    card_description = Column(Text)
    set_p = Column(Text)
    versions = Column(Text)
    rarity = Column(Text)
    pack = Column(Text)
    image = Column(Text)
    artist = Column(Text)


for thing in range(len(ptcg_df)):
    ingest_data = Pokemon_Cards(

            name = first_t.iloc[thing]["name"],
            type = first_t.iloc[thing]["type"],
            hp = first_t.iloc[thing]["hp"],
            card_type = first_t.iloc[thing]["card_type"],
            sub_type = first_t.iloc[thing]["sub_type"],
            evolves_from = first_t.iloc[thing]["evolves_from"],
            attacks = first_t.iloc[thing]["attacks"],
            ex_rule = first_t.iloc[thing]["ex_rule"],
            weaknesses = first_t.iloc[thing]["weaknesses"],
            retreat_cost = first_t.iloc[thing]["retreat_cost"],
            artist = first_t.iloc[thing]["artist"],
            card_description = first_t.iloc[thing]["card_description"],
            sett = first_t.iloc[thing]["set"],
            id = first_t.iloc[thing]["id"],
            rarity = first_t.iloc[thing]["rarity"],
            pack = first_t.iloc[thing]["pack"],
            versions = first_t.iloc[thing]["version"],
            image = first_t.iloc[thing]["image"],
            ability = first_t.iloc[thing]["ability"],
    )

    session.add(ingest_data)

session.commit()
session.close()

# Base.metadata.create_all(engine)


# for thing in range(len(ptcg_df)):
#     name = first_t.iloc[thing]["name"]
#     typee = first_t.iloc[thing]["type"]
#     hp = first_t.iloc[thing]["hp"]
#     card_type = first_t.iloc[thing]["card_type"]
#     sub_type = first_t.iloc[thing]["sub_type"]
#     evolves_from = first_t.iloc[thing]["evolves_from"]
#     attacks = first_t.iloc[thing]["attacks"]
#     ex_rule = first_t.iloc[thing]["ex_rule"]
#     weaknesses = first_t.iloc[thing]["weaknesses"]
#     retreat_cost = first_t.iloc[thing]["retreat_cost"]
#     artist = first_t.iloc[thing]["artist"]
#     card_description = first_t.iloc[thing]["card_description"]
#     sett = first_t.iloc[thing]["set"]
#     idd = first_t.iloc[thing]["id"]
#     rarity = first_t.iloc[thing]["rarity"]
#     pack = first_t.iloc[thing]["pack"]
#     versions = first_t.iloc[thing]["version"]
#     image = first_t.iloc[thing]["image"]
#     ability = first_t.iloc[thing]["ability"]
#     print(name, typee, hp, card_type, sub_type, evolves_from, attacks, ex_rule, weaknesses, retreat_cost, artist, 
#         card_description, sett, idd, rarity, pack, versions, image, ability)
#     print(thing)
#     Base.execute(text("INSERT INTO pokemon_ptcg (p_id, name, type, card_type, sub_type, evolves_from, hp, ability, attacks, ex_rule, weaknesses, retreat_cost, card_description, set, version, rarity, pack, image, artist) VALUES (p_id, name, type, card_type, sub_type, evolves_from, hp, ability, attacks, ex_rule, weaknesses, retreat_cost, card_description, set, versions, rarity, pack, image, artist);"))



# conn.execute(text("DROP TABLE IF EXISTS pokemon_ptcg; "
#             "CREATE TABLE pokemon_ptcg "
#             "(id serial PRIMARY KEY, "
#                 "p_id text,"
#                 "name varchar(100), "
#                 "type text,"
#                 "card_type text,"
#                 "sub_type text,"
#                 "evolves_from text,"
#                 "hp numeric(10),"
#                 "ability text,"
#                 "attacks text,"
#                 "ex_rule text,"
#                 "weaknesses text,"
#                 "retreat_cost numeric(10),"
#                 "card_description text,"
#                 "set text,"
#                 "versions text,"
#                 "rarity text,"
#                 "pack text,"
#                 "image text,"
#                 "artist text);"))

# for thing in range(len(ptcg_df)):
#     name = first_t.iloc[thing]["name"]
#     typee = first_t.iloc[thing]["type"]
#     hp = first_t.iloc[thing]["hp"]
#     card_type = first_t.iloc[thing]["card_type"]
#     sub_type = first_t.iloc[thing]["sub_type"]
#     evolves_from = first_t.iloc[thing]["evolves_from"]
#     attacks = first_t.iloc[thing]["attacks"]
#     ex_rule = first_t.iloc[thing]["ex_rule"]
#     weaknesses = first_t.iloc[thing]["weaknesses"]
#     retreat_cost = first_t.iloc[thing]["retreat_cost"]
#     artist = first_t.iloc[thing]["artist"]
#     card_description = first_t.iloc[thing]["card_description"]
#     sett = first_t.iloc[thing]["set"]
#     idd = first_t.iloc[thing]["id"]
#     rarity = first_t.iloc[thing]["rarity"]
#     pack = first_t.iloc[thing]["pack"]
#     versions = first_t.iloc[thing]["version"]
#     image = first_t.iloc[thing]["image"]
#     ability = first_t.iloc[thing]["ability"]
#     print(name, typee, hp, card_type, sub_type, evolves_from, attacks, ex_rule, weaknesses, retreat_cost, artist, 
#         card_description, sett, idd, rarity, pack, versions, image, ability)
#     print(thing)
#     session.execute(text("INSERT INTO pokemon_ptcg (p_id, name, type, card_type, sub_type, evolves_from, hp, ability, attacks, ex_rule, weaknesses, retreat_cost, card_description, set, version, rarity, pack, image, artist) VALUES (p_id, name, type, card_type, sub_type, evolves_from, hp, ability, attacks, ex_rule, weaknesses, retreat_cost, card_description, set, versions, rarity, pack, image, artist);"))


# conn.commit() 
# print('changes were commited to the database')

# conn.close()
    



# if __name__ == '__main__':
#     print()
#     # database connection settings
#     conn = psycopg2.connect(dbname='postgres', 
#                             user='postgres',
#                             host='localhost', 
#                             password="Glades2015@", 
#                             port=5432)
    
#     cur = conn.cursor()
#     print('starting cursor')

#     print('executing scripts')
