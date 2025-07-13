from typing import Annotated
from fastapi import FastAPI, Path, Query
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.models import *
from pydantic import BaseModel


# Pydantic model
class Card(BaseModel):
    pokemon_name: str 
    pack_name: str 


app = FastAPI()

@app.get("/cards")
async def get_card_data():
    print(idk)



