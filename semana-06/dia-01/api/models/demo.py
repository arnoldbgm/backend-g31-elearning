from db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer

class DemoModel(db.Model):
   id:Mapped[int]=mapped_column(Integer,primary_key=True)
   numero:Mapped[int]=mapped_column(Integer)


   __tablename__ = "demotabla"