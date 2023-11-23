from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/productos",
                   responses={404: {"message": "Not found"}})


class Producto(BaseModel):
    id: int
    nombre: str
    color: str


lista_productos = [Producto(id=1, nombre="Coche", color="Rojo"), Producto(
    id=2, nombre="Pelota", color="Azul")]


@router.get("/")
async def root():
    return list(lista_productos)
