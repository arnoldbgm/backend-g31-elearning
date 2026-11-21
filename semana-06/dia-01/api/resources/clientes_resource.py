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
      clientes = ClientesModel.query.all()
      resultado_formateado = []

      for elmt in clientes:
         formato = {
            "nombre": elmt.nombre,
            "telefono": elmt.telefono
         }
         resultado_formateado.append(formato)

      return {
         "msg": "Respuesta exitosa",
         "data": resultado_formateado
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

# Necesitamos un resource el cual permita
# Obtener los datos de un usuario, actualizarlos y elimnar al usuario

class ClienteListUpdateDelete(Resource):
   def get(self, id_cliente):
      cliente = ClientesModel.query.get(id_cliente)

      if not cliente:
         return {
            "msg": "No existe el cliente buscado"
         }, 404

      return cliente.to_dic()
   def put(self, id_cliente):
      cliente = ClientesModel.query.get(id_cliente)

      if not cliente:
         return {
            "msg": "No existe el cliente buscado"
         }, 404

      data = request.json

      if not data:
         return {
            "msg": "Debes de enviar la informacion"
         }, 400

      # Aqui ya viene la actualizacion de los valores
      if "nombre" in data:
         cliente.nombre = data["nombre"]

      if "telefono" in data:
         cliente.telefono = data["telefono"]

      if "direccion" in data:
         cliente.direccion = data["direccion"]

      db.session.commit()

      return cliente.to_dic()

   def delete(self, id_cliente):
      cliente = ClientesModel.query.get(id_cliente)

      if cliente is None:
         return {
            "msg": "No existe el cliente buscado"
         }, 404

      db.session.delete(cliente)
      db.session.commit()

      return {
         "msg": f"Cliente con id {id_cliente} eliminado exitosamente"
      }, 200