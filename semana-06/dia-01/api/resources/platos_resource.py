# RETO 01
# Crear un endpoint para poder insertar platos y listar platos
# /api/v1/platos
# Ademas este endpoint debe tener una validacion para evitar
# [OBLIG]que se introduzcan platos negativos
# [OPCIONAL]que se introduzcan campos vacios "         "

from flask_restful import Resource
from models.platos import PlatosModel
from flask import request
from db import db

class PlatosAddList(Resource):
   def get(self):
      platos = PlatosModel.query.all()
      # [PlatosModel1, PlatosModel2]
      resultado_formateado = []
      for elmt in platos:
         formato = {
            "id_plato": elmt.id_plato,
            "nombre": elmt.nombre,
            "categoria": elmt.categoria,
            "precio": elmt.precio
         }
         resultado_formateado.append(formato)

      return {
         "msg": "Respuesta exitosa",
         "data": resultado_formateado
      }, 200

   def post(self):
      data = request.json

      if not data:
         return {
            "msg": "Error data no enviada"
         }, 400

      if data["precio"] <= 0:
         return {
            "msg": "El precio no puede ser negativo"
         }, 400

      nuevo_plato = PlatosModel(
         nombre=data["nombre"],
         categoria=data["categoria"],
         precio=data["precio"]
      )
      db.session.add(nuevo_plato)
      db.session.commit()

      return {
         "msg": "Plato creado exitosamente"
      }, 201
