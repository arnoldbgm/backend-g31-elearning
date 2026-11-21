# Dentro de un archivo resource
# Vamo a crear toda la logica de nuestro resource
# Un reousrce es equivalente a un controlador
# Es decir dentro de un resource vamos a tener que definir como se debe de comportar un endpoint

# 01. Se solicita crear un resource que permita crear y listar clientes
# Este debe de llamarse /api/v1/clientes

from flask_restful import Resource
from flask import request
from models.clientes import ClientesModel
from db import db

# Este es la creacion de mi controlador
class ClientesAddList(Resource):
   def get(self):
      return {
         "msg": "Hola desde el get"
      }

   def post(self):
      data = request.json
      # 02. Valiar la informacion
      if not data:
         return {
            "msg": "Debes de enviar informacion"
         }, 400

      if not data["nombre"] or not data["telefono"] or not data["direccion"]:
         return {
            "msg": "Campos incompletos"
         }, 400
      
      # 03. Creacion de nuestro registro (llamas al modelo)
      nuevo_cliente = ClientesModel(
         nombre=data["nombre"],
         telefono=data["telefono"],
         direccion=data["direccion"]
      )
      # 04. Ejecucion
      # Dentro de mi bd(SQLAlchemy) de datos vas a insertar
      db.session.add(nuevo_cliente)
      db.session.commit()

      return {
         "msg": "Creacion exitosa"
      }, 201