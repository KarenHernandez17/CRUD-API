from models import Item

items = [
    Item(id=1, name="Melón", category="Paleta de Agua"),
    Item(id=2, name="Sandía", category="Paleta de Agua"),
    Item(id=3, name="Mango", category="Paleta de Agua"),
    Item(id=4, name="Kiwi", category="Paleta de Agua"),
    Item(id=5, name="Uva", category="Paleta de Agua"),
    Item(id=6, name="Grosella", category="Paleta de Agua"),
    Item(id=7, name="Picha con Chamoy", category="Paleta de Agua"),
    Item(id=8, name="Cacahuate", category="Paleta de Agua"),
    Item(id=9, name="Limón", category="Paleta de Agua"),
    Item(id=10, name="Nanche", category="Paleta de Agua"),
    Item(id=11, name="Coco", category="Paleta de Agua"),

    Item(id=12, name="Coco", category="Paleta de Crema"),
    Item(id=13, name="Chocolate", category="Paleta de Crema"),
    Item(id=14, name="Ron con Pasas", category="Paleta de Crema"),
    Item(id=15, name="Chicle", category="Paleta de Crema"),
    Item(id=16, name="Chocomenta", category="Paleta de Crema"),
    Item(id=17, name="Chocochips", category="Paleta de Crema"),
    Item(id=18, name="Vainilla", category="Paleta de Crema"),
    Item(id=19, name="Nuez", category="Paleta de Crema"),
    Item(id=20, name="Pistache", category="Paleta de Crema"),
    Item(id=21, name="Yogurt", category="Paleta de Crema"),

    Item(id=22, name="Chicle", category="Helado"),
    Item(id=23, name="Ron con Pasas", category="Helado"),
    Item(id=24, name="Beso de Ángel", category="Helado"),
    Item(id=25, name="Fresa con Crema", category="Helado"),
    Item(id=26, name="Limón", category="Helado"),
    Item(id=27, name="Coco", category="Helado"),
    Item(id=28, name="Pistache", category="Helado"),
    Item(id=29, name="Vainilla", category="Helado"),

    Item(id=30, name="Limón", category="Agua"),
    Item(id=31, name="Jamaica", category="Agua"),
    Item(id=32, name="Horchata de Coco", category="Agua"),
    Item(id=33, name="Guanábana", category="Agua"),

    Item(id=34, name="Chocobanana", category="Postre"),
    Item(id=35, name="Chamoyada", category="Postre"),
]

def get_item_by_id(item_id: int):
    return next((item for item in items if item.id == item_id), None)