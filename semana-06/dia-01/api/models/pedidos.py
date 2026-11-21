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

   def to_dic(self):
      return {
         "id_pedido": self.id_pedido,
         "cantidad": self.cantidad,
         "total": self.total,
         "id_cliente": self.id_cliente,
         "id_plato": self.id_plato
      }