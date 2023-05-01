from model import *
from pydantic import BaseModel

class PedidosSchema(BaseModel):
    brand: str
    color: str
    size: int
    destination: str

class FindPedidosSchema(BaseModel):
    id: int

def get_pedido(pedido: Pedidos):
    return {
        "id": pedido.id,
        "brand": pedido.brand,
        "color": pedido.color,
        "size": pedido.size,
        "destination": pedido.destination
    }