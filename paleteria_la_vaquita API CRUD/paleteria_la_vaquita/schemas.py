from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    category: str

class ItemUpdate(BaseModel):
    name: str
    category: str