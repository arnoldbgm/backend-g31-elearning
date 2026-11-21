# Aqui vamos a crear nuestro archivo base (cerebro) 🧠
# Crear el servidor
from flask import Flask
from db import db  # SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)

# ⚙️ 03. Configuraciones
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
# Integracion de SQLAlchemy en mi proyecto
db.init_app(app)
# Ejecuccion de Flask Migrate
migrate = Migrate(app, db)
api = Api(app)

# Importacion de los modelos (models/__init__.py los importa todos)
from models.clientes import ClientesModel
from models.pedidos import PedidosModel
from models.platos import PlatosModel
from models.demo import DemoModel

# Aqui vamos a definir nuestros endpoints
from resources.clientes_resource import ClientesAddList, ClienteListUpdateDelete
from resources.platos_resource import PlatosAddList, PlatosListUpdateDelete
from resources.pedidos_resource import PedidosList

api.add_resource(ClientesAddList, "/api/v1/clientes")
api.add_resource(PlatosAddList, "/api/v1/platos")
api.add_resource(ClienteListUpdateDelete, "/api/v1/clientes/<int:id_cliente>")
api.add_resource(PlatosListUpdateDelete, "/api/v1/platos/<int:id_plato>")
api.add_resource(PedidosList, "/api/v1/pedidos")

if __name__ == "__main__":
   app.run(debug=True)