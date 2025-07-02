import psycopg2
import pandas as pd
import sys 
import io
import os 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


ptcg_df = pd.read_csv('database/data/pokemon_ptcg_data.csv', encoding='latin1')
print(ptcg_df.head(5))
first_t = ptcg_df.head(30)

print('second row\n')
# print(first_t.iloc[thing])

column_names = ptcg_df.columns


# print('name', first_t.iloc[thing]['name'])
# print('type', first_t.iloc[thing]['type'])
# print('hp', first_t.iloc[thing]['hp'])

# for thing in range(0, 29):
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
#     version = first_t.iloc[thing]["version"]
#     image = first_t.iloc[thing]["image"]
#     ability = first_t.iloc[thing]["ability"]
#     print(name, typee, hp, card_type, sub_type, evolves_from, attacks, ex_rule, weaknesses, retreat_cost, artist, card_description, sett, idd, rarity, pack, version, image, ability)
#     print()



if __name__ == '__main__':
    print()
    # database connection settings
    conn = psycopg2.connect(dbname='postgres', 
                            user='postgres',
                            host='localhost', 
                            password="Glades2015@", 
                            port=5432)

    cur = conn.cursor()
    print('starting cursor')

    print('executing scripts')

    cur.execute("DROP TABLE IF EXISTS pokemon_ptcg; " \
                "CREATE TABLE pokemon_ptcg "
                "(id serial PRIMARY KEY, " \
                 "p_id text," \
                 "name text, " \
                 "type text," \
                 "card_type text," \
                 "sub_type text," \
                 "evolves_from text," \
                 "hp bigint," \
                 "ability text," \
                 "attacks text," \
                 "ex_rule text," \
                 "weaknesses text," \
                 "retreat_cost bigint," \
                 "card_description text," \
                 "set text," \
                 "version text," \
                 "rarity text," \
                 "pack text," \
                 "image text," \
                 "artist text);")

for thing in range(0, 29):
    name = first_t.iloc[thing]["name"]
    typee = first_t.iloc[thing]["type"]
    hp = first_t.iloc[thing]["hp"]
    card_type = first_t.iloc[thing]["card_type"]
    sub_type = first_t.iloc[thing]["sub_type"]
    evolves_from = first_t.iloc[thing]["evolves_from"]
    attacks = first_t.iloc[thing]["attacks"]
    ex_rule = first_t.iloc[thing]["ex_rule"]
    weaknesses = first_t.iloc[thing]["weaknesses"]
    retreat_cost = first_t.iloc[thing]["retreat_cost"]
    artist = first_t.iloc[thing]["artist"]
    card_description = first_t.iloc[thing]["card_description"]
    sett = first_t.iloc[thing]["set"]
    idd = first_t.iloc[thing]["id"]
    rarity = first_t.iloc[thing]["rarity"]
    pack = first_t.iloc[thing]["pack"]
    version = first_t.iloc[thing]["version"]
    image = first_t.iloc[thing]["image"]
    ability = first_t.iloc[thing]["ability"]
    print(name, typee, hp, card_type, sub_type, evolves_from, attacks, ex_rule, weaknesses, retreat_cost, artist, card_description, sett, idd, rarity, pack, version, image, ability)
    print(thing)
    cur.execute("INSERT INTO pokemon_ptcg (p_id, name, type, card_type, sub_type, evolves_from, hp, ability, attacks, ex_rule, weaknesses, retreat_cost, card_description, set, version, rarity, pack, image, artist) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                (idd, name, typee, card_type, sub_type, evolves_from, hp, ability, attacks, ex_rule, weaknesses, retreat_cost, card_description, sett, version, rarity, pack, image, artist))

conn.commit() 
print('changes were commited to the database')

cur.close()
conn.close()

