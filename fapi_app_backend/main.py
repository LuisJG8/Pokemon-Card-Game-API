from typing import Annotated, Optional, Any
from fastapi import FastAPI, Path, Query, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import sys
import os
from pathlib import Path 
from pydantic import BaseModel, ValidationError, AfterValidator, field_validator

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.dataframe import *
from database.psql_session import *
from database.models import *




# Pydantic model
class Card(BaseModel):
    id_value: int
    p_id: str
    name: str
    type_p: Optional[str] = None
    hp: Optional[int] = 0  
    card_type: str
    sub_type: Optional[str] = None
    evolves_from: Optional[str] = None
    attacks: Optional[str] = None
    ex_rule: Optional[str] = None
    weaknesses: Optional[str] = None
    retreat_cost: Optional[int] = 0 
    artist: str
    card_description: Optional[str] = None
    set_p: str
    rarity: Optional[str] = None
    pack: Optional[str] = None
    versions: str
    image: str
    ability: Optional[str] = None


    @field_validator('hp', 'retreat_cost', mode='before')
    @classmethod
    def fix_hp_retreat_cost_types(cls, value):
        print('the value is', type(value))
        print(value)
        if isinstance(value, str):
            return float(value.strip())
        else:
            return value

     
    

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()    


db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
async def index():
    return 'Pokemon Pocket TCG API'



@app.get("/sets")
async def pokemon_sets(db: db_dependency, response_model= Card):
    all_packs = db.query(Pokemon_cards.set_p).distinct().all()
    print("the output", all_packs)
    print("the type", type(all_packs))


    if not all_packs:
        raise HTTPException(status=404, detail="Data does not exist")

    newone = [thing[0].replace("(')", "") for thing in all_packs]


    return newone



@app.get("/cards")
async def all_cards(db: db_dependency, response_model=Card):
    all_cards = db.query(Pokemon_cards).all()
    if not all_cards:
        raise HTTPException(status=404, detail="Data does not exist")
    
    return all_cards
    # return JSONResponse(content=all_cards)



@app.get("/card/{card_id}", response_model=Card)
async def search_card(card_id: str, db: db_dependency):
    print(card_id) 
    
    card_result = db.query(Pokemon_cards).filter(Pokemon_cards.p_id == card_id).first()

    if not card_result:
        raise HTTPException(status_code=404, detail=f"Card with id {card_id} not found")

    return card_result



@app.get("/cards/{card_name}/pack/{pack_name}")
async def card_data(card_name: str, pack_name: str, db: db_dependency):
    print('the cards id', card_name)
    print(Pokemon_cards.p_id)
    
    the_card = db.query(Pokemon_cards).filter(Pokemon_cards.name == card_name, Pokemon_cards.pack == pack_name).all()

    if not the_card:
        raise HTTPException(status_code=404, 
                            detail=f"Card with name {card_name} and {pack_name} not found")


    return the_card


@app.get("/cards/{card_name}/{poke_set}")
async def pokemon_set(card_name: str, poke_set: str, db: db_dependency):

    the_card = db.query(Pokemon_cards).filter(Pokemon_cards.name == card_name, Pokemon_cards.set_p == poke_set).all()

    if not the_card:
        raise HTTPException(status_code=404, 
                            detail=f"Card with name {card_name} and set name {poke_set} not found")

    return the_card