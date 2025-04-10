from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from models import Item
from schemas import ItemCreate, ItemUpdate
from data import items, get_item_by_id
from enum import Enum

app = FastAPI(title="API - Paletería La Vaquita")

class CategoryEnum(str, Enum):
    paleta_de_agua = "Paleta de Agua"
    paleta_de_crema = "Paleta de Crema"
    helado = "Helado"
    agua = "Agua"
    postre = "Postre"

@app.get("/items", response_model=List[Item])
def list_items(category: Optional[CategoryEnum] = Query(None, description="Filtrar por categoría")):
    if category:
        return [item for item in items if item.category.lower() == category.value.lower()]
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = get_item_by_id(item_id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item)
def create_item(item: ItemCreate):
    new_id = len(items) + 1
    new_item = Item(id=new_id, **item.dict())
    items.append(new_item)
    return new_item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_data: ItemUpdate):
    item = get_item_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.name = item_data.name
    item.category = item_data.category
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    item = get_item_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    items.remove(item)
    return {"detail": "Item deleted"}