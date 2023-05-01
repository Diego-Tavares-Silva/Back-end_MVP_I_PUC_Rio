from flask import Flask, redirect, jsonify
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from model import *
from schemas import *
from sqlalchemy.orm.session import close_all_sessions

from sqlalchemy.exc import IntegrityError


info = Info(title="Minha API", description="Minha documentação de API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

redirect_tag = Tag(name="Redirect", description="Rota utilizada no redirecionamento para a documentação")
pedidos_tag = Tag(name="Pedidos", description="todas as rotas relacionada a tabela de pedidos")

@app.get("/", tags=[redirect_tag])
def hello_world():
    return redirect("/openapi")

@app.get("/pedidos", tags=[pedidos_tag])
def getPedidos():
    """Lê todos os itens da tabela pedidos
    """
    session = Session()
    pedidos = session.query(Pedidos).all()
    close_all_sessions()
    return jsonify({"pedidos": [get_pedido(pedido) for pedido in pedidos]})

@app.post("/pedidos", tags=[pedidos_tag])
def postPedidos(form: PedidosSchema):
    """cria um item na tabela pedidos
    """
    pedido = Pedidos(
        brand=form.brand,
        size=form.size,
        destination=form.destination,
        color=form.color
    )

    try:
        session = Session()
        session.add(pedido)
        session.commit()
        close_all_sessions()
        return 'Pedido criado com sucesso.', 201
    
    except IntegrityError as e:
        session.rollback()
        error = e.args
        return {"message": error}, 400
    
@app.delete("/pedidos", tags=[pedidos_tag])
def deletePedidos(form: FindPedidosSchema):
    """deleta um item da tabela pedidos
    """
    session = Session()
    excluido = session.query(Pedidos).filter(Pedidos.id == form.id).delete()
    
    if excluido:
        session.commit()
        close_all_sessions()
        return "Item excluido com sucesso!"
    
    else:
        return "Item não encontrado no banco"






