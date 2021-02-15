from fastapi import APIRouter
from source.schemas.gallon import GallonBase, GallonUpdate

gallon_routes = APIRouter()

fake_db = {
    1:'a',
    2:'b',
    3:'c'
}

@gallon_routes.get("/")
async def get_all():
    return fake_db

@gallon_routes.get("/{code}")
async def get_one(code: int):
    return fake_db[code]

@gallon_routes.post("/")
async def create_gallon(gallon: GallonBase):
    return gallon

@gallon_routes.put("/{code}")
async def update_gallon(code: int, gallon: GallonUpdate):
    return gallon

@gallon_routes.delete("/{code}")
async def delete_gallon(code: int):
    pass
