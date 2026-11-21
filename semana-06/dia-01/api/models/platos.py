from db import db
from sqlalchemy.orm import Mapped, mapped_column # Creacion
from sqlalchemy import Integer, String, Float  # Tipo Columnas

class PlatosModel(db.Model):
   id_plato:Mapped[int]=mapped_column(Integer, primary_key=True)
   nombre:Mapped[str]=mapped_column(String(100), nullable=False)
   categoria:Mapped[str]=mapped_column(String)
   precio:Mapped[float]=mapped_column(Float, nullable=False)

   __tablename__ = "platos"

   def to_dic(self):
      return {
         "id_plato": self.id_plato,
         "nombre": self.nombre,
         "categoria": self.categoria,
         "precio": self.precio
      }