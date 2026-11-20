# Dentro de este archivo vamos a crear la tabla
# Vamos a importar SQLAlchemy
from db import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

# db.Model => Que esta clase es una tabla
class ClientesModel(db.Model):
   # ✖️ Sintaxis antigua
   # id = db.Column(db.Integer, primary_key = True)

   # Mapped => Especificiar el tipo de la columna
   # mapped_column => Crear la columna
   # nullAble => ¿Puede ser esta columna nula?

   id_cliente:Mapped[int] = mapped_column(Integer, primary_key=True)
   nombre:Mapped[str] = mapped_column(String(100), nullable=False)
   telefono:Mapped[str] = mapped_column(String(9))
   direccion:Mapped[str] = mapped_column(String(200))

   # Para nombrar a tu tabla usas __tablename__
   __tablename__ = "clientes"