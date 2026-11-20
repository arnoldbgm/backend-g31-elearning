from db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, DateTime, Float, ForeignKey
from datetime import datetime

class PedidosModel(db.Model):
   id_pedido:Mapped[int]=mapped_column(Integer, primary_key=True)
   cantidad:Mapped[int]=mapped_column(Integer, nullable=False)
   fecha:Mapped[str]=mapped_column(DateTime, default=datetime.now)
   total:Mapped[float]=mapped_column(Float, nullable=False)

   # LLaves foraneas
   id_cliente:Mapped[int]=mapped_column(Integer, ForeignKey("clientes.id_cliente"))
   id_plato:Mapped[int]=mapped_column(Integer, ForeignKey("platos.id_plato"))

   __tablename__ = "pedidos"