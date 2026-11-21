from flask_restful import Resource
from models.pedidos import PedidosModel
from models.clientes import ClientesModel
from models.platos import PlatosModel

class PedidosList(Resource):
   def get(self):
      #
      # SQL
      # SELECT pedidos.id_pedido, pedidos.cantidad, pedidos.total, clientes.id_cliente, clientes.nombre, platos.id_plato, platos.nombre
      # JOIN clientes ON pedidos.id_cliente = clientes.id_cliente
      # JOIN platos ON pedidos.id_plato = platos.id_plato

      # PedidosModel.query.join("clientes").join("platos").all()
      pedidos = PedidosModel.query.join(ClientesModel).add_column(ClientesModel.nombre).all()

      print(pedidos) # [PedidosModel1]

      resultado_formateado = []

      for elmt in pedidos:
         formato = {
            "id_pedido": elmt[0].id_pedido,
            "cantidad": elmt[0].cantidad,
            "total": elmt[0].total,
            "cliente": {
               "id_cliente": elmt[0].id_cliente,
               "nombre": elmt[1]
            },
         }

         resultado_formateado.append(formato)
      return resultado_formateado

      # FORMATO ESPERADO
      # {
      #    "id_pedido": 1,
      #    "cantidad": 2,
      #    "total": 50,
      #    "cliente": {
      #       "id_cliente": 1,
      #       "nombre": "Juan",
      #    },
      #    "plato": {
      #       "id_plato": 1,
      #       "nombre": "Pizza",
      #    }
      # }